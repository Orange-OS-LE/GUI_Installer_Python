import tkinter, sys, os, subprocess

root = tkinter.Tk()
root.title("Orange OS Installer")
root.geometry("500x300")

def get_drives():
    drives = []
    for i in range(ord('a'), ord('z') + 1):
        drive = chr(i) + ":/"
        if os.path.isdir(drive):
            drives.append(drive)
    return drives

def get_hostname():
    return subprocess.check_output("hostname").decode("utf-8")

def get_hostname_entry():
    hostname = get_hostname()
    hostname_entry = tkinter.Entry(root)
    hostname_entry.insert(0, hostname)
    hostname_entry.pack()
    return hostname_entry

def get_drive_entry():
    drives = get_drives()
    drive_entry = tkinter.Entry(root)
    drive_entry.insert(0, drives[0])
    drive_entry.pack()
    return drive_entry

def get_drive_button():
    drive_button = tkinter.Button(root, text="Select Drive", command=get_drive_entry)
    drive_button.pack()
    return drive_button

def get_hostname_button():
    hostname_button = tkinter.Button(root, text="Select Hostname", command=get_hostname_entry)
    hostname_button.pack()
    return hostname_button

get_drive_button()
get_hostname_button()

root.mainloop()
