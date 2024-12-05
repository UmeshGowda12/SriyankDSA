import yaml

data = [
    {
        'reciever_id': 2, 
        'repreat_interval': '0s', 
        'receiver_type': 'slack', 
        'destinations': ['uk-south-staging', 'all-prod'], 
        'metadata': {
            'name': 'test-dev-alerts-default', 
            'slack_configs': [{
                'api_url': '$NURL_DEFAULT_SLACK_CHANNEL', 
                'channel': '#0sprey-alerts', 
                'send_resolved': True, 
                'text': '{{ range .Alerts }} *Alert:* {{ .Annotations.title }}{{ if .Labels.severity }} - `{{ .Labels.severity }}`{{ end }} *Summary:* {{ .Annotations.summary }} *Description:* {{ .Annotations.description }} *Details:*\n  {{ range .Labels.SortedPairs }} • *{{ .Name }}:* `{{ .Value }}`\n  {{ end }}\n{{ end }}',
                'title': '[{{ .Status | toUpper }}{{ if eq .Status "firing" }}:{{ .Alerts.Firing | len }}{{ end }}] {{ .CommonLabels.alertname }}'
            }]
        }
    },
    {
        'reciever_id': 1, 
        'repreat_interval': '20m', 
        'receiver_type': 'webhook', 
        'destinations': ['uk-south-staging'], 
        'metadata': {
            'name': 'OSSTIP Webhook', 
            'webhook_configs': [{
                'url': '$NURL_OSSTIP_WEBHOOK_URL', 
                'http_config': {'basic_auth': {'passwrd': 'Test', 'username': 'apikey'}}, 
                'send_resolved': True, 
                'extensions': {
                    'headers': [
                        {'name': 'Authorization', 'value': 'REDACTED'}, 
                        {'name': 'TIP-Instance', 'value': 'staging'}, 
                        {'name': 'X-Account-Id', 'value': '2c4a1985f9d5c10bd4842d2d3Test989088e'}, 
                        {'name': 'Alert-CName', 'value': 'staging'}
                    ]
                }
            }]
        }
    }
]

# Create a list of objects with the required properties
receiver_info_list = []

for receiver in data:
    receiver_info = {
        'receiver_type': receiver['receiver_type'],
        'repeat_interval': receiver['repreat_interval'],
        'metadata_name': receiver['metadata'].get('name', 'No name available')
    }
    receiver_info_list.append(receiver_info)



##############################

    # Load the existing YAML file (global_config.yml)
with open('global_config.yml', 'r') as file:
    yaml_data = yaml.safe_load(file)

# Check if 'routes' key exists and is a list; otherwise, initialize it as an empty list
if 'routes' not in yaml_data['route']:
    yaml_data['route']['routes'] = []

# Populate the routes section with the information from the list
for receiver in receiver_info_list:
    route = {
        'continue': True,
        'matchers': [f"{receiver['receiver_type']}={receiver['metadata_name']}"],
        'receiver': receiver['metadata_name'],
        'repeat_interval': receiver['repeat_interval']
    }
    yaml_data['route']['routes'].append(route)

# Write the updated data back to the same YAML file
with open('global_config.yml', 'w') as file:
    yaml.dump(yaml_data, file, default_flow_style=False, sort_keys=False)

print("YAML file 'global_config.yml' updated successfully.")

# Output the list of objects
print(receiver_info_list)
