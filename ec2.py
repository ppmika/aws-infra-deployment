import requests

# Base URL for metadata service
BASE_URL = "http://169.254.169.254/latest/meta-data/"

# Example metadata keys to retrieve
metadata_keys = [
    "instance-id",
    "instance-type",
    "local-ipv4",
    "public-ipv4",
    "availability-zone",
    "ami-id",
]

print("Retrieving EC2 instance metadata:\n")

for key in metadata_keys:
    try:
        response = requests.get(BASE_URL + key, timeout=2)
        response.raise_for_status()
        print(f"{key}: {response.text}")
    except Exception as e:
        print(f"Failed to get {key}: {e}")
