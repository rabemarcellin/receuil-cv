import requests
from schemas.user import User

def create_profile_service(profile: User):
    url = "https://x8ki-letl-twmt.n7.xano.io/api:9uKtYW-B/profiles"
    response = requests.post(url, json=profile.parse())
    if response.status_code == 200:
        return response.reason
    else:
        print(response.reason)
        return None
