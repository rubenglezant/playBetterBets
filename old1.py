import requests

url = "https://betterbets.io/api/bets"
url = "https://betterbets.io/api/highrollers"
url = "https://betterbets.io/api/mybets?accessToken=4fd9ef572c6c32bf4d4290da3a29c7e1c2cbb94811ceea932640f37c8977868c"
url = "https://betterbets.io/api/user?accessToken=4fd9ef572c6c32bf4d4290da3a29c7e1c2cbb94811ceea932640f37c8977868c"

response = requests.get(url)

print response.text

if response.status_code == 200:
    results = response.json()
    for result in results:
        print result
else:
    print "Error code %s" % response.status_code

datos = {
    "accessToken": "4fd9ef572c6c32bf4d4290da3a29c7e1c2cbb94811ceea932640f37c8977868c",
    "wager": "0.00000001",
    "chance": "49.5",
    "direction": "0",
}

# curl --trace-ascii out.txt -d "accessToken=4fd9ef572c6c32bf4d4290da3a29c7e1c2cbb94811ceea932640f37c8977868c&seed=670843610" https://betterbets.io/api/seed
# curl --trace-ascii out.txt -d "accessToken=4fd9ef572c6c32bf4d4290da3a29c7e1c2cbb94811ceea932640f37c8977868c&wager=0.00000001&chance=49.5&direction=0" https://betterbets.io/api/betDice/

url = "https://betterbets.io/api/betDice/"
response = requests.post(url, data=datos)
print response.text
