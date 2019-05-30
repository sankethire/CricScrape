from bs4 import BeautifulSoup as bsoup
import requests as req
import lxml
import sys
import csv


character = int(ord(sys.argv[1]))
ctr = chr(character)

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

new_char = ctr
gamer1 = 1
gamer2 = 1
for link in links:
	try:

		print(link.split("=")[1])

		PlayerID = link.split("=")[1]
		bowlsite = "http://www.howstat.com/cricket/Statistics/Players/PlayerYears_ODI.asp?PlayerID=" + PlayerID + "#bowl"
		bowlpage = req.get(bowlsite)
		bowlsoup = bsoup(bowlpage.text, "lxml")
		# bowl_table_t = bowlsoup.find("div",{"id" : "bowl"})
		bowl_table = bowlsoup.find("table", {"class" : "TableLined"})
		# bowl_table = 
		# print((bowl_table))

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
					for index in range(0,10):
						if(bowl_metadata[index] == ""):
							bowl_metadata[index] = "0"
					# print(bowl_metadata[0] + ">" + bowl_metadata[1] + ">" + bowl_metadata[2] + ">" + bowl_metadata[3] + ">" + bowl_metadata[4] + ">" + bowl_metadata[5] + ">" + bowl_metadata[6] + ">" + bowl_metadata[7] + ">" + bowl_metadata[8] + ">" + bowl_metadata[9] + ">" + bowl_metadata[10] + ">" + bowl_metadata[11] + ">" + bowl_metadata[12])
					bowlers.append(bowl_metadata[0] + ">" + bowl_metadata[1] + ">" + bowl_metadata[2] + ">" + bowl_metadata[3] + ">" + bowl_metadata[4] + ">" + bowl_metadata[5] + ">" + bowl_metadata[6] + ">" + bowl_metadata[7] + ">" + bowl_metadata[8] + ">" + bowl_metadata[9])
					# print(bowl_metadata[0] + ">" + bowl_metadata[1] + ">" + bowl_metadata[2] + ">" + bowl_metadata[3] + ">" + bowl_metadata[4] + ">" + bowl_metadata[5] + ">" + bowl_metadata[6] + ">" + bowl_metadata[7] + ">" + bowl_metadata[8] + ">" + bowl_metadata[9])
				except:
					pass
		bowlers = list(dict.fromkeys(bowlers))
		bowlers_data = []
		for bowler in range(0,len(bowlers)):
			bowlers_data.append(bowlers[bowler].split(">"))

		# print(bowlers.split(">"))	
		
		for p in bowlers:
			print(p)

		with open ('q_bowl_Score.csv', "a") as bowlFile:
			writer = csv.writer(bowlFile)
			writer.writerow([players[gamer2]]) 
			gamer2 += 1
			for p in range(1,len(bowlers_data)):
				writer.writerow(bowlers_data[p])
			writer.writerow(["\n"])	
		# bowlFile.close()
	except:
		# print(link.split("=")[1])

		# PlayerID1 = link.split("=")[1]
		# bowlsite1 = "http://www.howstat.com/cricket/Statistics/Players/PlayerYears_ODI.asp?PlayerID={}#bowl".format(PlayerID1)
		# bowlpage1 = req.get(bowlsite1)
		# bowlsoup1 = bsoup(bowlpage1.text, "lxml")
		# bowl_table1 = bowlsoup1.select("#bowl > table")
		# print()
		# print()
		# print()
		# print()
		# print(bowlsoup1)

		w = "http://www.howstat.com/cricket/Statistics/Players/PlayerYears.asp?PlayerID={}#bowl".format(link.split("=")[1])
		r = req.get(w)
		s = bsoup(r.text, "lxml")
		t = s.select("#bowl > table")
		t = t[0]
		# print(t[0].find_all('tr'))
		blrs = []
		for new_char in t:
			trs = t.find_all('tr')
			for tr in trs:
				bowl_metadata1 = []
				tds = tr.find_all('td')
				for td in tds:
					bowl_metadata1.append(td.text.strip())	
					# print(bowl_metadata1)	
					# batsmen.append(bat_metadata[0] + ">" + bat_metadata[1] + ">" + bat_metadata[2] + ">" + bat_metadata[3] + ">" + bat_metadata[4] + ">" + bat_metadata[5] + ">" + bat_metadata[6] + ">" + bat_metadata[7] + ">" + bat_metadata[8] + ">" + bat_metadata[9] + ">" + bat_metadata[10] + ">" + bat_metadata[11] + ">" + bat_metadata[12] + ">" + bat_metadata[13])				
				try:
					# print(bat_metadata[0] + ">" + bat_metadata[1] + ">" + bat_metadata[2] + ">" + bat_metadata[3] + ">" + bat_metadata[4] + ">" + bat_metadata[5] + ">" + bat_metadata[6] + ">" + bat_metadata[7] + ">" + bat_metadata[8] + ">" + bat_metadata[9] + ">" + bat_metadata[10] + ">" + bat_metadata[11] + ">" + bat_metadata[12] + ">" + bat_metadata[13])				
					for index in range(0,10):
						if(bowl_metadata1[index] == ""):
							bowl_metadata1[index] = "0"
					# print(bowl_metadata[0] + ">" + bowl_metadata[1] + ">" + bowl_metadata[2] + ">" + bowl_metadata[3] + ">" + bowl_metadata[4] + ">" + bowl_metadata[5] + ">" + bowl_metadata[6] + ">" + bowl_metadata[7] + ">" + bowl_metadata[8] + ">" + bowl_metadata[9] + ">" + bowl_metadata[10] + ">" + bowl_metadata[11] + ">" + bowl_metadata[12])
					blrs.append(bowl_metadata1[0] + ">" + bowl_metadata1[1] + ">" + bowl_metadata1[2] + ">" + bowl_metadata1[3] + ">" + bowl_metadata1[4] + ">" + bowl_metadata1[5] + ">" + bowl_metadata1[6] + ">" + bowl_metadata1[7] + ">" + bowl_metadata1[8] + ">" + bowl_metadata1[9])
					# print(bowl_metadata[0] + ">" + bowl_metadata[1] + ">" + bowl_metadata[2] + ">" + bowl_metadata[3] + ">" + bowl_metadata[4] + ">" + bowl_metadata[5] + ">" + bowl_metadata[6] + ">" + bowl_metadata[7] + ">" + bowl_metadata[8] + ">" + bowl_metadata[9])
				except:
					pass
		blrs = list(dict.fromkeys(blrs))
		blrs = blrs[1:]
		blrs_data = []
		for blr in range(0,len(blrs)):
			blrs_data.append(blrs[blr].split(">"))

		# print(bowlers.split(">"))	
		
		for p1 in blrs:
			print(p1)

		with open ('q_bowl_Score.csv', "a") as bowlFile:
			writer = csv.writer(bowlFile)
			writer.writerow([players[gamer2]]) 
			gamer2 += 1
			for p in range(1,len(bowlers_data)):
				writer.writerow(bowlers_data[p])
			writer.writerow(["\n"])			
