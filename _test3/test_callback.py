from tkinter import messagebox

def say_hello():
    messagebox.showinfo("Hello!", "Hello!")

def say_bye():
    messagebox.showinfo("Bye!")

def run_callback(callback):
    messagebox.showinfo("준비 중...")
    callback()
    messagebox.showinfo("완료!")

print("test 1..")
run_callback(say_hello)
print("test 2..")
run_callback(say_bye)
