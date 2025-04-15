import tkinter as tk
import time

class Stopwatch:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Stopwatch")

        self.running = False
        self.start_time = 0
        self.elapsed_time = 0

        self.time_label = tk.Label(root, text="00:00:00", font=("Helvetica", 48))
        self.time_label.pack(pady=20)

        button_frame = tk.Frame(root)
        button_frame.pack()

        self.start_button = tk.Button(button_frame, text="Start", command=self.start, width=10)
        self.start_button.grid(row=0, column=0, padx=5)

        self.stop_button = tk.Button(button_frame, text="Stop", command=self.stop, width=10)
        self.stop_button.grid(row=0, column=1, padx=5)

        self.reset_button = tk.Button(button_frame, text="Reset", command=self.reset, width=10)
        self.reset_button.grid(row=0, column=2, padx=5)

        self.update_time()

    def update_time(self):
        if self.running:
            self.elapsed_time = time.time() - self.start_time
        time_str = self.format_time(self.elapsed_time)
        self.time_label.config(text=time_str)
        self.root.after(100, self.update_time)

    def format_time(self, seconds):
        mins, secs = divmod(int(seconds), 60)
        hours, mins = divmod(mins, 60)
        return f"{hours:02}:{mins:02}:{secs:02}"

    def start(self):
        if not self.running:
            self.start_time = time.time() - self.elapsed_time
            self.running = True

    def stop(self):
        if self.running:
            self.running = False

    def reset(self):
        self.running = False
        self.elapsed_time = 0
        self.time_label.config(text="00:00:00")

# Run the stopwatch
root = tk.Tk()
stopwatch = Stopwatch(root)
root.mainloop()
