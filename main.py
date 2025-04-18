import time

def countdown(minutes):
    seconds = minutes * 60
    while seconds:
        mins = seconds // 60
        secs = seconds % 60
        print(f"{mins:02d}:{secs:02d}", end='\r')
        time.sleep(1)
        seconds -= 1
print("⏰Time's up")

countdown(25)