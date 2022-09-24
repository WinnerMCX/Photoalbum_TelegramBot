from tkinter import *
from datetime import datetime

temp = 0
after_id = ""
def tick():
    global temp, after_id
    f_temp = datetime.fromtimestamp(temp).strftime("%M:%S")
    label.configure(text=str(f_temp))
    temp +=1
    after_id = main_window.after(1000, tick)
def start_tick():
    btn_start.pack_forget()
    btn_stop.pack()
    tick()
def stop_tick():
    global temp
    temp = 0
    btn_stop.pack_forget()
    main_window.after_cancel(after_id)
    label.configure(text=0)
    btn_start.pack()

main_window = Tk()

main_window['bg'] = '#fafafa'
main_window.title("Секундомер")
main_window.wm_attributes("-alpha", 1)
main_window.geometry("300x250")
main_window.resizable(width=False,height=False)


label = Label(main_window,text="00:00",bg="white")
label.place(relx=0.31,rely=0.10,relwidth=0.4,relheight=0.4)

btn_start = Button(main_window, text="Старт",bg="gray",command=start_tick )
btn_pause = Button(main_window, text="Пауза",bg="gray")
btn_stop = Button(main_window, text="Стоп",bg="gray", command=stop_tick)
btn_continue = Button(main_window, text="Продолжить",bg="gray")
btn_start.pack()

main_window.mainloop()