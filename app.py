import mysql.connector
from customtkinter import *
from tkinter import messagebox

#Conexão com o Banco
def Conexao():
    try:
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Root",
            database="local"
        )
        return conexao
    except mysql.connector.Error as erro:
        print(f"Error when making connection! {erro}")
        return None
#Armazenando o Resultado da Função Conexão
db = Conexao()

#Função para Cadastrar Usuário
def Cadastro_User():
    if db is not None:
        cursor = db.cursor()
        sql = "INSERT INTO users (name, date, sex) VALUES (%s, %s,  %s)"
        if option_sexo.get() == "Male":
            valores = (digitNome.get(), digitData.get(), "M")
        if option_sexo.get() == "Female":
            valores = (digitNome.get(), digitData.get(), "F")
        
        #Validação dos Dados
        if not digitNome.get():
            messagebox.showerror("Erro", "Name cannot be empty!")
            return
        if len(digitData.get()) != 10 or digitData.get()[4] != '-' or digitData.get()[7] != '-':
            messagebox.showerror("Erro", "Date of Birth must be in YYYY-MM-DD format!")
            return
        
        try:
            cursor.execute(sql, valores)
            db.commit()
            messagebox.showinfo("Sucesso", "User registered successfully!")
        except mysql.connector.Error as erro:
            messagebox.showerror("Erro", f"Failed to register: {erro}")
        finally:
            cursor.close()
            db.close()
    else:
        messagebox.showerror("Erro", "Connection to the bank failed!")

#Iniciando App
App = CTk()

#Config do App
App._set_appearance_mode("light")
App.title("Register")
App.geometry("300x360")
App.resizable(False, False)
App.iconbitmap("icon.ico")

#Centralizar
def CentralizeWindow():
    App.update()
    screenX = App.winfo_screenwidth()
    screenY = App.winfo_screenheight()
    WindowX = App.winfo_width()
    WindowY = App.winfo_height()
    PosX = (screenX//2) - (WindowX//2)
    PosY = (screenY//2) - (WindowY//2)
    App.geometry(f"{WindowX}x{WindowY}+{PosX}+{PosY}")
CentralizeWindow()

#Titulo
Title = CTkLabel(App, text="Register User", text_color="black", font=("Arial", 20), bg_color="#EBEBEB")
Title.pack(pady=10)

#Nome
Name = CTkLabel(App, text="Name:", text_color="black", font=("Arial", 15), bg_color="#EBEBEB", justify="right")
Name.pack(padx=(0, 5), pady=(10, 0))

digitNome = CTkEntry(App, width=200, bg_color="#EBEBEB",fg_color="#ffffff", placeholder_text="Type Here",text_color="black",corner_radius=100)
digitNome.pack(pady=5)


#Data de Nascimento
DataNasc = CTkLabel(App, text="Date of birth:", text_color="black", font=("Arial", 15), bg_color="#EBEBEB", justify="right")
DataNasc.pack(padx=(0, 5), pady=(10, 0))

digitData = CTkEntry(App, width=200,placeholder_text="YYYY-MM-DD",bg_color="#EBEBEB", fg_color="#ffffff",text_color="black",corner_radius=100)
digitData.pack(pady=5)

#Sexo
Sexo = CTkLabel(App, text="Sex:", text_color="black", font=("Arial", 15), bg_color="#EBEBEB", justify="right")
Sexo.pack(padx=(0, 5), pady=(10, 0))

option_sexo = CTkOptionMenu(App, values=["Male", "Female"],bg_color="#EBEBEB")
option_sexo.pack(pady=5)

#Botão
btn_cadastrar = CTkButton(App, text="Register",font=("Arial",17), command=Cadastro_User,height=40,width=100,bg_color="#EBEBEB")
btn_cadastrar.pack(pady=20)

App.mainloop()
