import pymupdf
import bs4
import sec_api

#Design choice: Can either use sec_api which is a free SEC api to get filings
#Or can implement own scrapper using beautifulsoup4 or another library like selenium

SEC_API_KEY="f9b1416399d8b312537c61a49934fd91ab68d8e2bd3c1963a43ef578d413c374"

class Scrapper:
    #Initializes an instance of the class Scrapper
    def __init__(self):
        pass

    #Method that can pull data from the internet such as SEC filings to scrape data from
    def pull_web_data(self):
        pass

    #Parses data-after we get the file we can parse it
    def parse_web_data(self):
        pass


