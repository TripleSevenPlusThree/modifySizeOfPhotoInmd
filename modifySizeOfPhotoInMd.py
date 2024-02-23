import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

# 创建窗口
root = tk.Tk()
root.title("批量修改md文件图片大小")
root.geometry("400x150")

# 创建输入框
tk.Label(root,text='设置尺寸（1000或其他）:').place(x=10,y=25)

var_usr_name=tk.StringVar()
entry=tk.Entry(root,textvariable=var_usr_name)
entry.place(x=160,y=25)

# 创建选择文件框和文件按钮命令函数
def open_file_dialog():
    value=entry.get()
    file_paths = filedialog.askopenfilenames()
    for file_path in file_paths:
      with open(file_path, 'r') as file:
        lines = file.readlines()
      with open(file_path,"w") as f:  
        for line in lines:
            url_1=line.find("!")
            url_2=line.find("[")
            if url_1 !=-1 and url_2!=-1:
                insert_1="-"
                line=line[:url_1]+insert_1+line[url_1:]
                position=line.find("]")
                insert_2="|"+value
                line=line[:position]+insert_2+line[position:]
            f.write(line)
    messagebox.showinfo("提醒", "操作已完成")
        
# 创建选择文件按钮
button = tk.Button(root, text="选择文件",width=15,height=1, command=open_file_dialog)
button.place(x=140,y=70)

# 退出按钮命令函数
def on_exit():
    root.destroy()
# 创建退出按钮
exit_button = tk.Button(root, text="完成并退出",width=10,height=1, command=on_exit)
exit_button.place(x=155,y=110)

root.mainloop()