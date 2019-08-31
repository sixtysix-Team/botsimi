#bot aliansi simi
#aunthor : David Apriyanto (BLANK)
#team : sixtysix-Team

#module (perintah kerja)
import requests
import os
import json

#color
k = '\033[93m'
u = '\033[95m'
n  = '\033[94m'
m = '\033[91m'
h = '\033[92m'
p = '\033[00m'

#clear system
os.system('clear')

#banner
print n+" _           _   ____  _           _"
print n+"| |__   ___ | |_/ ___|(_)_ __ ___ (_)"
print n+"| '_ \ / _ \| __\___ \| | '_ ` _ \| |"
print k+"| |_) | (_) | |_ ___) | | | | | | | |"
print k+"|_.__/ \___/ \__|____/|_|_| |_| |_|_|"
print n+"author"+p+" = "+k+"David Apriyanto"
print

#variable nama&bahasa
nama = raw_input(n+"[#]"+p+" nama : ")
bhs = raw_input(n+"[#]"+p+" bahasa : ")
print

#perulangan
while(True):
	try:
		#input nama
		msg = raw_input(k+nama+" : ")
		#data mesin
		url = "https://wsapi.simsimi.com/190410/talk/"
		payload = "{\n\t\"utext\" : \"%s\",\n\t\"lang\": \"id\" \n}"%(msg)
		headers = {'Content-Type': "application/json",'x-api-key': "0xVM2jLGAH8vL4Zj4XzU0DhnVGIH6xQv4TrnFZIm"} #apikey
		
		#menjalankan mesin
		response = requests.request("POST", url, data=payload, headers=headers)
		#parse aray ke json
		a = json.loads(response.text)
		#menjalankan json decode
		print h+"(-_-)"+u+" simi : "+a["atext"]
	#penutup program
	except KeyboardInterrupt:
		exit()