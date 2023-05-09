import bs4
import requests
from bs4 import BeautifulSoup

def main():
    url = "https://funkeys.co.kr/shop/list.php?ca_id=10"
    response = requests.get(url)
    if response.status_code == 200:
        soup = bs4.BeautifulSoup(response.text, "html.parser")
        proudctList = soup.select(".item-list")
        for item in proudctList:
            title = item.select_one(".title").text.strip()  # strip - 공백 제거
            sale = item.select_one(".dcView").text.strip()
            # print(title.strip())
            switchoption = item.select(".switchop")
            for option in switchoption:
                switch = option.select_one(".optTitle").text
                price = option.select_one(".pull-right").text
                print('[' + sale + ']', title, '(' + switch + ')', price)

if __name__ == '__main__':
    main()
