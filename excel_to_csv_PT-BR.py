#!/usr/bin/env python3

#!/usr/bin/env python3

import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import pandas as pd


root= tk.Tk()
root.iconbitmap('')
#Nomeando o título do programa
root.title('Converter by Fred Silva')
#Impedindo maximização do programa
root.resizable(0,0)

#Definindo propriedades do Canvas
canvas1 = tk.Canvas(root, width = 300, height = 250, bg = 'lightsteelblue2', relief = 'raised')
canvas1.pack()

# Criando botões do programa
label1 = tk.Label(root, text='Conversor de Arquivos', bg = 'lightsteelblue2', fg='green')
label1.config(font=('helvetica', 20))
canvas1.create_window(150, 50, window=label1)

#Declarando funções e ajustando o modelo 
def getExcel ():
	global read_file
	
	import_file_path = filedialog.askopenfilename()
	read_file = pd.read_excel (import_file_path)
	
	export_file_path = filedialog.asksaveasfilename(defaultextension='.csv')
	read_file.to_csv (export_file_path, index = None, header=True)
	
browseButton_Excel = tk.Button(text="Importar Arquivo Excel para CSV", command=getExcel, bg='gray', fg='blue', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 100, window=browseButton_Excel)


def getCSV ():
	global read_file
	
	import_file_path = filedialog.askopenfilename()
	read_file = pd.read_csv (import_file_path)
	
	export_file_path = filedialog.asksaveasfilename(defaultextension='.xlsx')
	read_file.to_excel (export_file_path, index = None, header=True)
	
browseButton_CSV = tk.Button(text="Importar Arquivo CSV para Excel", command=getCSV, bg='gray', fg='blue', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 150, window=browseButton_CSV)

def exitApplication():
	MsgBox = tk.messagebox.askquestion ('Sair do aplicativo','Você tem certeza que gostaria de sair',icon = 'warning')
	if MsgBox == 'yes':
		root.destroy()
		
exitButton = tk.Button (root, text='Sair do aplicativo',command=exitApplication, bg='gray', fg='red', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 200, window=exitButton)
#root.mainloop()

def help():
	MsgBox = tk.messagebox.showinfo ('Ajuda','Para converter um arquivo:\n1-Clicar na conversão desejada.\n2-Localizar e selecionar o arquivo\n3-Selecionar onde deseja salvar o arquivo convertido.\n4-Digitar qual o nome que deseja dar ao arquivo convertido.\n5-Clicar em "Save".\n6-Pronto, seu arquivo já estará convertido e na pasta de destino')
	root.mainloop()
helpButton= tk.Button (root, text='Ajuda❓',command=help, bg='lightsteelblue2', fg='black', font=('helvetica', 12, 'bold')).place(x=220, y=0)
canvas1.create_window(150, 100, window=helpButton)
root.mainloop()