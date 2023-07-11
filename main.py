# Importing Tkinter...
from cgitb import text
from tkinter import *
from tkinter import font

from tkinter import ttk
from tkinter import messagebox

# Importing TKDatepiker
from tkcalendar import Calendar, DateEntry

# Importing TKDatepiker
from view import *

################# Colors ###############
co0 = "#f0f3f5"  # Preta
co1 = "#feffff"  # branca
co2 = "#4fa882"  # verde
co3 = "#38576b"  # valor
co4 = "#403d3d"   # letra
co5 = "#e06636"   # - profit
co6 = "#038cfc"   # azul
co7 = "#ef5350"   # vermelha
co8 = "#263238"   # + verde
co9 = "#e9edf5"   # sky blue

################# Creating window ###############

window = Tk()
window.title("")
window.geometry('1043x453')
window.configure(background=co9)
window.resizable(width=FALSE, height=FALSE)

################# Splitting the window ###############

frame_top = Frame(window, width=310, height=50, bg=co2, relief='flat')
frame_top.grid(row=0, column=0)

frame_bottom = Frame(window, width=310, height=403, bg=co1, relief='flat')
frame_bottom.grid(row=1, column=0, sticky=NSEW, padx=0, pady=1)

frame_right = Frame(window, width=588, height=403, bg=co1, relief='flat')
frame_right.grid(row=0, column=1, rowspan=2, padx=1, pady=0, sticky=NSEW)

################# Label top ###############
app_name = Label(frame_top, text='Formulario de Consultoria', anchor=NW, font=('Ivy 13 bold'), bg=co2, fg=co1, relief='flat')
app_name.place(x=10, y=20)

# Funcão Inserir
def inserir():
    nome = app_nome.delete(0, 'end')
    email = app_email.delete(0, 'end')
    tel = app_tel.delete(0, 'end')
    dia = app_cal.delete(0, 'end')
    estado = app_estado.delete(0, 'end')
    assunto = app_sobre.delete(0, 'end')
    
    lista = [nome, email, tel, dia, estado, assunto]
    
    if nome=='':
        messagebox.showerror('Erro', 'O nome não pode ser vázio')
    else:
        inserir_info(lista)
        messagebox.showinfo('Sucesso', 'Os dados foram inseridos com sucesso')
        
        nome.delete(0, 'end')
        email = app_email.delete(0, 'end')
        tel = app_tel.delete(0, 'end')
        dia = app_cal.delete(0, 'end')
        estado = app_estado.delete(0, 'end')
        assunto = app_sobre.delete(0, 'end')
        
    for widget in frame_right.winfo_children():
        widget.destroy()
        
    mostrar()


# Funcão Inserir
def atualizar():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        tree_lista = treev_dicionario['values']
        
        valor = tree_lista[0]
        
        app_nome.delete(0, 'end')
        app_email.delete(0, 'end')
        app_tel.delete(0, 'end')
        app_cal.delete(0, 'end')
        app_estado.delete(0, 'end')
        app_sobre.delete(0, 'end')
        
        app_nome.insert(0, tree_lista[1])
        app_email.insert(0, tree_lista[2])
        app_tel.insert(0, tree_lista[3])
        app_cal.insert(0, tree_lista[4])
        app_estado.insert(0, tree_lista[5])
        app_sobre.insert(0, tree_lista[6])
        
       
        def update():
            nome = app_nome.delete(0, 'end')
            email = app_email.delete(0, 'end')
            tel = app_tel.delete(0, 'end')
            dia = app_cal.delete(0, 'end')
            estado = app_estado.delete(0, 'end')
            assunto = app_sobre.delete(0, 'end')
            
            lista = [nome, email, tel, dia, estado, assunto]
            
            if nome=='':
                messagebox.showerror('Erro', 'O nome não pode ser vázio')
            else:
                atualizar_info(lista)
                messagebox.showinfo('Sucesso', 'Os dados foram atualizados com sucesso')
                
                app_nome.delete(0, 'end')
                app_email = app_email.delete(0, 'end')
                app_tel = app_cal.delete(0, 'end')
                dia = app_cal.delete(0, 'end')
                estado = app_estado.delete(0, 'end')
                assunto = app_sobre.delete(0, 'end')
                
            for widget in frame_right.winfo_children():
                widget.destroy()
                
            #Botão atualizar:
            b_confirmar = Button(frame_bottom,command=update, text='Atualizar', width=10, anchor=NW, font=('Ivy 7 bold'), bg=co2, fg=co1, relief='raised', overrelief='ridge')
            b_confirmar.place(x=110, y=380)
                
            mostrar()
        
    except IndexError:
        messagebox.showerror('Erro', 'Seleciona um dos dados na tabela')


        
        
