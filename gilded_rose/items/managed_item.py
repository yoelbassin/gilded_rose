from typing import Protocol


class ManagedItem(Protocol):
    def update_quality(self) -> None:
        ...
