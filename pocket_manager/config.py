from os import environ as env

POCKET_CONSUMER_KEY = env.get("POCKET_CONSUMER_KEY")
API_HOST = "https://getpocket.com/v3"
POCKET_MODIFY_ENDPOINT = f"{API_HOST}/send"

POCKET_ACCESS_TOKEN = env.get("POCKET_ACCESS_TOKEN")
SLACK_WEBHOOK_URL = env.get("SLACK_WEBHOOK_URL")
