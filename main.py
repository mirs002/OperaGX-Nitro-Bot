import requests
import uuid
import time
url = "https://api.discord.gx.games/v1/direct-fulfillment"
headers = {
            "Content-Type": "application/json",
            "Sec-Ch-Ua": '"Opera GX";v="105", "Chromium";v="119", "Not?A_Brand";v="24"',
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 OPR/105.0.0.0",
        }
data = {"partnerUserId": str(uuid.uuid4())}
        
def generation(loop_amount, interval):              
    for i in range(int(loop_amount)):
        try:
            response = requests.post(url, json=data, headers=headers)
            promo = f"https://discord.com/billing/partner-promotions/1180231712274387115/{response.json().get('token')}"
            with open("promotions.txt", "a") as f:f.write(f"\n{promo}\n")
            print("Generated new code: " + promo)
            print("Total Codes: " + str(i+1) + "\n")
            time.sleep(float(interval))
        except:
            print("An Error happened. Please wait a moment, if this issue persists, please restart the program.")
            time.sleep(15)
            continue

if __name__ == "__main__":
    loop_amount = input('How many Codes do you want?\n"Inf" for infinite.\nAmount: ')
    print("")
    interval = input('How long do you want to wait between each generation?\nDont make it too short, or you will get timed out quickly.\nSeconds (Press "Enter" for default): ')
    print("")
    if interval == "":
        interval = 1
    if loop_amount.lower() == "inf":
        loop_amount = 999999999999
    generation(loop_amount, interval)
