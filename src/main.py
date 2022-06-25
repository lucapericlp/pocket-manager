from typing import Sequence
from src.filter_items import filter_for_elapsed
from src.get_items import PocketItem, get_favourite_items
from src.notifications import send_notifications
from src.tags import update_empty_tags

def advance_sr_tags(items: Sequence[PocketItem]) -> Sequence[PocketItem]:
    ...

def run_sr_manager():
    tagged_items = update_empty_tags(get_favourite_items())
    elapsed_items = filter_for_elapsed(tagged_items)
    if elapsed_items:
        notified_items = send_notifications(elapsed_items)
        advance_sr_tags(notified_items)

if __name__ == "__main__":
    run_sr_manager()
