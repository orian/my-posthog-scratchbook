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

    payload = {
      "kind": "DataTableNode",
      "source": {
        "kind": "ErrorTrackingQuery",
        "orderBy": "occurrences",
        "status": "all",
        "dateRange": {
          "date_from": "-7d",
          "date_to": None
        },
        "assignee": None,
        "customVolume": {
          "value": 168,
          "interval": "hour"
        },
        "filterGroup": {
          "type": "AND",
          "values": [
            {
              "type": "AND",
              "values": []
            }
          ]
        },
        "filterTestAccounts": False,
        "searchQuery": "",
        "limit": 50
      },
      "showActions": False,
      "showTimings": False,
      "columns": [
        "error",
        "volume",
        "occurrences",
        "sessions",
        "users",
        "assignee"
      ]
    }
    enc_payload = '{"query":{"kind":"ErrorTrackingQuery","orderBy":"occurrences","status":"all","dateRange":{"date_from":"-1d","date_to":null},"assignee":null,"customVolume":{"value":168,"interval":"hour"},"filterGroup":{"type":"AND","values":[{"type":"AND","values":[]}]},"filterTestAccounts":false,"searchQuery":"","limit":50,"modifiers":{"debug":true}},"client_query_id":"f593ee13-95a4-41e5-9f31-382418828deb","refresh":"force_sync"}'
    enc_payload = json.dumps(payload)

    for i in range(1):
        payload_ = {
            "query": {
                "kind": "HogQLQuery",
                "query": f"select properties.$current_url from events where timestamp > NOW() and properties.$current_url like '%/blog%' limit {i}"
            }
        }

        response = requests.post(url, headers=headers, data=enc_payload)
        if response.status_code != 200:
            raise Exception(f"wrong: {response.status_code} - {response.text}")

        print(response.json())