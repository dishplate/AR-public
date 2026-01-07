#amazing, this works!
#It posts to slack
import requests
import os

output = ('Hello world')

# Send results to Slack
# SLACK_WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL")
SLACK_WEBHOOK_URL = "https://hooks.slack.com/services/MY_SLACK_URL"
if SLACK_WEBHOOK_URL:
    message = output
    requests.post(
        SLACK_WEBHOOK_URL,
        json={"text": message}
    )
print(f"Output sent to Slack: {output}")
print(requests.get(SLACK_WEBHOOK_URL).status_code)
