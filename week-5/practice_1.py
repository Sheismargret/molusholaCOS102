import tkinter as tk

# Handling button click event
def button_click():
#print("button clicked!")

#show an information message box
msgbox.showinfo("Info", "Welcome to COS 102 GUI App!\n")

#Ask for user confirmation
result = msgbox.askyesno("COnfirmation", "Do you want to continue?")

#Create the main window
root = tk.Tk()
root.title("Home Page")
root.geometry("300x100")

#Add a label widget
label = tk.label(root, text = "Hello Friend \n")
label.pack()

#Add a button widget
button = tk.button(root, text="Click Me!", command=button_click)
button.pack()

#styling the button widget
button.config(fg = "red", bg="yellow")

#Start the event loop
root.mainloop() 