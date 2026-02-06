import requests
from plyer import notification
import time
import schedule


# usage of Nofitication-->

# notification.notify(
#     title="Alert",
#     message="Task complete",
#     timeout=10  # Seconds
# )


def update():
    r = requests.get('https://disease.sh/v3/covid-19/countries/bangladesh')
    data = r.json()
    notification.notify(
        title="COVID Bangladesh",
        message=f"Cases: {data['cases']:,} Deaths: {data['deaths']:,} Recovered: {data['recovered']:,}",
        timeout=10
    )

# notification after 24 hour later-->

while True:
    update()
    time.sleep(86400)
    
    

# if we use schedule-->

# schedule.every().day.at("09:00").do(update)
# while True:
#     schedule.run_pending()
#     time.sleep(60) 
