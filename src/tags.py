from dataclasses import asdict
from typing import Sequence
import requests
from src.config import API_HOST, POCKET_ACCESS_TOKEN, POCKET_CONSUMER_KEY
from src.get_items import PocketItem

POCKET_MODIFY_ENDPOINT = f"{API_HOST}/send"
INITIAL_SR_TAG = "sr-1"

def update_empty_tags(items: Sequence[PocketItem]) -> Sequence[PocketItem]:
    keys = {"consumer_key": POCKET_CONSUMER_KEY, "access_token": POCKET_ACCESS_TOKEN}
    query = {"action": "tags_add", "tags": INITIAL_SR_TAG}
    tagged_items = []

    for item in items:
        if not item.tags:
            actions = [{**query, "item_id": item.item_id}]
            resp = requests.post(
                POCKET_MODIFY_ENDPOINT, json={**keys, "actions": actions}
            )
            response = resp.json()
            if not int(response["status"]):
                print("Pocket encountered an error. Ignoring...")
            item = PocketItem.from_dict({**asdict(item), "tags": [INITIAL_SR_TAG]})
        tagged_items.append(item)
    return tagged_items
