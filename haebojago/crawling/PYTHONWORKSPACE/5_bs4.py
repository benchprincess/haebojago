import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")
# print(soup.title)
# print(soup.title.get_text())
# print(soup.a) #안됨..

# print(soup.find("a", attrs={"class" : "ComponentHead__more--TOglK"}))
# print(soup.find(attrs={"class" : "ComponentHead__more--TOglK"}))

# print(soup.find("li",attrs={"class" : "AsideList__ranking--sNPZy"}))
rank1 = soup.find("li", attrs={"class":"rank01"})
# print(rank1.a.get_text())
# print(rank1.next_sibling)
# rank2 = rank1.next_sibling.next_sibling
# rank3 = rank2.next_sibling.next_sibling
# print(rank3.a.get_text())
# rank2 = rank3.previous_sibling.previous_sibling
# print(rank2.a.get_text())
# print(rank1.parent)
# rank2 = rank1.find_next_sibling("li")
# print(rank2.a.get_text())
# rank3 = rank3.find_next_sibling("li")
# print(rank3.a.get_text())