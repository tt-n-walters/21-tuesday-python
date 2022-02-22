import requests
from bs4 import BeautifulSoup

url = "http://nicowalters.techtalents.club/page2.html"
response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, features="html.parser")

# Direct tag access
img_link = soup.img["src"]

# Tag searching
names = []
spans = soup.find_all("span", class_="profile-name")
for span in spans:
    names.append(span.text)


imgs = []
imgs_html = soup.find_all("img")
for img in imgs_html:
    imgs.append(img["src"])

print(names)
print(imgs)
