import requests
from bs4 import BeautifulSoup


def getApps(keyword,mode=1):
	if mode==1:
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
	else:
		keyword=keyword.replace(" ","+")
		source=requests.get("https://dlandroid.com/?s="+keyword).text
		soup=BeautifulSoup(source,'lxml')
		res=soup.findAll(class_='onvan')
		app={}
		for i in res:
			app[i.text]="https://dl-android.com/p/index.php?id="+(i['href']).split('/')[-2]
		return app

def apklink(id,mode=1):
	if (mode==1):
		source=requests.get("https://an1.com/file_"+str(id)+"-dw.html").text
		soup=BeautifulSoup(source,'lxml')
		res=str(soup.find('script', {'type': 'text/javascript'}))
		link=(res.split("href=")[1]).split(">")[0]
		return {"Download":link}
	else:
		source=requests.get(id).text
		soup = BeautifulSoup(source,'lxml')
		res=soup.find(class_='dlbtng')
		apps={}
		for i in res.findAll("a"):
			apps[i.text]=i["href"]
		return apps
  
mode=int(input("1) Games\n2) Apps\n enter:    "))
keyword=input("Enter the Mod apk you want:    ")
apps=getApps(keyword,mode)
for no,i in enumerate(apps):
	print(str(no+1)+')',i)
id=list(apps.values())[int(input())-1]
print(apklink(id,mode))
