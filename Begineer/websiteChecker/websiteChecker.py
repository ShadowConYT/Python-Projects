import csv
import requests
from fake_useragent import UserAgent
from http import HTTPStatus

def getWebsites(csvfile: str) -> list[str]:
    websites: list[str] = []
    with open(csvfile,'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if 'https://' not in row[1]:
                websites.append(f"https://{row[1]}")
            else:
                websites.append(row[1])
    return websites

print(getWebsites('websites.csv'))

def getUA():
    ua = UserAgent()
    return ua.chrome

def statusDescription(status_code: str) -> str:
    for value in HTTPStatus:
        if value == status_code:
            description: str = f'({value} {value.name}) {value.description}'
            return description
    
    return '(???) Unknown Status Code'

def checkWebsite(website: str, userAgent: str):
    try:
        code: int = requests.get(website, headers={'User-Agent': userAgent}).status_code
        print(website,statusDescription(code))
    except Exception:
        print(f'**could not get information for the website: "{website}"')

def main():
    sites: list[str] = getWebsites('websites.csv')
    user_agent: str = getUA()

    for site in sites:
        checkWebsite(site,user_agent)

if __name__ == '__main__':
    main()


