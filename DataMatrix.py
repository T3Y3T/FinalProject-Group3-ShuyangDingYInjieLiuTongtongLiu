import tkinter
from pystrich.datamatrix import DataMatrixEncoder

def DataMatrix():
    code = input("What is your data：")
    encoder = DataMatrixEncoder("{:0>6}".format(code))
    encoder.save("DM01.png", cellsize=20)


def ShowDataMatrix():
    root = tkinter.Tk()
    canvas = tkinter.Canvas(root, width=600, height=600, bg="white")
    img = tkinter.PhotoImage(file="DM01.png")
    canvas.create_image(300, 300, image=img)
    canvas.pack()
    root.mainloop()


if __name__ == "__main__":
    DataMatrix()
    ShowDataMatrix()

