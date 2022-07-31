from dataclasses import asdict
from typing import Sequence
import requests
from pocket_manager.config import POCKET_ACCESS_TOKEN, POCKET_CONSUMER_KEY, POCKET_MODIFY_ENDPOINT
from pocket_manager.get_items import PocketItem

INITIAL_SR_TAG = "sr-1"

def get_latest_tag(item: PocketItem) -> int:
    return max([int(tag.split("-")[1]) for tag in item.tags])


def update_with_tags(item: PocketItem, desired_tags: Sequence[str]) -> PocketItem:
    """ this should be a nice instance method for the PocketItem model """
    tags = ",".join(desired_tags)
    keys = {"consumer_key": POCKET_CONSUMER_KEY, "access_token": POCKET_ACCESS_TOKEN}
    query = {"action": "tags_add", "tags": tags}

    actions = [{**query, "item_id": item.item_id}]
    resp = requests.post(
        POCKET_MODIFY_ENDPOINT, json={**keys, "actions": actions}
    )
    response = resp.json()
    if not int(response["status"]):
        print(f"Pocket encountered an error updating tags for {item.item_id}. Ignoring...")
    return PocketItem.from_dict({**asdict(item), "tags": desired_tags})


def update_empty_tags(items: Sequence[PocketItem]) -> Sequence[PocketItem]:
    tagged_items = []

    for item in items:
        if not item.tags:
            item = update_with_tags(item, [INITIAL_SR_TAG])
        tagged_items.append(item)
    return tagged_items
