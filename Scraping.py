# coding: utf-8

import requests #httpリクエストを実行
import bs4 #BeutifulSoupをインポート
import re #正規表現を利用
from datetime import *

url_apachehttpd = 'https://httpd.apache.org/'
url_apachetomcat = 'http://tomcat.apache.org/'
url_openssl = "https://www.openssl.org/"


def getsoup(url):
	res = requests.get(url) #Apacheサイト
	#print(res.status_code) #ステータスコードを表示
	try:
		res.raise_for_status() #20x系以外の場合例外を起こす
	except requests.exceptions.HTTPError:
		html = """<html><head><title>Error</title></head></html>"""
		#soup = bs4.BeautifulSoup(html,'html.parser')
		soup = bs4.BeautifulSoup(html,'lxml')
	else:
		soup = bs4.BeautifulSoup(res.text,'lxml')
	finally:
		return soup


def apachehttpd_scraping():
	soup = getsoup(url_apachehttpd)
	elems = soup.select('h1') #タグすべてをリストに取得
	#バージョン取得
	list = []
	for elem in elems:
		text = elem.getText()
		if text.find("Released") == -1:
			pass
		elif text.find("End") != -1:
			pass
		else:
			retext = re.findall('[0-9]{1,}\.[0-9]{1,}\.[0-9]{1,}' , text)
			#print(retext[0])#バージョン
			strRawdate = elem.select('span')[0].getText()
			dateDatetime = datetime.strptime(strRawdate, '%Y-%m-%d')
			dateDate = date(dateDatetime.year, dateDatetime.month, dateDatetime.day)
			#print(dateDate)#リリース日
			list.append([retext[0],dateDate])
			
	return list


def apachetomcat_scraping():
	soup = getsoup(url_apachetomcat)
	elems = soup.select('h3') #タグすべてをリストに取得
	
	list = []
	for elem in elems:
		text = elem.get("id")
		pattern = "Tomcat_[0-9]{1}"
		
		if re.match(pattern , text) != None:
			retext = re.findall('[0-9]{1,}\.[0-9]{1,}\.[0-9]{1,}' , text)
			#print(retext[0])#バージョン
			strRawdate = elem.select("span")[0].getText()
			dateDatetime = datetime.strptime(strRawdate, '%Y-%m-%d')
			dateDate = date(dateDatetime.year, dateDatetime.month, dateDatetime.day)
			#print(dateDatetime)#リリース日
			list.append([retext[0],dateDate])
			
	return list


def openssl_scraping():
	soup = getsoup(url_openssl)
	table = soup.findAll("table",{"class":"newsflash"})
	rows = table[0].findAll("tr")
	list = []
	for row in rows:
		text = row.select("td.t")[0].getText()
		pattern = "OpenSSL [0-9]{1,}\.[0-9]{1,}\.[0-9]{1,}[a-z] is now available"
		
		if re.match(pattern , text) != None:
			strRawdate = row.select("td.d")[0].getText()
			dateDatetime = datetime.strptime(strRawdate, '%d-%b-%Y')
			dateDate = date(dateDatetime.year, dateDatetime.month, dateDatetime.day)
			#print(dateDate)#リリース日
			retext = re.findall('[0-9]{1,}\.[0-9]{1,}\.[0-9]{1,}[a-z]' , row.select("td.t")[0].getText())#リリース日
			#print(retext[0])#バージョン
			list.append([retext[0], dateDate])
			
	return list


if __name__ == '__main__':
    print(apachehttpd_scraping())
    print(apachetomcat_scraping())
    print(openssl_scraping())


