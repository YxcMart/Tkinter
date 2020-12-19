from tkinter import *
from PIL import Image, ImageTk



root = Tk()
root.title("Tkinter label")
root.geometry("500x500")

#1
    #anchor
"""
        This options controls where the text is positioned if the widget has more space than the text needs. The default is anchor=CENTER,
        which centers the text in the available space.
        NW;N;NE;W;CENTER;E;SW;S;SE
        """
#2	
    #bg
"""
        The normal background color displayed behind the label and indicator.
        """
#3	
    #bitmap
"""
        Set this option equal to a bitmap or image object and the label will display that graphic.
        "error";"gray75";"gray50";"gray25";"gray12";"hourglass";"info";"questhead";"question";"warning"
        """
#4	
    #bd
"""
        The size of the border around the indicator. Default is 2 pixels.
        """
#5	
    #cursor
"""
        If you set this option to a cursor name (arrow, dot etc.), the mouse cursor will change to that pattern when it is over the checkbutton.
        "arrow";"circle";"clock";"cross";"dotbox";"exchange";"fleur";"heart";"heart";"man";"mouse";"pirate";"plus";"shuttle";"sizing";"spider";"spraycan";"star";"target";"tcross";"trek";"watch"
        """
#6	
    #font
"""
        If you are displaying text in this label (with the text or textvariable option, the font option specifies in what font that text will be displayed.
        example font=("Times New Roman", 12, "bold")
        
        family − The font family name as a string.
        size − The font height as an integer in points. To get a font n pixels high, use -n.
        weight − "bold" for boldface, "normal" for regular weight.
        slant − "italic" for italic, "roman" for unslanted.
        underline − 1 for underlined text, 0 for normal.
        overstrike − 1 for overstruck text, 0 for normal.
        """
#7	
    #fg
"""
        If you are displaying text or a bitmap in this label, this option specifies the color of the text. If you are displaying a bitmap,
        this is the color that will appear at the position of the 1-bits in the bitmap.
        """
#8	
    #height
"""
        The vertical dimension of the new frame.
        """
#9	
    #image
"""
        To display a static image in the label widget, set this option to an image object.
        """
#10	
    #justify
"""
        Specifies how multiple lines of text will be aligned with respect to each other: LEFT for flush left, CENTER for centered (the default), or RIGHT for right-justified.
        LEFT;RIGHT;CENTER
        """
#11	
    #padx
"""
        Extra space added to the left and right of the text within the widget. Default is 1.
        """
#12	
    #pady
"""
        Extra space added above and below the text within the widget. Default is 1.
        """
#13	
    #relief
"""
        Specifies the appearance of a decorative border around the label. The default is FLAT; for other values.
        FLAT;RAISED;SUNKEN;GROOVE;RIDGE
        """
#14	
    #text
"""
        To display one or more lines of text in a label widget, set this option to a string containing the text. Internal newlines ("\n") will force a line break.
        """
#15	
    #textvariable
"""
        To slave the text displayed in a label widget to a control variable of class StringVar, set this option to that variable.
        """
#16	
    #underline
"""
        You can display an underline (_) below the nth letter of the text, counting from 0, by setting this option to n. The default is underline=-1, which means no underlining.
        TRUE;FALSE OR 0,1,2,3,4.....
        """
#17	
    #width
"""
        Width of the label in characters (not pixels!). If this option is not set, the label will be sized to fit its contents.
        """
#18
    #wraplength
"""
        You can limit the number of characters in each line by setting this option to the desired number. The default value, 0, means that lines will be broken only at newlines.
        """

#anchor; bg; text; fg; bd; padx; pady
Label(root,anchor=CENTER,  bg = "#bfbfbf", text = "Hello World",fg="#ffffff",padx=20,pady=20,bd=30,font=["Times", "24", "bold italic"]).pack()
#bitmap
Label(root,bitmap="error").pack()
Label(root,bitmap="error", text = "Hello World",fg="white").pack()


#image

image = Image.open("bg.jpg")
photo = ImageTk.PhotoImage(image)
label = Label(root, image=photo).pack()


root.mainloop()
