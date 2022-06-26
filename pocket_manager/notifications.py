from typing import Mapping, Sequence
from collections import defaultdict
import requests
from pocket_manager.config import SLACK_WEBHOOK_URL
from pocket_manager.get_items import PocketItem
from pocket_manager.tags import get_latest_tag


def send_notification(
    items: Sequence[PocketItem]
) -> bool:
    bucketed_reviews: Mapping[int, Sequence[PocketItem]] = defaultdict(list)
    for item in items:
        latest_tag = get_latest_tag(item)
        bucketed_reviews[latest_tag].append(item)

    output_str = "<!channel> Spaced Repetition time!\n\n"
    for bucket, items in bucketed_reviews.items():
        to_review = "\n".join([f"• {item.resolved_url}" for item in items])
        output_str += f"{bucket} days have passed since you last reviewed:\n\n{to_review}\n\n"

    result = requests.post(SLACK_WEBHOOK_URL, json={"text": output_str})
    if result.status_code != 200:
        return False
    return True
