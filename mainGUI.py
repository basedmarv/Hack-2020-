from tkinter import *
import openpyxl

from openpyxl import Workbook
# from openpyxl.utils import get_column_letter
def create_list(message_body):
    wb = Workbook()
    dest_filename = "sample.xlsx"

    sheet = wb.active
    sheet.title = "messages"

    arr = [] 

    # for x in range(sheet.max_row - 1):
    #     yuh = sheet.cell(x+2,1)
    #     arr.append(yuh)

    for row in range(1,20):
        for col in range(1,2):
            sheet.cell(column = col, row = row, value="{0}".format(message_body))

    wb.save(filename = dest_filename)

    return arr

def append_list(number, message_body):
    cells = create_list()
    cells[0] = message_body
    
        

def main():
    yessir = create_list()

    top = Tk()

    for x in range(len(yessir)):
        print(yessir[x].value)

    # window description
    top.title('The Newlyweds')
    top.geometry("500x400")

    # C = Canvas(top, bg = "black", height=250, width=300)
    # file = PhotoImage(file = "bg.jpg")
    # gr_label = Label(top, image=filename)
    # gr_label.place(x=0,y=0,relwidth=1,relheight=1)
    # C.pack()

    tobeWeds = Label(top, fg="red", text="Mr. and Mrs. ' Wedding", font="Times 16 italic").pack() 

    for x in range(len(yessir)):
        tobeWeds = Label(top, fg="red", text=yessir[x].value, font="Times 12").pack()
    messages = Text(top, height = 20, width = 50).pack()


    top.mainloop() 
 


if __name__ == "__main__":
    main()