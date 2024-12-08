import os
import requests
import json

# Define your variables
repo_owner = "ashishshaji"
repo_name = "OneWorkFlowCallsOther"
workflow_id = "second-workflow.yml"  # or the workflow ID
github_token = os.getenv("GITHUB_TOKEN")

# GitHub API endpoint for triggering a workflow
url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/actions/workflows/{workflow_id}/dispatches"

# Headers for authentication and content type
headers = {
    "Authorization": f"token {github_token}",
    "Accept": "application/vnd.github.v3+json"
}

# Payload with the ref (branch) to trigger the workflow
payload = {
    "ref": "main",  # Replace 'main' with your branch
    "inputs": {
        "key1": "value1",
        "key2": "value2"
    }
}

# Make the POST request to trigger the workflow
response = requests.post(url, headers=headers, data=json.dumps(payload))

# Check if the request was successful
if response.status_code == 204:
    print("Workflow triggered successfully.")
else:
    print(f"Failed to trigger workflow: {response.status_code}")
    print(response.text)
