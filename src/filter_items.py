from typing import Sequence
import datetime
from src.get_items import PocketItem


def filter_for_elapsed(items: Sequence[PocketItem]) -> Sequence[PocketItem]:
    elapsed = []
    for item in items:
        latest_tag = int(max(item.tags).split("-")[1])
        time_to_notify = item.time_added + datetime.timedelta(days=latest_tag)
        if datetime.datetime.now() > time_to_notify:
            elapsed.append(item)
    return elapsed
