from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep

class Browser:
    def __init__(self):
        print('Browser Booting Up....')
        self.browser = webdriver.Chrome()
    
    def open_browser(self,url: str):
        print(f'Opening {url}')
        self.browser.get(url)
        print('Done!')
    
    # Selenium Automatically Closes Browser so No need for Writing a script to close the Browser


if __name__ == '__main__':
    browser = Browser()
    browser.open_browser('https://google.com')
    sleep(10)