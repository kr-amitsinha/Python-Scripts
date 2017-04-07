#A simple scripts which notifies you of the live scores from espncricinfo. 
#Made By: Kumar Amit Sinha
#	  Shiv Nadar University

import requests
from bs4 import BeautifulSoup
from time import sleep
import notify2

print (chr(27) + "[2J")
notify2.init('Live Scorecard:')
url = 'http://static.cricinfo.com/rss/livescores.xml'
req = requests.get(url)

soup = BeautifulSoup(req.content,'lxml')
print (soup.prettify)

for data in soup.find_all('title'):
	print (data.text)
	break

for data in soup.find_all('pubdate'):
	print(data.text + '\n')

index = 0
for data in soup.find_all('description'):
	if(index!=0):
		print ('(' + str(index) + ') ' + data.text)
	index += 1

match_num = int(input("\nEnter the match you want to follow closely:"))


i = 1
for link in soup.find_all('guid'):
	if(i == match_num):
		url = link.text
		break
	i += 1
#print (url)
while True:
	req = requests.get(url)
	soup = BeautifulSoup(req.content,'lxml')
	display = soup.find_all('title')
	position = display[0].text.find('|')
	score = display[0].text[0:position]
	string = str(score) + "\nVisit: " + url
	n = notify2.Notification('Live Scorecard', string)
	n.show()
	#print (url)
	sleep(45)
