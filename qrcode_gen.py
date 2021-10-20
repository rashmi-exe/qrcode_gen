import qrcode
from tkinter import *

root = Tk()
root.title("QR CODE GENERATOR 😁")
input_frame = LabelFrame(root, text="INPUT FRAME", padx=10, pady=10)


def save():
    qr.save("qr_code.jpg")


def generator():
    global qr
    url = qrcode.make(s.get())
    # qr = qrcode.QRCode()
    # qr.add_data(s.get())
    # qr.make()
    # img = qr.make_image()
    # newWindow = Toplevel(root)
    # # type(img)
    # #img = url.make_image()
    # newWindow.title("QR CODE")
    # Label(newWindow, image=qr).pack()
    # Button(newWindow, text=" SAVE ", pady=10, padx=15, command=save).pack()
    url.save("qr_code.jpg")
    url.show("qr_code.jpg")


input_url = Label(input_frame, text=" Enter the url/text/number ")
s = Entry(input_frame, width=50)

create_qr = Button(root, text=" Create QR Code",
                   padx=15, pady=10, command=generator)

input_frame.pack()
input_url.grid(row=0, column=0)
s.grid(row=0, column=1, padx=15)
create_qr.pack()

root.mainloop()
