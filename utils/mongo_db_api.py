import requests
import json
url = "https://us-east-2.aws.data.mongodb-api.com/app/data-cfefrbf/endpoint/data/v1/action/findOne"

payload = json.dumps({
    "collection": "users",
    "database": "qmldb_dev",
    "dataSource": "QuoteMyLife",
    "projection": {
        "_id": 1,
        "test": "test"
    }
})
headers = {
  'Content-Type': 'application/json',
  'Access-Control-Request-Headers': '*',
  'api-key': '8P2aj4MMZ5vQXl6mVz7zXyfV8zXm4de8ky1JJP54pzvtGI1erdLo1FOEP0ddMvH4',
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
