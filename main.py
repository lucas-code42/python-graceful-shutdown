import sys
import time
import signal  # Signal handling library in Python


def sigterm_handler(signal_num, current_stack_frame):
    print("Received SIGTERM signal, starting graceful shutdown process")
    # Finish remaining processes here, if your app is multithreaded then
    # you might want to give a simple timeout in here to ensure the other
    # threads' task are finished

    # You can also start unsubscribing from message queues
    # or closing database connections in here.
    print("Remaining processes finished!, shutting down now.")

    print("signal_num", signal_num)
    print("current_stack_frame", current_stack_frame)

    sys.exit(0)  # Exit the Python app's process w/ 0 return code


def main():
    # Boot up your app, connect to DBs, message queues, etc.
    while True:
        print("Doing very important tasks...")
        time.sleep(2)  # Idle for 2 seconds


# Run sigterm_handler() whenever SIGTERM is received
signal.signal(signal.SIGINT, sigterm_handler)
main()
