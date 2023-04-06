from tkinter import *
import socket
from tkinter import filedialog
import os

root = Tk()
root.title("FileShare")
root.geometry("450x560+500+200")
root.config(bg="#fff")
root.resizable(False, False)
global filename


def send():
    window = Toplevel(root)
    window.title("Send")
    window.geometry('450x560+500+200')
    window.config(bg="#fff")
    window.resizable(FALSE, FALSE)

    def select_file():
        filedialog.askopenfile(initialdir=os.getcwd(), title='Select Image',
                               filetypes=(('file_type', '*.txt'), ('allfiles', '*.*')))

    def sender():
        s = socket.socket()
        user: str = socket.gethostname()
        port = 8080
        s.bind((user, port))
        s.listen(1)
        print(user)
        print('waiting for any incoming connections....')
        conn, addr = s.accept()
        file = open(filename, 'rb')
        file_data = file.read(1024)
        conn.send(file_data)
        print('Data has been transmitted successfully..')

    # icon
    image_icon1 = PhotoImage(file='./Images/send.png')
    window.iconphoto(FALSE, image_icon1)

    s_background = PhotoImage(file='./Images/background.png')
    Label(window, image=s_background).place(x=-2, y=0)

    m_background = PhotoImage(file='./Images/Sender1.png')
    Label(window, image=m_background, height=216, width=430, bg='#D9D9D9').place(x=10, y=260)

    host = socket.gethostname()
    Label(window, text=f'Id:{host}', bg='#D9D9D9', fg='black', font='14').place(x=220, y=386)

    Button(window, text="+ Select File", width=10, height=1, font='arial 14 bold',
           bg='#D9D9D9', fg='#061C3C', command=select_file).place(x=160, y=180)
    Button(window, text="SEND", width=8, height=1, font='arial 14 bold', bg='#D9D9D9', fg='#061C3C',
           command=sender).place(x=300, y=180)

    window.mainloop()


def receive():
    main = Toplevel(root)
    main.title("Receive")
    main.geometry('450x560+500+200')
    main.config(bg="#fff")
    main.resizable(FALSE, FALSE)

    def accept():
        userid = sender_id.get()
        filename1: str = incoming_file.get()
        s = socket.socket()
        port = 8080
        s.connect((userid, port))
        file = open(filename1, 'wb')
        file_data = s.recv(1024)
        file.write(file_data)
        file.close()
        print("File has been received successfully")

    # icon
    image_icon2 = PhotoImage(file='./Images/received.png')
    main.iconphoto(FALSE, image_icon2)

    h_background = PhotoImage(file='./Images/receiver.png')
    Label(main, image=h_background).place(x=-2, y=0)

    logo = PhotoImage(file='Images/profile.png')
    Label(main, image=logo, bg='#fff').place(x=50, y=250)

    Label(main, text="Receive", font=('arial', 20), bg="#fff").place(x=150, y=280)

    Label(main, text='Input Sender id', font=('arial', 10, 'bold'), bg='#fff').place(x=20, y=340)
    sender_id = Entry(main, width=25, fg='black', border=2, bg='white', font=('arial', 15))
    sender_id.place(x=20, y=370)
    sender_id.focus()

    Label(main, text='filename for the incoming file:', font=('arial', 10, 'bold'), bg='#fff').place(x=20, y=420)
    incoming_file = Entry(main, width=25, fg='black', border=2, bg='white', font=('arial', 15))
    incoming_file.place(x=20, y=450)

    image_icon1 = PhotoImage(file='./Images/arrow.png')
    rr = Button(main, text=' Receive', compound=LEFT, image=image_icon1, width=160, bg='#D9D9D9', font='arial 14 bold',
                command=accept)
    rr.place(x=20, y=485)
    main.mainloop()


# icon
image_icon = PhotoImage(file="./Images/icon.png")

root.iconphoto(False, image_icon)

Label(root, text="File Transfer", font=("Acumen Variable Concept", 20, 'bold'),
      bg="#fff").place(x=20, y=30)
Frame(root, width=400, height=2, bg="#f3f5f6").place(x=30, y=80)

send_image = PhotoImage(file='./Images/send.png')
send = Button(root, image=send_image, bg="#fff", bd=0, command=send)
send.place(x=50, y=100)

receive_image = PhotoImage(file='./Images/received.png')
receive = Button(root, image=receive_image, bg="#fff", bd=0, command=receive)
receive.place(x=300, y=100)

# label
Label(root, text="Send", font=("Acumen Variable Concept", 17, 'bold'),
      bg='#fff').place(x=50, y=170)
Label(root, text="Receive", font=("Acumen Variable Concept", 17, 'bold'),
      bg='#fff').place(x=285, y=170)

back_image = PhotoImage(file="./Images/back1.png")
Label(root, image=back_image, height=230, width=445).place(x=-2, y=323)
root.mainloop()
