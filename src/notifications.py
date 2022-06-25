from typing import Sequence, Tuple
from src.get_items import PocketItem


def send_notifications(
    items: Sequence[PocketItem]
) -> Sequence[Tuple[PocketItem, bool]]:
    ...
