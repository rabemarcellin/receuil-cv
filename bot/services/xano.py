import requests
import json

def create_profile_service(profile):
    url = "https://x8ki-letl-twmt.n7.xano.io/api:9uKtYW-B/profiles"
    response = requests.post(url, json=profile.parse())
    if response.status_code == 200:
        return response.reason
    else:
        print(response.reason)
        return None

def get_cv_content(cv_url: str):
    url = "https://x8ki-letl-twmt.n7.xano.io/api:9uKtYW-B/cv_content_extractor"
    params = {"cv_url": cv_url}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        data = json.load(data)
        print(data)
        cv_content = data.get("response", {}).get("result", {}).get("formatedText")
        print("cv content", cv_content)
        return cv_content
                    
