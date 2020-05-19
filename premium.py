import requests
from bs4 import BeautifulSoup

def getApps(search):	
	search=search.replace(" ","+")
	source=requests.get("https://dlandroid.com/?s="+search).text
	soup=BeautifulSoup(source,'lxml')
	res=soup.findAll(class_='onvan')
	app={}
	for i in res:
		app[i.text]="https://dl-android.com/p/index.php?id="+(i['href']).split('/')[-2]
	return app

def apklink(link):
	source=requests.get(link).text
	soup = BeautifulSoup(source,'lxml')
	res=soup.find(class_='dlbtng')
	apps={}
	for i in res.findAll("a"):
		apps[i.text]=i["href"]
	return apps

keyword=input("Enter the Mod apk you want:    ")
apps=getApps(keyword)
for no,i in enumerate(apps):
	print(str(no+1)+')',i)
id=list(apps.values())[int(input())-1]
print(apklink(id))