import requests
import json
import time

#Upload New Layer Version

url = "https://4lhz7nq5cn3ojggwtfqa2g6q2a0psxso.lambda-url.us-east-1.on.aws/UploadNewLayerVersion"

payload = json.dumps({
  "layer": {
    "name": "messageLibraryLayer",
    "description": "",
    "compatible_runtimes": [
      "python3.9"
    ],
    "license_info": "",
    "compatible_architectures": [
      "x86_64"
    ]
  },
  "zip_location": {
    "type": "S3",
    "S3Bucket": "lambdalayersbuildbucket",
    "S3Key": "messageLibrary.zip"
  }
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

#Wait 10s for next request 

time.sleep(10)


#Update Function to Latest Version

url = "https://4lhz7nq5cn3ojggwtfqa2g6q2a0psxso.lambda-url.us-east-1.on.aws/UpdateFunctionToLatestVersion"

payload = json.dumps({
  "function": {
    "name": "lambdafunctions"
  },
  "layer": {
    "name": "messageLibraryLayer",
    "description": "",
    "compatible_runtimes": [
      "python3.9"
    ],
    "license_info": "",
    "compatible_architectures": [
      "x86_64"
    ]
  }
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
