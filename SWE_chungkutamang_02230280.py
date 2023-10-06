import pyautogui
import time
import threading
import queue

# Function to close a single tab
def close_tab():
    # Simulate the "Ctrl + W" keyboard 
    pyautogui.hotkey('ctrl', 'w')
    # Add a small delay to allow the tab to close
    time.sleep(1)
      

# Worker function to process tasks from the queue
def worker(q):
    while not q.empty():
        task = q.get()
        if task == "close_tab":
            close_tab()
        q.task_done()

# Function to close multiple tabs using a queue
def close_tabs_with_queue(num_tabs_to_close):
    # Create a queue for tasks
    task_queue = queue.Queue()

    # Enqueue "close_tab" tasks for the specified number of tabs
    for _ in range(num_tabs_to_close):
        task_queue.put("close_tab")

    # Create a worker thread to process tasks
    worker_thread = threading.Thread(target=worker, args=(task_queue,))
    worker_thread.start()

    # Wait for the worker thread to finish
    worker_thread.join()
    #it checks whether the cript id being run as the ain program
if __name__ == "__main__":
    # Ensure that the Firefox is active 

    # Specify the number of tabs to close
    # Change this to the number of tabs you want to close
    num_tabs_to_close = 10
    # Close the specified number of tabs using a queue
    close_tabs_with_queue(num_tabs_to_close)
    