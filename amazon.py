import requests
from bs4 import BeautifulSoup
import lxml


class AmazonPrice:
    def __init__(self):
        self.header = {
            "User-Agent": "YOUR USER AGENT",
            "Accept-Language": "YOUR ACCEPT LANGUAGE"
        }
        self.url = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
        self.response = requests.get(url=self.url,headers=self.header)
        self.data = self.response.text

    def show_data(self):
        soup = BeautifulSoup(self.data,"lxml")
        price = soup.find('span',class_="a-offscreen")
        price_value = price.getText()
        return price_value