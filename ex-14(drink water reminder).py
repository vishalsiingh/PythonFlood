# import time
# from plyer import notification

# notification.notify(
#     title="💧 Drink Water Reminder",
#     message="Stay hydrated! Drink a glass of water now.",
#     timeout=10  # Notification stays for 10 seconds
#     )
    
import time
from plyer import notification

def drink_water_reminder():
    while True:
        notification.notify(
            title="💧 Time to Hydrate!",
            message="Take a short break and drink a glass of water. Stay healthy!",
            app_name="Drink Water Reminder",
            timeout=10
        )
        
        time.sleep(30)

if __name__ == "__main__":
    drink_water_reminder()

    

