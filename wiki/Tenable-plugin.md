~~~

from tenable.io import TenableIO

# Initialize Tenable.io connection
tio = TenableIO('YOUR_ACCESS_KEY', 'YOUR_SECRET_KEY')

# Get list of all agents
agents = tio.agents.list()

# Extract agent ID and last plugin update date
agent_data = []
for agent in agents:
    agent_data.append({
        'Agent ID': agent['id'],
        'Hostname': agent['name'],
        'Last Plugin Update': agent.get('last_plugin_update_time', 'N/A')
    })

# Print or process the results
for agent in agent_data:
    print(agent)

~~~