import tkinter as tk
import qrcode
from tkinter import messagebox
from tkinter import PhotoImage
from tkinter import ttk

userEntryText = ""


def save_qrcode(qrdata):
    origin_path = 'Result'
    if QR_COLOR.get() != "1":
        img = qrdata.make_image(back_color=list(QR_COLOR.get().split(" "))[0], fill_color=list(QR_COLOR.get().split(" "))[1])
        img.save(f"{userEntryText}.png")
    else:
        img = qrdata.make_image()
        img.save(f"{userEntryText}.png")


def make_qr():
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(qrdata_entry.get())
    qr.make(fit=True)

    save_qrcode(qr)

    img = PhotoImage(file=f"{userEntryText}.png")

    image_label.config(image=img)
    image_label.photo = img
    image_label.pack(anchor="center", expand=True)


def accept_input():
    global userEntryText

    if qrdata_entry.get() != "" or qrdata_entry.get() is None:
        userEntryText = qrdata_entry.get()
        make_qr()
    else:
        messagebox.showerror("Nothing TO Make Qr From", 'Please Enter Something in Field!')


root = tk.Tk()
root.geometry("500x600")
root.configure(bg='black')
root.title("QR Maker")
root.eval('tk::PlaceWindow . center')

image_label = tk.Label(root, relief="solid")

main_frame = tk.Frame(root, background="black", width=500, height=250)
main_frame.pack(pady=10, anchor=tk.CENTER, side=tk.TOP)

label = tk.Label(main_frame, text="Enter QR Data:", fg="white", bg="black", font=("NPIAmir", 17))
label.grid(row=0, column=0, padx=10, pady=10)

qrdata_entry = tk.Entry(main_frame, fg="black", bg="white", font=("NPIAmir", 17), relief='solid', bd=5)
qrdata_entry.grid(row=0, column=1, padx=10, pady=10)

rd_frame = tk.Frame(root, background="black")
rd_frame.pack(anchor="center", side="top")
QR_COLOR = tk.StringVar(rd_frame, "1")
colors = [("#B7F1F5", "#E440A8"), ("#5DE541", "#2A39D8"), ("#F6DB09", "#FD5142")]
style = ttk.Style(rd_frame)
style.configure("TRadiobutton", background="black", foreground="white", font=("NPIAmir", 15))
rd_blue_pink = ttk.Radiobutton(rd_frame, text="Blue/Pink",
                              variable=QR_COLOR, value=colors[0])
rd_blue_pink.grid(row=0, column=1, pady=10, padx=5)
lbl_blue = tk.Label(rd_frame, text="   ", bg="#B7F1F5")
lbl_blue.grid(row=0, column=2, pady=10)
lbl_pink = tk.Label(rd_frame, text="   ", bg="#E440A8")
lbl_pink.grid(row=0, column=3, pady=10)

rd_green_blue = ttk.Radiobutton(rd_frame, text="green/blue",
                               variable=QR_COLOR, value=colors[1])
rd_green_blue.grid(row=0, column=4, pady=10,  padx=5)
lbl_green = tk.Label(rd_frame, text="   ", bg="#5DE541")
lbl_green.grid(row=0, column=5, pady=10)
lbl_blue = tk.Label(rd_frame, text="   ", bg="#2A39D8")
lbl_blue.grid(row=0, column=6, pady=10)

rd_yellow_red = ttk.Radiobutton(rd_frame, text="yellow/red",
                               variable=QR_COLOR, value=colors[2])
rd_yellow_red.grid(row=0, column=7, pady=10,  padx=5)
lbl_yellow = tk.Label(rd_frame, text="   ", bg="#F6DB09")
lbl_yellow.grid(row=0, column=8, pady=10)
lbl_red = tk.Label(rd_frame, text="   ", bg="#FD5142")
lbl_red.grid(row=0, column=9, pady=10)

submit_button = tk.Button(main_frame, text="Submit", command=accept_input, fg="white", bg="black", bd=1,
                          font=("NPIAmir", 20), relief='solid')
submit_button.grid(row=1, column=0, columnspan=2, pady=10)

root.mainloop()
