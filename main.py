import tkinter as tk
import time
import threading

class PomodoroApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🍅 Vishnupriya's Pomodoro Timer")
        self.root.geometry("300x200")
        self.root.resizable(False, False)

        self.timer_running = False
        self.time_left = 25 * 60  # 25 minutes

        self.label = tk.Label(root, text="🍅 25:00", font=("Helvetica", 30))
        self.label.pack(pady=20)

        self.start_button = tk.Button(root, text="Start Focus", command=self.start_timer)
        self.start_button.pack()

        self.reset_button = tk.Button(root, text="Reset", command=self.reset_timer)
        self.reset_button.pack(pady=10)

    def start_timer(self):
        if not self.timer_running:
            self.timer_running = True
            threading.Thread(target=self.countdown).start()

    def reset_timer(self):
        self.timer_running = False
        self.time_left = 25 * 60
        self.label.config(text="🍅 25:00")

    def countdown(self):
        while self.time_left > 0 and self.timer_running:
            mins, secs = divmod(self.time_left, 60)
            time_format = f"🍅 {mins:02d}:{secs:02d}"
            self.label.config(text=time_format)
            time.sleep(1)
            self.time_left -= 1

        if self.time_left == 0:
            self.label.config(text="✅ Done!")
            self.timer_running = False

if __name__ == "__main__":
    root = tk.Tk()
    app = PomodoroApp(root)
    root.mainloop()
