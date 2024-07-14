from tkinter import * 
from tkinter .messagebox import * 
from qrcode import * 

root = Tk()
root.title("QR code generator by hasrh")
root.geometry("700x500+50+50")
f = ("Arial", 30, "bold")

def gen():
	url = ent_url.get()
	if url == "":
		showerror("issue", "url is empty")
		ent_url.focus()
		return
	img = make(url)
	
	filename = ent_file.get()
	if filename == "":
		showerror("issue", "u did not enter filename")
		ent_file.focus()
		return

	img.save(str(filename) + ".png")
	showinfo("Success", "QR code generated in the  folder")
	
	ent_url.delete(0, END)
	ent_file.delete(0, END)
	ent_url.focus()

lab_title = Label(root, text="QR code wallah", font=f)
lab_url = Label(root, text="enter url", font=f)
ent_url = Entry(root, font=f)
lab_file = Label(root, text="Enter filname", font=f)
ent_file = Entry(root, font=f)
btn_generate = Button(root, text="Generate QR Code", font=f, command=gen)

lab_title.pack(pady=5)
lab_url.pack(pady=5)
ent_url.pack(pady=5)
lab_file.pack(pady=5)
ent_file.pack(pady=5)
btn_generate.pack(pady=5)

root.mainloop()