import time

def countdown_timer(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)  # Convert seconds into minutes and seconds
        timer = f"{mins:02d}:{secs:02d}"  # Format as MM:SS
        print(timer, end="\r")  # Print on the same line
        time.sleep(1)  # Wait for 1 second
        seconds -= 1
    
    print("Time's up!") 


try:
    total_time = int(input("Enter the time in seconds: "))
    countdown_timer(total_time)
except ValueError:
    print("Please enter a valid number.")
