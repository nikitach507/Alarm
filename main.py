from datetime import datetime
from playsound import playsound


def validate_time(alarm_time):
    if len(alarm_time) != 11:
        return "Invalid time format! Please try again..."
    else:
        if int(alarm_time[0:2]) > 12:
            return "Invalid HOUR format! Please try again..."
        elif int(alarm_time[3:5]) > 59:
            return "Invalid MINUTE format! Please try again..."
        elif int(alarm_time[6:8]) > 59:
            return "Invalid SECOND format! Please try again..."
        else:
            return "Ok"


while True:
    alarm_time = input("Enter time in 'HH:MM:SS AM/PM' format: ")
    alarm_text = input("Enter event: ")

    validate = validate_time(alarm_time.lower())
    if validate != "Ok":
        print(validate)
    else:
        print(f"Setting alarm for {alarm_time}...")
        break

alarm_hour = alarm_time[0:2]
alarm_min = alarm_time[3:5]
alarm_sec = alarm_time[6:8]
alarm_period = alarm_time[9:].upper()


while True:

    now = datetime.now()

    current_hour = now.strftime("%I")
    current_min = now.strftime("%M")
    current_sec = now.strftime("%S")
    current_period = now.strftime("%p")

    if alarm_period == current_period:
        if alarm_hour == current_hour:
            if alarm_min == current_min:
                if alarm_sec == current_sec:
                    print(alarm_text)
                    playsound("Alarm/loud_alarm_clock.mp3")
                    choice = input("Press ENTER to stop playback or 'again' to snooze the alarm in 5 minutes: ")
                    if choice == "":
                        print("Bye")
                        break
                    elif choice == "again":
                        new_alarm_min = int(alarm_time[3:5]) + 1
                        if new_alarm_min < 10:
                            alarm_min = "0" + str(new_alarm_min)
                        elif new_alarm_min > 54:
                            new_alarm_hour = int(alarm_hour) + 1
                            if new_alarm_hour == 13:
                                alarm_hour = "01"
                            alarm_hour = str(new_alarm_hour)
                            alarm_min = "0" + str(new_alarm_min - 55)
                        else:
                            alarm_min = str(new_alarm_min)
                        alarm_time = alarm_hour + ":" + alarm_min + ":" + alarm_sec + " " + alarm_period
                        print(f"Setting alarm for {alarm_time}...")
                    else:
                        print("")