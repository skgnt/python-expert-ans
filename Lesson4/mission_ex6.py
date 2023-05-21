import tkinter as tk
from tkinter import scrolledtext

class Timer:
    def __init__(self, root):
        self.root = root
        self.root.title("Timer")
        self.root.geometry("300x200")
        self.ttime=60
        self.time_left = 60 # 初期値を60秒とする
        #スクロールボックス挿入
        self.st= scrolledtext.ScrolledText(
                                        self.root, 
                                        width=20, 
                                        height=3,
                                        font=("Helvetica",
                                        10))
        self.st.pack()
        self.label = tk.Label(self.root, text=str(self.time_left), font=("Arial", 40))
        self.label.pack(pady=20)
        self.start_button = tk.Button(self.root, text="Start", command=self.start_timer)
        self.start_button.pack(side=tk.LEFT, padx=10)
        self.stop_button = tk.Button(self.root, text="rec", command=self.stop_timer)
        self.stop_button.pack(side=tk.LEFT)
        
    def start_timer(self):
        self.start_button["state"]="disable"
        self.countdown()
    def countdown(self):
        if self.time_left> 0:
            self.label.config(text="{:.2f}".format(self.time_left))
            self.time_left-=0.1
            self.root.after(100, self.countdown)
        else:
            self.label.config(text="Time's up!")
    def stop_timer(self):
        #tk.ENDはテキストボックスの文字列の最後の次の位置を示す。roundは四捨五入
        self.st.insert(tk.END,f"time:{round(self.time_left,2)}   ,   {round(self.ttime-self.time_left,2)}\n")

if __name__ == "__main__":
    root = tk.Tk()
    timer = Timer(root)
    root.mainloop()