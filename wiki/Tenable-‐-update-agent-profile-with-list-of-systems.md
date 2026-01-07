~~~
import requests

# === CONFIGURATION ===
access_key = 'YOUR_ACCESS_KEY'
secret_key = 'YOUR_SECRET_KEY'
agent_uuid = 'AGENT_UUID_TO_ADD'
agent_group_id = 'AGENT_GROUP_ID'  # Integer
base_url = 'https://cloud.tenable.com'  # Or your regional URL

# === HEADERS ===
headers = {
    'Content-Type': 'application/json',
    'X-ApiKeys': f'accessKey={access_key}; secretKey={secret_key}'
}

# === PAYLOAD ===
payload = { "criteria": {
        "all_agents": False,
        "hardcoded_filters": ["agent_string_here"]
    } }

# === REQUEST ===
url = f'{base_url}/agent-groups/{agent_group_id}/agents/_bulk/add'
response = requests.post(url, headers=headers, json=payload)

# === OUTPUT RESULT ===
print(f'Status Code: {response.status_code}')
print(response.json())


~~~