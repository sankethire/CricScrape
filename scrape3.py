from bs4 import BeautifulSoup as bsoup
import requests as req
import lxml
import sys
import csv


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
col_data = []
a = []
for character in findtbl:
	row_data = findtbl.find_all('tr')
	for tr in row_data:
		data = []
		col_data = tr.find_all('td')
		for td in col_data:
			links = td.find_all('a')
			for link in links:
				if(link['href'][15:18] == "ODI"):
					a.append(link['href'])
			data.append(td.text.strip())
		try:
			if(data[4] != ""):
				players.append(data[0] + " - (" + data[2] + ")" + " - " + data[1])
		except:
			pass			

links = list(dict.fromkeys(a))
for p in links:
	print(p)
players = list(dict.fromkeys(players))
# print(len(a), len(players))
# players_count = int(players[len(players)-1].split(" ")[4])
# print(players_count)
# print(players)
for i in range(1,len(players)):
	print(players[i]) 

new_char = chr(81)
gamer1 = 1
gamer2 = 1
for link in links:
	
	print(link.split("=")[1])
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
				# batsmen.append(bat_metadata[0] + ">" + bat_metadata[1] + ">" + bat_metadata[2] + ">" + bat_metadata[3] + ">" + bat_metadata[4] + ">" + bat_metadata[5] + ">" + bat_metadata[6] + ">" + bat_metadata[7] + ">" + bat_metadata[8] + ">" + bat_metadata[9] + ">" + bat_metadata[10] + ">" + bat_metadata[11] + ">" + bat_metadata[12] + ">" + bat_metadata[13])				
			try:
				# print(bat_metadata[0] + ">" + bat_metadata[1] + ">" + bat_metadata[2] + ">" + bat_metadata[3] + ">" + bat_metadata[4] + ">" + bat_metadata[5] + ">" + bat_metadata[6] + ">" + bat_metadata[7] + ">" + bat_metadata[8] + ">" + bat_metadata[9] + ">" + bat_metadata[10] + ">" + bat_metadata[11] + ">" + bat_metadata[12] + ">" + bat_metadata[13])				
				for index in range(0,12):
					if(bat_metadata[index] == ""):
						bat_metadata[index] = "0"
				# print(bat_metadata[0] + ">" + bat_metadata[1] + ">" + bat_metadata[2] + ">" + bat_metadata[3] + ">" + bat_metadata[4] + ">" + bat_metadata[5] + ">" + bat_metadata[6] + ">" + bat_metadata[7] + ">" + bat_metadata[8] + ">" + bat_metadata[9] + ">" + bat_metadata[10] + ">" + bat_metadata[11] + ">" + bat_metadata[12])
				batsmen.append(bat_metadata[0] + ">" + bat_metadata[1] + ">" + bat_metadata[2] + ">" + bat_metadata[3] + ">" + bat_metadata[4] + ">" + bat_metadata[5] + ">" + bat_metadata[6] + ">" + bat_metadata[7] + ">" + bat_metadata[8] + ">" + bat_metadata[9] + ">" + bat_metadata[10] + ">" + bat_metadata[11] + ">" + bat_metadata[12])
			except:
				pass
	batsmen = list(dict.fromkeys(batsmen))
	batsmen_data = []
	for batsman in range(0,len(batsmen)):
		batsmen_data.append(batsmen[batsman].split(">"))

	# for p in batsmen_data:
	# 	print(p)

	with open ('q_bat_Score.csv', "a") as batFile:
		writer = csv.writer(batFile)
		writer.writerow([players[gamer1]]) 
		gamer1 += 1	
		for p in range(0,len(batsmen_data)):
			writer.writerow(batsmen_data[p])
		writer.writerow(["\n"])
	batFile.close()
	

	PlayerID2 = link.split("=")[1]
	bowlsite = "http://www.howstat.com/cricket/Statistics/Players/PlayerYears_ODI.asp?PlayerID=" + PlayerID2 + "#bowl"
	bowlpage = req.get(bowlsite)
	bowlsoup = bsoup(bowlpage.text, "lxml")
	bowl_table = bowlsoup.find("table", { "class" : "TableLined" })


	bowlers = []
	for new_char in bowl_table:
		trs = bowl_table.find_all('tr')
		for tr in trs:
			bowl_metadata = []
			tds = tr.find_all('td')
			for td in tds:
				bowl_metadata.append(td.text.strip())		
				# batsmen.append(bat_metadata[0] + ">" + bat_metadata[1] + ">" + bat_metadata[2] + ">" + bat_metadata[3] + ">" + bat_metadata[4] + ">" + bat_metadata[5] + ">" + bat_metadata[6] + ">" + bat_metadata[7] + ">" + bat_metadata[8] + ">" + bat_metadata[9] + ">" + bat_metadata[10] + ">" + bat_metadata[11] + ">" + bat_metadata[12] + ">" + bat_metadata[13])				
			try:
				# print(bat_metadata[0] + ">" + bat_metadata[1] + ">" + bat_metadata[2] + ">" + bat_metadata[3] + ">" + bat_metadata[4] + ">" + bat_metadata[5] + ">" + bat_metadata[6] + ">" + bat_metadata[7] + ">" + bat_metadata[8] + ">" + bat_metadata[9] + ">" + bat_metadata[10] + ">" + bat_metadata[11] + ">" + bat_metadata[12] + ">" + bat_metadata[13])				
				for index in range(0,12):
					if(bowl_metadata[index] == ""):
						bowl_metadata[index] = "0"
				# print(bowl_metadata[0] + ">" + bowl_metadata[1] + ">" + bowl_metadata[2] + ">" + bowl_metadata[3] + ">" + bowl_metadata[4] + ">" + bowl_metadata[5] + ">" + bowl_metadata[6] + ">" + bowl_metadata[7] + ">" + bowl_metadata[8] + ">" + bowl_metadata[9] + ">" + bowl_metadata[10] + ">" + bowl_metadata[11] + ">" + bowl_metadata[12])
				bowlers.append(bowl_metadata[0] + ">" + bowl_metadata[1] + ">" + bowl_metadata[2] + ">" + bowl_metadata[3] + ">" + bowl_metadata[4] + ">" + bowl_metadata[5] + ">" + bowl_metadata[6] + ">" + bowl_metadata[7] + ">" + bowl_metadata[8] + ">" + bowl_metadata[9])
			except:
				pass
	bowlers = list(dict.fromkeys(bowlers))
	bowlers_data = []
	for bowler in range(0,len(bowlers)):
		bowlers_data.append(bowlers[bowler].split(">"))

	for p in bowlers_data:
		print(p)

	# with open ('q_bowl_Score.csv', "a") as bowlFile:
	# 	writer = csv.writer(bowlFile)
	# 	writer.writerow([players[gamer2]]) 
	# 	gamer2 += 1
	# 	for p in range(0,len(bowlers_data)):
	# 		writer.writerow(bowlers_data[p])
	# 	writer.writerow(["\n"])	
	# bowlFile.close()

	# print("Here it is")
	# print(players)	
	# website = "http://howstat.com/cricket/Statistics/Players/PlayerList.asp?Group={}".format(chr(character))
	# webpage = req.get(website)
	# # soup = bsoup(webpage, "html.parser")
	# # table = webpage.select("table", { "class" : "TableLined" })
	# table = bsoup(webpage.text, "lxml")
	# # print(table.find)
	# findtbl = table.find("table", { "class" : "TableLined" })	

# for i in range(2,len(players)):
# 	print(players[i])


# http://www.howstat.com/cricket/Statistics/Players/PlayerYears_ODI.asp?PlayerID=4495
