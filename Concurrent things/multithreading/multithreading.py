import threading
def print_current_thread():
    for _ in range(2):
        print(threading.current_thread().name)
        print(threading.current_thread().name)
def run_multithread():
    for _ in range(2):
        threading.Thread(target=print_current_thread).start()
run_multithread()