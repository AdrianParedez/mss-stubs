from types import TracebackType
from typing import Self

class ScreenShot:
    size: tuple[int, int]
    bgra: bytes

class MSSBase:
    monitors: list[dict[str, int]]
    def grab(self, monitor: dict[str, int]) -> ScreenShot: ...
    def __enter__(self) -> Self: ...
    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None: ...

def MSS() -> MSSBase: ...
