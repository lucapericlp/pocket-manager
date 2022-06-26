import datetime
from typing import Dict, List, Sequence
import requests
from dataclasses import dataclass, field
from dataclasses_json import dataclass_json

from pocket_manager.config import API_HOST, POCKET_CONSUMER_KEY, POCKET_ACCESS_TOKEN

POCKET_GET_ENDPOINT = f"{API_HOST}/get"

@dataclass_json
@dataclass
class PocketItem:
    item_id: int
    resolved_url: str
    time_added: datetime.datetime
    tags: List[str] = field(default_factory=list)

    @classmethod
    def type_conversions(cls, item):
        overrides = {
            "item_id": int(item["item_id"]),
            "time_added": datetime.datetime.utcfromtimestamp(int(item["time_added"])),
            "tags": list(item.get("tags", {}).keys())
        }
        return {**item, **overrides}

def get_favourite_items() -> Sequence[PocketItem]:
    keys = {"consumer_key": POCKET_CONSUMER_KEY, "access_token": POCKET_ACCESS_TOKEN}
    query = {"favorite": 1, "since": 1, "sort": "newest", "detailType": "complete"}
    response = requests.post(POCKET_GET_ENDPOINT, json={**keys, **query}).json()
    return [
        PocketItem.from_dict(PocketItem.type_conversions(item))  # type: ignore
        for item in response["list"].values()
    ]
