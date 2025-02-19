import requests
import json

POSTHOG_PERSONAL_API_KEY = 'phx_GpQl8sn7vFzHwdwUp5ca69CCPEzqy3gVCkiNWONhS5BDxLv'

if __name__ == "__main__":
    headers = {
        'Content-Type': 'application/json',
        "Authorization": f"Bearer {POSTHOG_PERSONAL_API_KEY}"
    }

    project_id = 1
    url = f"http://localhost:8010/api/projects/{project_id}/query/"

    for i in range(20):
        payload = {
            "query": {
                "kind": "HogQLQuery",
                "query": f"select properties.$current_url from events where timestamp > NOW() and properties.$current_url like '%/blog%' limit {i}"
            }
        }

        response = requests.post(url, headers=headers, data=json.dumps(payload))
        print(response.json())