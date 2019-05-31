########################################################################################################
# 										Author: Sanket Hire											   #
# 						Aim: To scrap the players data in the ODI cricket 			                   #
# 							Source for scraping: http://howstat.com/            					   #
########################################################################################################

import requests as req
from bs4 import BeautifulSoup as bsoup
import lxml
import csv

def cumulify(lis):
    total = 0
    for x in lis:
        total += x
        yield total

#collects data of all cricket players from A to Z (i.e. 65 to 90 in ascii code)
years = []
for j in range(1970, 2020):
	years.append(j)
with open ('ODI_player_scores.csv', "a") as writeFile:
		writer = csv.writer(writeFile)
		writer.writerow(["Player's Name", "Nationality"] + years)


for i in range(65, 91):
	complete_score_data=[]

	website = "http://www.howstat.com/cricket/Statistics/Players/PlayerList.asp?Group=" + chr(i)
	webpage = req.get(website)
	websoup = bsoup(webpage.text, "lxml")
	player_table = websoup.find("table", {"class" : "TableLined"})

	players = []
	a = []
	initials = chr(i)
	for initials in player_table:
		trs = player_table.find_all('tr')
		for tr in trs:
			player_metadata = []
			tds = tr.find_all('td')
			for td in tds:
				links = td.find_all('a')
				for link in links:
					if(link['href'][15:18] == "ODI"):
						a.append(link['href'])
				player_metadata.append(td.text.strip())
			try:
				if(player_metadata[4] != ""):
					players.append(player_metadata[0] + ">" + player_metadata[2])
			except:
				pass

	links = list(dict.fromkeys(a))

	players = list(dict.fromkeys(players))
	players_data = []
	for player in range(0,len(players)):
		players_data.append(players[player].split(">"))


	for link in links:
	
		PlayerID = link.split("=")[1]
		batsite = "http://www.howstat.com/cricket/Statistics/Players/PlayerYears_ODI.asp?PlayerID=" + PlayerID + "#bat"
		
		batpage = req.get(batsite)
		
		batsoup = bsoup(batpage.text, "lxml")
		
		bat_table = batsoup.find("table", { "class" : "TableLined" })	

		batsmen = []
		for new_char in bat_table:
			trs = bat_table.find_all('tr')
			for tr in trs:
				bat_metadata = []
				tds = tr.find_all('td')
				for td in tds:
					bat_metadata.append(td.text.strip())		
				try:
					for index in range(0,12):
						if(bat_metadata[index] == ""):
							bat_metadata[index] = "0"
					batsmen.append(bat_metadata[0] + ">" + bat_metadata[8])

				except:
					pass

					
		batsmen = list(dict.fromkeys(batsmen))
		batsmen_data = []
		for batsman in range(0,len(batsmen)):
			batsmen_data.append(batsmen[batsman].split(">"))

		for intg in range(1,len(batsmen_data)):
			batsmen_data[intg][1] = int(batsmen_data[intg][1])	
			

		batsmen_data_temp = batsmen_data[1:len(batsmen_data)-1]
		li1 = []
		li1=[]
		li0=[]
		for b in range(0,len(batsmen_data_temp)):
			li0.append(int(batsmen_data_temp[b][0]))
			li1.append(batsmen_data_temp[b][1])
		li1 = list(cumulify(li1))	
		li2=[]
		for b in range(0,len(li1)):
			li2.append((li0[b],li1[b]))

		li3=[]
		for b in range(1970,2020):
			li3.append((b,0))

		for bb in range(0,len(li2)):
			index = li2[bb][0] - 1970
			li3[index] = li2[bb]

		yearwise_score = []
		for bb in range(0,len(li3)):
			yearwise_score.append(li3[bb][1])

		complete_score_data.append(yearwise_score)
		# print(i,PlayerID)

	li = []
	try:
		for ii in range(0,len(complete_score_data)):
			li.append(players_data[ii+1] + complete_score_data[ii])
	except:
		pass		


	# print(chr(i) + "is done")

	with open ('ODI_player_scores.csv', "a") as writeFile:
		writer = csv.writer(writeFile)
		for p in range(0,len(li)):
			writer.writerow(li[p])

			
