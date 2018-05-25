import Tkinter as tk


window = tk.Tk()

window.title("gps")

window.geometry("400x480")

#Tombol
button1 = tk.Button(text="track", bg="green")
button1.grid(column=1, row=1)

button2 = tk.Button(text="back", bg="red")
button2.grid(column=1, row=2)

button3 = tk.Button(text="STOP")
button3.grid(column=1, row=3)

#arah
entry_field1 = tk.Entry()
entry_field1.grid(column=1, row=4)

text_field = tk.Text(master=window, height=20, width=50)
text_field.grid(column=1, row=0)

window.mainloop()
