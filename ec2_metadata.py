import requests

metadata_url = "http://169.254.169.254/latest/meta-data/"
fields = ["i-0d45b3b5bcb1beedf", "t3.micro", "18.208.165.243", "ami-000d41719f4ab3d23"]

for field in fields:
    res = requests.get(metadata_url + field)
    print(f"{field}: {res.text}")