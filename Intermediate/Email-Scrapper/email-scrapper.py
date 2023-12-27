import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from typing import Final

Email_regex: Final[str] = r"""(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[
\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[
a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[
0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[
\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"""
class Browser:
    def __init__(self,driver):
        print('Booting Up Browser....')
        self.chrome_options = Options()
        self.chrome_options.add_argument('--headless')

        self.service = Service(driver)
        self.browser = webdriver.Chrome(service=self.service, options=self.chrome_options)

    def scrape_emails(self, url: str) -> set:
        print(f'Scraping : {url} for Emails....')
        self.browser.get(url) # Loading the URL in the Browser
        page_source: str = self.browser.page_source

        re_mails: set = set()
        for regex_match in re.finditer(Email_regex, page_source):
            re_mails.add(regex_match.group())

        return re_mails

    def close_browser(self):
        print('Closing Browser....')
        self.browser.close()

def main():
    driver: str = 'chromedriver.exe'
    browser: str = Browser(driver)

    #user_input: str = input("Enter Your URL: ")

    emails: list = browser.scrape_emails(url = 'https://www.randomlists.com/email-addresses?qty=100')
    print(emails)

    for i, email in enumerate(emails, start=1):
        print(i, email, sep=': ')

if __name__ == '__main__':
    main()