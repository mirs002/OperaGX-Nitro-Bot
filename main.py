import requests
import uuid
import time

loop_amount = input("How many codes do you want?: ")
interval = input("How long do you want to wait between each code (in seconds)?: ")
url = "https://api.discord.gx.games/v1/direct-fulfillment"
headers = {
            "Content-Type": "application/json",
            "Sec-Ch-Ua": '"Opera GX";v="105", "Chromium";v="119", "Not?A_Brand";v="24"',
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 OPR/105.0.0.0",
        }
data = {"partnerUserId": str(uuid.uuid4())}

if loop_amount == "inf":
    while True:
        response = requests.post(url, json=data, headers=headers)
    promo = f"https://discord.com/billing/partner-promotions/1180231712274387115/{response.json().get('token')}"
    with open("promotions.txt", "a") as f:
                            f.write(f"\n{promo}\n")
    time.sleep(float(interval))
else:
    for i in range(int(loop_amount)):
        response = requests.post(url, json=data, headers=headers)
        promo = f"https://discord.com/billing/partner-promotions/1180231712274387115/{response.json().get('token')}"
        with open("promotions.txt", "a") as f:
                                f.write(f"\n{promo}\n")
        time.sleep(float(interval))