################# Setting up bottom frame ###############

#Nome:
app_nome = Label(frame_bottom,text='Nome *', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
app_nome.place(x=10, y=10)
app_nome = Entry(frame_bottom, width=45, justify='left', relief='solid')
app_nome.place(x=15, y=40)

#Email:
app_email = Label(frame_bottom,text='Email *', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
app_email.place(x=10, y=70)
app_email = Entry(frame_bottom, width=45, justify='left', relief='solid')
app_email.place(x=15, y=100)

#Telefone:
app_tel = Label(frame_bottom,text='Telefone *', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
app_tel.place(x=10, y=130)
app_tel = Entry(frame_bottom, width=45, justify='left', relief='solid')
app_tel.place(x=15, y=160)

#Data da consulta:
app_cal = Label(frame_bottom,text='Data da consulta *', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
app_cal.place(x=10, y=190)
app_cal = DateEntry(frame_bottom, width=12, background='darkblue', foreground='white', borderwidth=2)
app_cal.place(x=15, y=220)

#Estado da consulta:
app_estado = Label(frame_bottom,text='Estado da consulta *', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
app_estado.place(x=160, y=190)
app_estado = Entry(frame_bottom, width=20, justify='left', relief='solid')
app_estado.place(x=160, y=220)

#Sobre:
app_sobre = Label(frame_bottom,text='Informações adicionais *', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
app_sobre.place(x=15, y=260)
app_sobre = Entry(frame_bottom, width=45, justify='left', relief='solid')
app_sobre.place(x=15, y=290)

#Botão inserir:
b_inserir = Button(frame_bottom,command=inserir, text='Inserir', width=10, anchor=NW, font=('Ivy 7 bold'), bg=co6, fg=co1, relief='raised', overrelief='ridge')
b_inserir.place(x=15, y=340)

#Botão atualizar:
b_inserir = Button(frame_bottom,text='Atualizar', width=10, anchor=NW, font=('Ivy 7 bold'), bg=co2, fg=co1, relief='raised', overrelief='ridge')
b_inserir.place(x=110, y=340)

#Botão deletar:
b_inserir = Button(frame_bottom,text='Deletar', width=10, anchor=NW, font=('Ivy 7 bold'), bg=co7, fg=co1, relief='raised', overrelief='ridge')
b_inserir.place(x=205, y=340)

################# Frame direita ###############

def mostrar():
    
    lista = []

    # lista para cabecario
    tabela_head = ['ID','Nome',  'email','telefone', 'Data', 'Estado','Sobre']

    # criando a tabela
    tree = ttk.Treeview(frame_right, selectmode="extended", columns=tabela_head, show="headings")

    # vertical scrollbar
    vsb = ttk.Scrollbar(frame_right, orient="vertical", command=tree.yview)

    # horizontal scrollbar
    hsb = ttk.Scrollbar( frame_right, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')

    frame_right.grid_rowconfigure(0, weight=12)


    hd=["nw","nw","nw","nw","nw","center","center"]
    h=[30,170,140,100,120,50,100]
    n=0

    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
        # adjust the column's width to the header string
        tree.column(col, width=h[n],anchor=hd[n])
        
        n+=1

    for item in lista:
        tree.insert('', 'end', values=item)

# Chamando a função mostrar
mostrar()

window.mainloop()