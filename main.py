import os
import time
import win10toast
import argparse

def show_notification(title, subtitle, message):
    # Play alert sound
    os.system('powershell -c "(New-Object Media.SoundPlayer \'C:\Windows\Media\Speech On.wav\').PlaySync()"')

    # Show notification
    toaster = win10toast.ToastNotifier()
    toaster.show_toast(title=title,
                       msg=message,
                       icon_path=None,
                       duration=10,
                       threaded=True)

def start_pomodoro(pomodoro_time):
    """Start a Pomodoro timer."""
    print("Starting Pomodoro...")
    time_left = pomodoro_time
    while time_left > 0:
        minutes, seconds = divmod(time_left, 60)
        time_str = f"{minutes:02d}:{seconds:02d}"
        print(f"Time left: {time_str}")
        time.sleep(1)
        time_left -= 1
    print("Pomodoro completed.")
    show_notification("Pomodoro completed", "", "Time is up.")

def take_short_break(short_break_time):
    """Take a short break."""
    print("Taking short break...")
    time_left = short_break_time
    while time_left > 0:
        minutes, seconds = divmod(time_left, 60)
        time_str = f"{minutes:02d}:{seconds:02d}"
        print(f"Time left: {time_str}")
        time.sleep(1)
        time_left -= 1
    show_notification("Short break completed", "", "Time for the next Pomodoro.")

def take_long_break(long_break_time):
    """Take a long break."""
    print("Taking long break...")
    time_left = long_break_time
    while time_left > 0:
        minutes, seconds = divmod(time_left, 60)
        time_str = f"{minutes:02d}:{seconds:02d}"
        print(f"Time left: {time_str}")
        time.sleep(1)
        time_left -= 1
    show_notification("Long break completed", "", "Time for the next Pomodoro.")

def main(pomodoro_time, short_break_time, long_break_time, num_pomodoros):
    """Main function of the script."""
    pomodoros_completed = 0
    while True:
        start_pomodoro(pomodoro_time)
        pomodoros_completed += 1
        if pomodoros_completed == num_pomodoros:
            take_long_break(long_break_time)
            pomodoros_completed = 0
        else:
            take_short_break(short_break_time)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Pomodoro Technique Script')
    parser.add_argument('pomodoro_time', type=int, help='Length of Pomodoro in seconds')
    parser.add_argument('short_break_time', type=int, help='Length of short break in seconds')
    parser.add_argument('long_break_time', type=int, help='Length of long break in seconds')
    parser.add_argument('num_pomodoros', type=int, help='Number of Pomodoros until long break')
    args = parser.parse_args()
    main(args.pomodoro_time, args.short_break_time, args.long_break_time, args.num_pomodoros)
