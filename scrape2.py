from bs4 import BeautifulSoup as bsoup
import requests as req
import lxml
import sys


character = int(ord(sys.argv[1]))

website = "http://howstat.com/cricket/Statistics/Players/PlayerList.asp?Group={}".format(chr(character))
webpage = req.get(website)
# soup = bsoup(webpage, "html.parser")
# table = webpage.select("table", { "class" : "TableLined" })
table = bsoup(webpage.text, "lxml")
# print(table.find)
findtbl = table.find("table", { "class" : "TableLined" })

# print(findtbl.text)
# print(len(findtbl))

players = []
for character in findtbl:
	row_data = findtbl.find_all('tr')
	for tr in row_data:
		data = []
		col_data = tr.find_all('td')
		for td in col_data:
			data.append(td.text.strip())
		try:
			players.append(data[0] + " - (" + data[2] + ")" + " - " + data[1])

		except:
			pass			

players = list(dict.fromkeys(players))
# players_count = int(players[len(players)-1].split(" ")[4])
# print(players_count)
# print(players)
# for i in range(2,players_count+2):
# print(players[i]) 
for i in range(2,len(players)):
	print(players[i])



