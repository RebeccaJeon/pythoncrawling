from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "http://companyinfo.stock.naver.com/v1/company/cF3002.aspx?cmp_cd=068270&frq=0&rpt=0&finGubun=MAIN&frqTyp=0&cn="
html = urlopen(url)
bsObj = BeautifulSoup(html, "html.parser")

print(bsObj)
