
# iskat  center i krasit ego

from tkinter import Tk, Label, StringVar, Button, Entry

window = Tk()

window.title("Matrix")
window.geometry("1000x1000+120+120")
window.configure(bg='bisque2')
window.resizable(False, False)

# empty arrays for your Entrys and StringVars
text_var = []
entries = []

# # callback function to get your StringVars
# def get_mat():
#     matrix = []     # createing a matrix
#     for i in range(rows):
#         matrix.append([])
#         for j in range(cols):
#             matrix[i].append(text_var[i][j].get())
#
#     print(matrix)

# Label(window, text="Enter matrix :", font=('arial', 10, 'bold'),
#       bg="bisque2").place(x=20, y=20)


# def paint_button():
#     coord_button['bg'] = 'red'

x2 = 0
y2 = 0
rows, cols = (20,20)

for i in range(rows):
    # append an empty list to your two arrays
    # so you can append to those later
    text_var.append([])
    entries.append([])
    for j in range(cols):
        # append your StringVar and Entry
        text_var[i].append(StringVar())
        #entries[i].append(Entry(window, textvariable=text_var[i][j],width=3))  # here is an entry to input coords
        entries[i].append(Button())
        entries[i][j].place(x=60 + x2, y=50 + y2)
        x2 += 30

    y2 += 30
    x2 = 0

button= Button(window,text="Submit", bg='bisque3', width=15)
button.place(x=800,y=900)

window.mainloop()
