import requests
from bs4 import BeautifulSoup


def an1getApps(keyword):
	keyword=keyword.replace(' ','+')
	source=requests.get("https://an1.com/?story="+keyword+"&do=search&subaction=search").text
	soup=BeautifulSoup(source,'lxml')
	res=soup.findAll(class_='title')
	apps={}
	for i in res:
		id=i.find('a')['href']
		id=(id.split("/")[-1]).split("-")[0]
		apps[i.find('a').text]=id
	return apps

def an1getApkLink(id):
	source=requests.get("https://an1.com/file_"+str(id)+"-dw.html").text
	soup=BeautifulSoup(source,'lxml')
	res=str(soup.find('script', {'type': 'text/javascript'}))
	link=(res.split("href=")[1]).split(">")[0]
	return link


keyword=input("Enter the Mod apk you want:    ")
apps=an1getApps(keyword)
for no,i in enumerate(apps):
	print(str(no+1)+')',i)
id=list(apps.values())[int(input())-1]
print(an1getApkLink(id))