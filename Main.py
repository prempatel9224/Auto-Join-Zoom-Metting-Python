import schedule
import time
from datetime import datetime
import webbrowser
#Enter Time In 24 Hour Format
tr = "15:15"#Enter The Time At You Want To Enter Metting
now = datetime.now().strftime("%H:%M")
def classe():
   #Enter The Link Of Your Metting
    webbrowser.open_new_tab("https://us05web.zoom.us/j/3205548410453?pwd=cmVLbEFGSjUvZEgwT1dZWi9pWG5XQT09")
    print("I'm Entering...")
    time.sleep(3)
    quit()

schedule.every(10).minutes.do(classe)
schedule.every().hour.do(classe)
schedule.every().day.at(tr).do(classe)


def timer():
    while True:
          schedule.run_pending()
          time.sleep(2)



timer().start()
