import requests
import json
from decouple import config

# Common environment varibles
API_KEY = config('GODADDY_API_KEY')
API_SECRET = config('GODADDY_API_SECRET')
API_URL = config('API_URL')

def check_public_ip():
    """Check public IP Address using api.ipify.org"""
    try:
        ip = requests.get('https://api.ipify.org').text
        print(ip)
        return ip
    except requests.ConnectionError as ConnectionError:
        print(ConnectionError)
        return None

def get_domain_info(domain_name):
    """Get info of a specific domain"""
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

def get_record_info(domain_name, record_type, record_name):
    """Retrieve DNS Records for the specified Domain, 
    optionally with the specified Type and/or Name
    url: /v1/domains/{domain}/records/{type}/{name}
    """
    api_url = API_URL + '/v1/domains/' + domain_name + '/records/' + record_type \
                        + '/' + record_name
    headers = {'Content-Type': 'application/json',
                'Authorization': 'sso-key ' + API_KEY + ':' + API_SECRET}
    try:
        response = requests.get(api_url, headers=headers)
        print(response.status_code)
        if response.status_code == 200:
            print(json.loads(response.content.decode('utf-8')))
            return json.loads(response.content.decode('utf-8'))
        else:
            print("Check your code, cannot get dns record")
            return None
    except requests.ConnectionError as ConnectionError:
        print(ConnectionError)
        return None

def update_record_info(domain_name, record_type, record_name, ip_address):
    """Update IP Address of a specific A DNS record
    /v1/domains/{domain}/records/{type}/{name}
    Replace all DNS Records for the specified Domain with the specified Type and Name
    """
    api_url = API_URL + '/v1/domains/' + domain_name + '/records/' + record_type \
                        + '/' + record_name
    headers = {'Content-Type': 'application/json',
                'Authorization': 'sso-key ' + API_KEY + ':' + API_SECRET}
    data = [{'data': ip_address, 'ttl': 1800}]
    try:
        response = requests.put(api_url, headers=headers, json=data)
        print("Response status code: " + str(response.status_code))
        if response.status_code == 200:
            # print(json.loads(response.content.decode('utf-8')))
            print(type(response))
            return response
        else:
            print("Check your code, cannot update ip address of dns record")
            return None
    except requests.ConnectionError as ConnectionError:
        print(ConnectionError)
        return None

def main():
    # Check public ip address
    current_public_ip = check_public_ip()
    # Get domain info
    # get_domain_info('ipractice.site')
    # Get dns record
    get_record_info('ipractice.site','A','129')
    if current_public_ip != None:
        update_record_info('ipractice.site','A','129', current_public_ip)

if __name__ == "__main__":
    main()