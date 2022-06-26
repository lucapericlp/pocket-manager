from typing import Sequence
from pocket_manager.filter_items import filter_for_elapsed
from pocket_manager.get_items import PocketItem, get_favourite_items
from pocket_manager.notifications import send_notification
from pocket_manager.tags import get_latest_tag, update_empty_tags, update_with_tags

def advance_sr_tags(items: Sequence[PocketItem]) -> Sequence[PocketItem]:
    advanced_items = []
    for item in items:
        new_tag = f"sr-{get_latest_tag(item)*2}"
        new_item = update_with_tags(item, [*item.tags, new_tag])
        advanced_items.append(new_item)
    return advanced_items


def run_sr_manager():
    tagged_items = update_empty_tags(get_favourite_items())
    elapsed_items = filter_for_elapsed(tagged_items)
    if elapsed_items:
        if not send_notification(elapsed_items):
            raise Exception("Failed to send notifications!")
        advance_sr_tags(elapsed_items)

def lambda_handler(event, context):
    run_sr_manager()
    return {"status": "Success"}

if __name__ == "__main__":
    run_sr_manager()
