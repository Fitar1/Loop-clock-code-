# Loop-clock-code-
import tkinter as tk
from time import strftime

def time():
    string = strftime('%Y-%m-%d %H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)

# 创建窗口
window = tk.Tk()
window.title("Real-Time Clock")

# 创建标签用于显示时间
label = tk.Label(window, font=('calibri', 40, 'bold'), background='black', foreground='white')
label.pack(anchor='center')

# 启动时钟函数
time()

# 不再调用 window.mainloop()
# window.mainloop()

# 运行窗口
window.update_idletasks()
window.update()

# 进入无限循环
while True:
    pass
