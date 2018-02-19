from urllib.request import urlopen
from bs4 import BeautifulSoup
import json

code = "005930"
url = "http://companyinfo.stock.naver.com/v1/company/cF3002.aspx?cmp_cd={}&frq=0&rpt=0&finGubun=MAIN&frqTyp=0&cn=".format(code)
html = urlopen(url)
bsObj = BeautifulSoup(html, "html.parser")

#string to json object
jsonObject = json.loads(str(bsObj))
data = jsonObject['DATA']

for item in data:
    result = "{},{},{},{},{},{}".format(item['ACC_NM'], item['DATA1'], item['DATA2'], item['DATA3'], item['DATA4'], item['DATA5'])
    print(result)

