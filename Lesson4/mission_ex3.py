import tkinter as tk

class Timer:
    def __init__(self, root):
        self.root = root
        self.root.title("Timer")
        self.root.geometry("300x200")
        self.time_left = 60 # 初期値を60秒とする
        self.label = tk.Label(self.root, text=str(self.time_left), font=("Arial", 40))
        self.label.pack(pady=20)
        self.start_button = tk.Button(self.root, text="Start", command=self.start_timer)
        self.start_button.pack(side=tk.LEFT, padx=10)
        self.stop_button = tk.Button(self.root, text="Stop", command=self.stop_timer)
        self.stop_button.pack(side=tk.LEFT)
    def start_timer(self):
        self.start_button["state"]="disable"
        self.countdown()
    def countdown(self):
        if self.time_left> 0:
            self.label.config(text="{:.2f}".format(self.time_left))
            self.time_left-=0.1
            self.root.after(100, self.countdown)
            if self.time_left<=20:
                self.root.config(bg="yellow")
        else:
            self.label.config(text="Time's up!")
    def stop_timer(self):
        self.time_left = 0

if __name__ == "__main__":
    root = tk.Tk()
    timer = Timer(root)
    root.mainloop()