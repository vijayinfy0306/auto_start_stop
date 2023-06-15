import threading
import time

# Global flag variable
running = False

def stopcall():
    val = input("Press Enter to stop the loop...")
    return val

# Function that runs the loop
def run_loop():
    global running
    while running:
        # Perform your desired actions inside the loop
        time.sleep(1)
        print("Running...")

        # Check if the loop should be terminated
        # if not running:
        #     print(f'{running} value')
        #     break

# Function to start the loop
def start_loop():
    global running
    if not running:
        running = True
        # Create and start a new thread for the loop
        thread = threading.Thread(target=run_loop)
        thread.start()
        print("Loop started.")

# Function to stop the loop
def stop_loop():
    global running
    print("Entered...")
    if running:
        running = False
        print("Loop stopped.")

# Example usage
command = input("Enter 'auto' to start the loop or 'stop' to terminate it: ")
if command == "auto":
    start_loop()  # Start the loop
    # input("Press Enter to stop the loop...")
    # stop_loop()  # Stop the loop
elif command == "stop":
    print("Loop terminated immediately.")
else:
    print("Invalid command.")

while True:
  response = stopcall()

  if response == 'stop':
      stop_loop()  # Stop the loop
      break
    













































# x = "awesome"


# def myfunc():
#     global x
#     x = "fantastic"
#     print("Python is " + x)

# myfunc()




# def secfun():
#   x = 10
#   print("value of x:",x)


# print("Python is " + x)

# secfun()