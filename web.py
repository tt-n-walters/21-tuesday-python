import requests

url = "http://nicowalters.techtalents.club/page2.html"

response = requests.get(url)

html = response.text
html.count("<img")
img_location = html.find("<img", 600)
quote_location = html.find("\"", img_location + 10)

img_link = html[img_location+10:quote_location]


print(html[480:570])
print(html[496:545])
print(img_link)
