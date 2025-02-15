import sys, time, signal

name = sys.argv[1] if len(sys.argv) > 1 else "default"
iterations = int(sys.argv[2]) if len(sys.argv) > 2 else 100

counter = 0
is_force_shutdown = False

def shutdown(signal, frame):
    global is_force_shutdown
    print("Stopping task")
    is_force_shutdown = True

signal.signal(signal.SIGTERM, shutdown)
    
while True:
    counter += 1
    print("[%s]: Loop %s" % (name, counter))

    if counter >= iterations or is_force_shutdown:
        break

    time.sleep(5)