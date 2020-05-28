#!/usr/bin/env python3
import sys 
import requests
import json
from decouple import config

# Common environment varibles
API_KEY = config('GODADDY_API_KEY')
API_SECRET = config('GODADDY_API_SECRET')
API_URL_BASE = config('API_URL_BASE')

def get_public_ip():
    """Get public IP Address using api.ipify.org"""
    try:
        ip = requests.get('https://api.ipify.org').text
        print(ip)
        return ip
    except requests.ConnectionError as ConnectionError:
        print(ConnectionError)
        return None

def get_domain_info(domain_name):
    """Get info of a specific domain"""
    api_url = API_URL_BASE + '/v1/domains/' + domain_name
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
    api_url = API_URL_BASE + '/v1/domains/' + domain_name + '/records/' + record_type \
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
    """
    Update IP Address of a specific A DNS record
    /v1/domains/{domain}/records/{type}/{name}
    Replace all DNS Records for the specified Domain with the specified Type and Name
    domain_name: string
        Domain name, e.g: practicehabits.net
    record_type: string
        Type of record, e.g: A, CNAME
    record_name: string
        E.g: www, dev
    ip_address: string
    """
    api_url = API_URL_BASE + '/v1/domains/' + domain_name + '/records/' + record_type \
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
    # Checl arguments
    # print("Arguments list: " + str(sys.argv))
    # print("Number of arguments: " + str(len(sys.argv)))
    # for arg in sys.argv:
    #    print(arg)

    if len(sys.argv) != 3:
        print("Usage:\nargv[0] 'domain_name' 'A_DNS_record_name'")
        sys.exit("Check usage syntax for number of arguments.")
    else:
        domain_name = sys.argv[1]
        record_name = sys.argv[2]
        print(domain_name, ':', record_name)

    # Check public ip address
    current_public_ip = get_public_ip()
    
    # Get domain info
    # domain_info = get_domain_info('ipractice.site')
    # domain_info = get_domain_info(domain_name)
    # print(domain_info)

    # Get dns record
    # get_record_info('ipractice.site','A','129')
    record_info = get_record_info(domain_name,'A',record_name)
    if record_info != None:
        print(record_info)
        if record_info != []:
            record_ip_address = record_info[0]['data']
        else:
            record_ip_address = ''
    if current_public_ip != None and record_ip_address != current_public_ip:
        update_record_info(domain_name,'A',record_name, current_public_ip)

if __name__ == "__main__":
    main()
