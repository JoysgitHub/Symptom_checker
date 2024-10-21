import tkinter as tk

symptom1 = input("Symptom1 > ")
symptom2 = input("Symptom2 > ")
symptom3 = input("Symptom3 > ")


print(f"{symptom1}, {symptom2}, {symptom3}")



root = tk.Tk()
root.title("Symptom Checker")
root.geometry("400x300") 

root.mainloop()