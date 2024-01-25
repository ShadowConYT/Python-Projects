import requests
from bs4 import BeautifulSoup

def get_soup():
    headers = {
        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 OPR/106.0.0.0"
    }
    request = requests.get("https://www.nytimes.com/", headers=headers)
    data = request.text

    soup = BeautifulSoup(data, "html.parser")
    return soup

def get_headlines(soup):
    headlines = set()

    for head in soup.findAll('p', class_ = "indicate-hover"):
        headline = head.contents[0]
        headlines.add(headline)
    
    return headlines

def check_headlines(headlines, term):

    found_terms = []

    for headline in headlines:
        if term in headline:
            found_terms.append(headline)
    
    print(f"Number of headlines: {len(headlines)}")
    print(f"Number of headlines with {term}: {sum(1 for headline in headlines if term in headline)}")

    return found_terms


def main():
    soup = get_soup()
    headlines = get_headlines(soup)
    check = check_headlines(headlines, "Trump")

    for i, line in enumerate(check,start=1):
        print(f"{i}. {line}")

if __name__ == "__main__":
    main()