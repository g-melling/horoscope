import requests

signs = requests.get("http://sandipbgt.com/theastrologer/api/sunsigns/").json()
user_sign = ""

print("** STAR SIGNS **")
for sign in signs:
    print(f"  - {sign.title()}")
    
while user_sign not in signs:
    user_sign = input("Please select your star sign: ").lower()
    
horoscope_json = requests.get(f"http://sandipbgt.com/theastrologer/api/horoscope/{user_sign}/today").json()

print(horoscope_json["horoscope"])