import requests

#发送GET请求
response = requests.get("https://www.zhihu.com/")
#获取网页内容
html_content = response.text.encode(response.encoding).decode()
#打印网页内容
print(html_content)

#使用beautifulsoup来解析网页内容
from bs4 import BeautifulSoup

#使用Beautifulsoup解析html
soup = BeautifulSoup(html_content,'')