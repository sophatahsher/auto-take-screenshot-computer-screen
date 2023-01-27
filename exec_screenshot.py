import time
import tkinter
import telepot
import datetime
from PIL import ImageGrab

# set bot 
bot = telepot.Bot('{BOT_TOKEN}')

while True:

    now = datetime.datetime.now()

    # start at 12:00pm
    if  now.hour >= 12:

        # take screenshot in each & every 10mins
        if now.minute % 10 == 0:

            print('Screenshot inprogress...')

            # check screen resolution
            root = tkinter.Tk()
            width = root.winfo_screenwidth()
            height = root.winfo_screenheight()
            
            # 1440p monitor
            if width == 2560 and height == 1440:
                img = ImageGrab.grab(bbox=(40, 150, 2560, 1080))

            # 1080p monitor
            elif width == 1920 and height == 1080:
                img = ImageGrab.grab(bbox=(40, 115, 1920, 1050))

            
            #save screenshot
            img.save("screenshot.png")
            time.sleep(1)
            
            from datetime import datetime
            str_time = datetime.today().strftime("%I:%M %p") # %I 12 hour, %H 24-hours

            bot.sendPhoto({CHAT_ID}, photo=open('screenshot.png', 'rb'), caption=str_time)
            time.sleep(60)
            print('Success')

    # stop capturing at 05:00 pm
    elif now.hour == 17:
        break
