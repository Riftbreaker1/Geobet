import requests
import time
from datetime import datetime, timezone

apikey_debug = "" # Insert your own API key here if you need, it's just used as a back up
norad_backup = "25544" # A backup NORAD ID for when none is inputted, change if needed
coords = "/41.702/-76.014/" # API default, add your own if you like

print("========================\n   Welcome to GeoBet!\n========================\n")

apikey = input("Please input your n2y0 API Key: ")
if apikey == "":
    apikey = apikey_debug
    print("API key was not added, used debug key")
print("API Key is" + apikey)

norad = input("Please input satelites NORAD ID (backup ID is: " + norad_backup + "): ")
if norad == "":
    norad = norad_backup
    print ("No NORAD ID was added, used " + norad_backup)

print("Please input what time you think the pass will occur, if you are within 10 minutes of the pass, then you win!")
prediction_year= int(input("Year: "))
prediction_month= int(input("Month: "))
prediction_monthday= int(input("Month day: "))
prediction_hour= int(input("Hour: "))
prediction_min= int(input("Minute: "))
prediction_sec= int(input("Second: "))

prediction = datetime(prediction_year, prediction_month, prediction_monthday, prediction_hour, prediction_min, prediction_sec, tzinfo=timezone.utc)
epoch_time = prediction.timestamp()

passtime = requests.get("https://api.n2yo.com/rest/v1/satellite/radiopasses/" + norad + coords + "0/1/11/&apiKey=" + apikey)
if passtime.status_code == 200:
    passes = passtime.json()

    pass_epoch = []

    for pass_info in passes.get("passes", []):
        pass_epoch.append(pass_info.get("startUTC"))
    
    print("Epoch time: " + str(pass_epoch))

    start_epoch = pass_epoch[0] if pass_epoch else 0
    start_datetime = datetime.fromtimestamp(start_epoch, tz=timezone.utc)

    start_normal = time.gmtime(start_epoch)

    if start_epoch - 600 <= epoch_time <= start_epoch + 600: # if guess is 10 minutes within start of pass, win
        print("Nice work! You were within 10 minutes of the pass start!")
    else:
        print("Good try, but you weren't within 10 minutes of the pass start...")

    print(f"Next pass starts at: {start_datetime.strftime('%Y-%m-%d %H:%M:%S UTC')}")
    print(f"Your prediction was: {prediction.strftime('%Y-%m-%d %H:%M:%S UTC')}")

    json_response_arg = input("Print full json recived? y/n")
    if json_response_arg == "y":
        print(passtime.json())
    else:
        print("\n")

else:
    print(passtime.status_code)