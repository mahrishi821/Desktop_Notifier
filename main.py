from plyer import notification
import time
if __name__=='__main__':
    while True:
        notification.notify(
            title="*** Take Rest ***",
            message="Rest is important for good functioning of brain",
            app_icon="D:/My_document/Python Scripts/python_project/Desktop_Notifier/clock_green.ico",
            timeout=5
        )
        time.sleep(10)