import requests

# Step 1: Get IMDSv2 token
try:
    token_response = requests.put(
        "http://169.254.169.254/latest/api/token",
        headers={"X-aws-ec2-metadata-token-ttl-seconds": "21600"},
        timeout=2
    )
    token = token_response.text.strip()
except Exception as e:
    print("Failed to get token:", e)
    token = None

# Step 2: Use token to fetch metadata
fields = ["instance-id", "instance-type", "local-ipv4", "ami-id"]
metadata_url = "http://169.254.169.254/latest/meta-data/"

for field in fields:
    try:
        headers = {"X-aws-ec2-metadata-token": token} if token else {}
        res = requests.get(metadata_url + field, headers=headers, timeout=2)
        print(f"{field}: {res.text}")
    except Exception as e:
        print(f"{field}: ERROR ->", e)