from os import environ as env

POCKET_CONSUMER_KEY = env.get("POCKET_CONSUMER_KEY", "102564-a5c83c555be8e0e65609cb8")
API_HOST = "https://getpocket.com/v3"
POCKET_MODIFY_ENDPOINT = f"{API_HOST}/send"

# how long will this last?
POCKET_ACCESS_TOKEN = "2e1e3a51-b7ab-0bfd-9129-ddd436"
SLACK_WEBHOOK_URL = "https://hooks.slack.com/services/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"
