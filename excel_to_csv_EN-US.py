#!/usr/bin/env python3

import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import pandas as pd

#Create the GUI
root= tk.Tk()
root.iconbitmap('')
#Naming the program Title
root.title('Converter by Fred Silva')
#Preventing program maximization
root.resizable(0,0)

#Setting Canvas Properties
canvas1 = tk.Canvas(root, width = 300, height = 250, bg = 'lightsteelblue2', relief = 'raised')
canvas1.pack()

# Creating program buttons
label1 = tk.Label(root, text='File Converter', bg = 'lightsteelblue2', fg='green')
label1.config(font=('helvetica', 20))
canvas1.create_window(150, 50, window=label1)

#Declaring Roles and Adjusting the Model 
def getExcel ():
	global read_file
	
	import_file_path = filedialog.askopenfilename()
	read_file = pd.read_excel (import_file_path)
	
	export_file_path = filedialog.asksaveasfilename(defaultextension='.csv')
	read_file.to_csv (export_file_path, index = None, header=True)
	
browseButton_Excel = tk.Button(text="Import Excel to CSV", command=getExcel, bg='gray', fg='blue', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 100, window=browseButton_Excel)


def getCSV ():
	global read_file
	
	import_file_path = filedialog.askopenfilename()
	read_file = pd.read_csv (import_file_path)
	
	export_file_path = filedialog.asksaveasfilename(defaultextension='.xlsx')
	read_file.to_excel (export_file_path, index = None, header=True)
	
browseButton_CSV = tk.Button(text="Import CSV File to Excel", command=getCSV, bg='gray', fg='blue', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 150, window=browseButton_CSV)

def exitApplication():
	MsgBox = tk.messagebox.askquestion ('Exit','Are you sure',icon = 'warning')
	if MsgBox == 'yes':
		root.destroy()
		
exitButton = tk.Button (root, text='Exit',command=exitApplication, bg='gray', fg='red', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 200, window=exitButton)
#root.mainloop()

def help():
	MsgBox = tk.messagebox.showinfo ('Help','To convert a file:\n1-Click the desired conversion.\n2-Find and select the file\n 3-Select where you want to save the converted file.\n4-Type what name you want to give the converted file. \n5-Click on "Save".\n6-Done, your file will already be converted and in the destination folder.')
	root.mainloop()
helpButton= tk.Button (root, text='Help❓',command=help, bg='lightsteelblue2', fg='black', font=('helvetica', 12, 'bold')).place(x=220, y=0)
canvas1.create_window(150, 100, window=helpButton)
root.mainloop()
