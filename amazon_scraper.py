import requests
from selectorlib import Extractor 

class AmazonScraper:
    
    def __init__(self, extractor_file):
        self.extractor = Extractor.from_yaml_file(extractor_file)
    
    def scrape(self, url, headers):    
        r = requests.get(url, headers=headers)
        if r.status_code >= 500:
            return None
        return self.extractor.extract(r.text)