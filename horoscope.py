import requests

signs = requests.get("http://sandipbgt.com/theastrologer/api/sunsigns/").json()

print("Please select your star sign:")
for sign in signs:
    print(f"  - {sign}")