import requests
from bs4 import BeautifulSoup

web=requests.get("https://www.yelp.com/search?find_desc=Restaurants&find_loc=%C4%B0slambey%2C+Istanbul%2C+Turkey")


# print(web)

soup=BeautifulSoup(web.text,"html.parser")

# print(soup)

boxes=soup.find_all("a",class_="y-css-12ly5yx")

print(len(boxes))

# name=soup.find_all("a")
# # print(name)

# for a_tag in name:
#     title = a_tag.get("title")
#     if title:
#         print(title)



# prices=soup.find_all("p",class_="price_color")
# # print(price)

# for price in prices:
#     print(price.text)