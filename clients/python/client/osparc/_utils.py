import asyncio
import hashlib
import os
from pathlib import Path
from typing import AsyncGenerator, Callable, Generator, Optional, Tuple, TypeVar, Union

import httpx
from osparc_client import (
    ApiClient,
    File,
    Job,
    PageFile,
    PageJob,
    PageSolver,
    PageStudy,
    Solver,
    Study,
)

_KB = 1024  # in bytes
_MB = _KB * 1024  # in bytes
_GB = _MB * 1024  # in bytes

Page = Union[PageJob, PageFile, PageSolver, PageStudy]
T = TypeVar("T", Job, File, Solver, Study)


class PaginationGenerator:
    """Class for wrapping paginated http methods as generators"""

    def __init__(
        self,
        first_page_callback: Callable[[], Page],
        api_client: ApiClient,
        base_url: str,
        auth: Optional[httpx.BasicAuth],
    ):
        self._first_page_callback: Callable[[], Page] = first_page_callback
        self._api_client: ApiClient = api_client
        self._next_page_url: Optional[str] = None
        self._client: httpx.Client = httpx.Client(
            auth=auth, base_url=base_url, follow_redirects=True
        )

    def __del__(self):
        self._client.close()

    def __len__(self) -> int:
        """Number of elements which the iterator can produce"""
        page: Page = self._first_page_callback()
        assert isinstance(page.total, int)
        return page.total

    def __iter__(self) -> Generator[T, None, None]:
        """Returns the generator"""
        if len(self) == 0:
            return
        page: Page = self._first_page_callback()
        while True:
            assert page.items is not None
            assert isinstance(page.total, int)
            yield from page.items
            if page.links.next is None:
                break
            response: httpx.Response = self._client.get(page.links.next)
            page = self._api_client._ApiClient__deserialize(response.json(), type(page))


async def file_chunk_generator(
    file: Path, chunk_size: int
) -> AsyncGenerator[Tuple[bytes, int], None]:
    if not file.is_file():
        raise RuntimeError(f"{file} must be a file")
    if chunk_size <= 0:
        raise RuntimeError(f"chunk_size={chunk_size} must be a positive int")
    bytes_read: int = 0
    file_size: int = file.stat().st_size
    while bytes_read < file_size:
        with open(file, "rb") as f:
            f.seek(bytes_read)
            nbytes = (
                chunk_size
                if (bytes_read + chunk_size <= file_size)
                else (file_size - bytes_read)
            )
            assert nbytes > 0
            chunk = await asyncio.get_event_loop().run_in_executor(None, f.read, nbytes)
            yield chunk, nbytes
            bytes_read += nbytes


S = TypeVar("S")


async def _fcn_to_coro(callback: Callable[..., S], *args) -> S:
    """Get a coroutine from a callback."""
    result = await asyncio.get_event_loop().run_in_executor(None, callback, *args)
    return result


def compute_sha256(file: Path) -> str:
    assert file.is_file()
    sha256 = hashlib.sha256()
    with open(file, "rb") as f:
        while True:
            data = f.read(100 * _KB)
            if not data:
                break
            sha256.update(data)
        return sha256.hexdigest()


def dev_features_enabled() -> bool:
    return os.environ.get("OSPARC_DEV_FEATURES_ENABLED") == "1"
