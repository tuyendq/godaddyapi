import requests
import json
from decouple import config

def check_public_ip():
    try:
        ip = requests.get('https://api.ipify.org').text
        print(ip)
        return ip
    except requests.ConnectionError as ConnectionError:
        print(ConnectionError)
        return None

def get_domain_info(domain_name):
    """Get info of a specific domain"""
    API_KEY = config('GODADDY_API_KEY')
    API_SECRET = config('GODADDY_API_SECRET')
    API_URL = config('API_URL')

    api_url = API_URL + '/v1/domains/' + domain_name
    headers = {'Content-Type': 'application/json',
                'Authorization': 'sso-key ' + API_KEY + ':' + API_SECRET}
    try:
        response = requests.get(api_url, headers=headers)
        print(response.status_code)
        if response.status_code == 200:
            print(json.loads(response.content.decode('utf-8')))
            return json.loads(response.content.decode('utf-8'))
        else:
            print("Check your code, cannot get list of domain")
            return None
    except requests.ConnectionError as ConnectionError:
        print(ConnectionError)
        return None

def main():
    # Check public ip address
    check_public_ip()
    # Get domain info
    get_domain_info('ipractice.site')

if __name__ == "__main__":
    main()