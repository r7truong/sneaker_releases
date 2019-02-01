import bs4
from urllib.request import urlopen
import datetime


MY_URL = "https://www.kixify.com/release-dates/upcoming"
DESIRED_SNEAKERS = ["air jordan 3", "air jordan 11", "bape", "yeezy", "element", "supreme"]

# Grabbing the desired webpage
webpage = urlopen(MY_URL)
page_html = webpage.read()
webpage.close()
webpage_soup = bs4.BeautifulSoup(page_html, "html.parser")


# Grabbing the container with the sneaker names and release dates
sneaker_divs = webpage_soup.find_all("div", {"class": "col-xs-6 col-sm-3 col-md-3 release-date-item-continer clear-padding"})


def main():
    releases = ""
    for sneaker_div in sneaker_divs:
        release_date_container = sneaker_div.div.div.div.text
        year = datetime.datetime.now().year
        month = release_date_container.lstrip("0123456789")
        day = release_date_container[:len(month)].lower().rstrip("qwertyuiopasdfghjklzxcvbnm")

        release_date = f"{year}-{month}-{day}"
        name = sneaker_div.find_all("div", {"class": "release-date-title"})[0].a.string
        name_searchable = name.lower()
        if any(sneaker_keywords in name_searchable for sneaker_keywords in DESIRED_SNEAKERS):
            releases += f"{name} is releasing on {release_date}\n\n"
    return releases
