from urllib.request import urlopen
from bs4 import BeautifulSoup
import urllib.parse


keyword = urllib.parse.quote_plus("삼성전자")
url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query={}".format(keyword)

html = urlopen(url)
bsObj = BeautifulSoup(html, "html.parser")

companyName = bsObj.find("span", {"class":"main_title"}).find("strong")
companyCategory = bsObj.find("div", {"class":"company_info"})\
    .find("ul", {"class":"info_list half_columns"}).findAll("li")[1].find("span",{"class":"txt"})

print(companyName.text)
print(companyCategory.attrs['title'])

