import requests as req
from bs4 import BeautifulSoup as soup
import lxml
import csv

for i in range(65, 91):
	website = "http://www.howstat.com/cricket/Statistics/Players/PlayerList.asp?Group=" + chr(i)
	webpage = req.get(website)
	websoup = soup(webpage.text, "lxml")
	player_table = websoup.find("table", {"class" : "TableLined"})

	players = []
	initials = chr(i)
	for initials in player_table:
		trs = player_table.find_all('tr')
		for tr in trs:
			player_metadata = []
			tds = tr.find_all('td')
			for td in tds:
				player_metadata.append(td.text.strip())
			try:
				if(player_metadata[4] != ""):
					if(player_metadata[3] == ""):
						player_metadata[3] = "0"
					if(player_metadata[5] == ""):
						player_metadata[5] = "0"	
					players.append(player_metadata[0] + ">" + player_metadata[1] + ">" + player_metadata[2] + ">" + player_metadata[3] + ">" + player_metadata[4] + ">" + player_metadata[5])
			except:
				pass

	players = list(dict.fromkeys(players))
	players_data = []
	for player in range(0,len(players)):
		players_data.append(players[player].split(">"))

	with open ('ODI_players/' + chr(i) +  '_players.csv', "w") as writeFile:
		writer = csv.writer(writeFile)
		for p in range(0,len(players_data)):
			writer.writerow(players_data[p])
	writeFile.close()	

	print("Players with initials " + chr(i) + " are written successfully!")	

