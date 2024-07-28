from plyer import notification
import time


if __name__== '__main__':
        while(True):
            notification.notify(
                title="Message from PC",
                message="Time to drink water",
                app_icon=None,
                timeout=5) 
            time.sleep(10)
                    

    


    

   