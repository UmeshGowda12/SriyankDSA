import yaml

# Define the global and route configuration directly in the script
config = {
    'global': {
        'resolve_timeout': '10s'
    },
    'route': {
        'group_by': ['...'],
        'group_interval': '10s',
        'group_wait': '10s',
        'receiver': 'osprey-dev-alerts-default',
        'repeat_interval': '15m',
        'routes': []  # Empty list to add the routes to
    }
}

# Define the list of routes you want to add to the configuration
routes = [
    {
        'continue': True,
        'matchers': ['slack=osprey-dev-alerts-default'],
        'receiver': 'osprey-dev-alerts-default',
        'repeat_interval': '0s'
    },
    {
        'continue': True,
        'matchers': ['webhook=OSSTIP Webhook'],
        'receiver': 'OSSTIP Webhook',
        'repeat_interval': '20m'
    }
]

# Append each route to the routes section of the config
config['route']['routes'].extend(routes)

# Convert the config dictionary to a YAML string
yaml_data = yaml.dump(config, default_flow_style=False)

# Print the YAML data (or write it to a file)
print(yaml_data)

# Optionally, write the YAML data to a file
with open('config.yaml', 'w') as file:
    yaml.dump(config, file, default_flow_style=False)
