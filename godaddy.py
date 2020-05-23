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
    pass


def main():
    # Check public ip address
    check_public_ip()

if __name__ == "__main__":
    main()