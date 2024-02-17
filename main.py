import requests,secrets
from hh import keep_alive
kk="7067616341"
m="HOPING YOU HIT 95% ON EXAMS! 💕"
ll=0
while True:
	try:
		l=secrets.token_hex(6)
		res=requests.get(f"https://mbomber.onrender.com/customsms/{kk}/antitoolz/{l}/{m}").text
		if 'success' in res:
			ll +=1
			print(f"Done Sended –—–⟩⟩ {ll}")
		else:
			print("Error")
	except RequestException:
		print("Are Net Toh On Kar")
keep_alive()
	
