import time
import os

start_time = None
elapsed_time = 0
running = False

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def header():
    print("=" * 40)
    print("        SIMPLE STOPWATCH")
    print("=" * 40)

def start():
    global start_time, running
    if not running:
        start_time = time.time()
        running = True
        print("Stopwatch has started.")
    else:
        print("Stopwatch already running.")

def stop():
    global running, elapsed_time
    if running:
        elapsed_time += time.time() - start_time
        running = False
        print("Stopwatch stopped.")
    else:
        print("Stopwatch is not running.")

def showtime():
    if running:
        current = elapsed_time + (time.time() - start_time)
    else:
        current = elapsed_time

    minutes, seconds = divmod(current, 60)
    print(f"Elapsed time: {int(minutes):02}:{seconds:05.2f}")

def reset():
    global start_time, elapsed_time, running
    start_time = None
    elapsed_time = 0
    running = False
    print("Stopwatch has been reset.")

def start_ui():
    while True:
        clear_screen()
        header()
        print("1. Stop")
        print("2. Show time")
        print("3. Reset")
        print("4. Back to main menu")

        choice = input("Input here: ").strip()

        if choice == "1":
            stop()
        elif choice == "2":
            showtime()
        elif choice == "3":
            reset()
        elif choice == "4":
            return
        else:
            print("Invalid choice.")

        input("\nPress Enter to continue...")

def main_ui():
    while True:
        clear_screen()
        header()
        print("1. Start")
        print("2. Exit")

        choice = input("Input here: ").strip()

        if choice == "1":
            start()
            start_ui()
        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    main_ui()
