import requests
import base64

def get_challenge_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        # Decode the Base64 content
        encoded_content = response.json()[0][0]  # Assuming the content is in the first element of the first list
        decoded_content = base64.b64decode(encoded_content).decode('utf-8')
        return decoded_content
    else:
        print(f"Failed to fetch content from {url}. Status code: {response.status_code}")
        return None

# Replace the URL below with the actual challenge URL
challenge_url = "https://0ijq1i6sp1.execute-api.us-east-1.amazonaws.com/dev/start?q=select%20contents%20from%20readme"

content = get_challenge_content(challenge_url)
if content:
    print(content)
