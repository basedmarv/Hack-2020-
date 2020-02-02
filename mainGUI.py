from tkinter import *
import openpyxl
from PIL import ImageTk, Image
import time
from openpyxl import Workbook
import Credentials

path = Credentials.path

def create_list(workbook):
    ws = workbook.active
    arr = [] 
    for x in range(ws.max_row - 1):
        createL = ws.cell(x+2,1)
        arr.append(createL)

    return arr


def main(message_body = None):

    wb = openpyxl.load_workbook(path)
    cL = create_list(wb)

    top = Tk()
    top.title('The Newlyweds')
    top.geometry("500x400")
    
    tobeWeds = Label(top, fg="red", text="Mr. and Mrs. Wedding", font="Times 16 italic").pack()

    maxR = wb.active.max_row
    
    count = 10
    if maxR < 10:
        for x in range(len(cL)):
            text_try = Text(top, height = 2, width = 50)
            text_try.tag_configure("left", justify='left')
            text_try.pack()
            text_try.insert(END, cL[x].value)
    else: 
        while count > 0:
            text_try = Text(top, height = 2, width = 50)
            text_try.tag_configure("left", justify='left')
            text_try.pack()
            text_try.insert(END, cL[maxR-count-1].value)
            count = count - 1

    top.mainloop() 
 
if __name__ == "__main__":
    main()
