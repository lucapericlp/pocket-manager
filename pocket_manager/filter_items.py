from typing import Sequence
import datetime
from pocket_manager.get_items import PocketItem
from pocket_manager.tags import get_latest_tag


def filter_for_elapsed(items: Sequence[PocketItem]) -> Sequence[PocketItem]:
    elapsed = []
    for item in items:
        latest_tag = get_latest_tag(item)
        time_to_notify = item.time_added + datetime.timedelta(days=latest_tag)
        if datetime.datetime.now() > time_to_notify:
            elapsed.append(item)
    return elapsed
