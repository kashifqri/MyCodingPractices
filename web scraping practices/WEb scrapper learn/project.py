import requests
from bs4 import BeautifulSoup


web=requests.get("https://shuttertop.com/")
print(web)

print(web.content)

print(web.url)

print(web.status_code)

soup=BeautifulSoup(web.content,"html.parser")

print(soup.prettify())

print(soup.title)

print(soup.title.name)

print(soup.a)

print(soup.p)

print(soup.h1)



tag=soup.html
print(tag)

type(tag)
print(tag)


tag=soup.p
print(tag)


tag=soup.a
print(tag)


tag=soup.h1
print(tag)



tag=soup.p.string
print(tag)


tag=soup.a.string
print(tag)


tag=soup.h1.string
print(tag)

tag=soup.find("p")
print(tag)

tag=soup.find_all("p")
print(tag)

com=soup.p.string

print(com)

com=soup.h1.string

print(com)

class_data=soup.find("div",class_="site-branding has-site-logo")

print(class_data)



id_data=soup.find("div",id="page")

print(id)

p_tag=id_data.find_all("p")

print(p_tag)

line=soup.find_all("p")

print(line)

for l in line:
    print(l.text)


s=soup.find("div",class_="col-lg-10 com-md-12")

print(s)


line_1=s.find_all("p")

print(line_1)

for l_1 in line_1:
    print(l_1.text)


img=soup.find_all("img")
print(img)


for i in img:
    print(i.get("src"))
