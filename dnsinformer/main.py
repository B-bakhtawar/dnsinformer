import argparse
import requests
import whois
from datetime import datetime
import dns.resolver

def bold_text(text):
    return f"\033[1m{text}\033[0m"

def get_subdomains(domain):
    subdomains = []
    try:
        result = dns.resolver.resolve(domain, 'NS')
        for val in result:
            subdomains.append(val.to_text())
    except Exception as e:
        print(f"Error fetching subdomains: {e}")
    return subdomains

def get_ip_address(domain):
    ip_addresses = []
    try:
        result = dns.resolver.resolve(domain, 'A')
        for val in result:
            ip_addresses.append(val.to_text())
    except Exception as e:
        print(f"Error fetching IP addresses: {e}")
    return ip_addresses

def get_server_details(domain):
    server_details = {}
    try:
        response = requests.get(f"http://{domain}")
        server_details['server'] = response.headers.get('Server', 'N/A')
    except Exception as e:
        print(f"Error fetching server details: {e}")
    return server_details

def get_whois_info(domain):
    whois_info = {}
    try:
        w = whois.whois(domain)
        whois_info['creation_date'] = w.creation_date
        whois_info['expiration_date'] = w.expiration_date
        whois_info['updated_date'] = w.updated_date
    except Exception as e:
        print(f"Error fetching WHOIS information: {e}")
    return whois_info

def print_dns_info(domain):
    print(bold_text("IP Addresses:"))
    ip_addresses = get_ip_address(domain)
    for ip in ip_addresses:
        print(ip)

    print(bold_text("\nSubdomains:"))
    subdomains = get_subdomains(domain)
    for sub in subdomains:
        print(sub)

    print(bold_text("\nServer Details:"))
    server_details = get_server_details(domain)
    for key, value in server_details.items():
        print(f"{key.capitalize()}: {value}")

    print(bold_text("\nWHOIS Information:"))
    whois_info = get_whois_info(domain)
    for key, value in whois_info.items():
        if isinstance(value, list):
            value = ', '.join([str(v) for v in value])
        print(f"{key.replace('_', ' ').capitalize()}: {value}")

def main():
    parser = argparse.ArgumentParser(description='Fetch DNS information for a domain.')
    parser.add_argument('domain', type=str, help='Domain name to fetch information for')
    args = parser.parse_args()

    print_dns_info(args.domain)
