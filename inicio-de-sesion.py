import tkinter as tk
import mysql.connector
from tkinter import messagebox

class VentanaPrincipal:
    def VentanaSecundaria():
        #conecte su base de datos
        conexion = conexion = mysql.connector.connect(
        host="Host",
        user="Usuario",
        password="Contrseña",
        database="Base de datos",
        port='Puerto'
        )
            
        Root = tk.Tk()
        Root.geometry('600x110')
        Root.resizable(0,0)
        Root.config(background='maroon1')
        Root.title('Registro')
        Root.iconbitmap('base-de-datos.ico')

        TextoIngresarNombre = tk.Label(Root,text='Ingresar Nombre',bg='maroon1')
        TextoIngresarNombre.place(x=50,y=5)
        TextoIngresarApellido = tk.Label(Root, text='Ingresar Apellido',bg='maroon1')
        TextoIngresarApellido.place(x=50,y=30)
        TextoIngresarEmail = tk.Label(Root, text='Ingresar Email',bg='maroon1')
        TextoIngresarEmail.place(x=50,y=55)
        TextoIngresarContraseña = tk.Label(Root,text='Ingresar Contraseña',bg='maroon1')
        TextoIngresarContraseña.place(x=50,y=80)

        EntryIgresarNombre = tk.Entry(Root,width=30)
        EntryIgresarNombre.place(x=200,y=5)
        EntryIgresarApellido = tk.Entry(Root,width=30)
        EntryIgresarApellido.place(x=200,y=30)
        EntryIgresarEmail = tk.Entry(Root,width=30)
        EntryIgresarEmail.place(x=200,y=55)
        EntryIgresarContraseña = tk.Entry(Root,width=30,show='*')
        EntryIgresarContraseña.place(x=200, y=80)
        
        cursor = conexion.cursor()
        #Cambia de tabla en mi caso es user y tiene las siguientes secciones (nombre, apellido,email,contraseña)
        InsertarValores ='INSERT INTO user (nombre, apellido, email, contraseña) values (%s,%s,%s,%s)'
        
        
        
        def Acceso():
            valores = (EntryIgresarNombre.get(),EntryIgresarApellido.get(),EntryIgresarEmail.get(),EntryIgresarContraseña.get())   
            if valores == ('','','',''):
                messagebox.showerror('Acceso','Ingrese un valor valido')
                conexion.close()
                Root.destroy()
            if valores == (EntryIgresarNombre.get(),'','',''):
                messagebox.showerror('Acceso','Ingrese un valor valido')
                conexion.close()
                Root.destroy()
            if valores == (EntryIgresarNombre.get(),'','',''):
                messagebox.showerror('Acceso','Ingrese un valor valido')
                conexion.close()
                Root.destroy()
            if valores == (EntryIgresarNombre.get(),EntryIgresarApellido.get(),'',''):
                messagebox.showerror('Acceso','Ingrese un valor valido')
                conexion.close()
                Root.destroy()
            if valores == (EntryIgresarNombre.get(),EntryIgresarApellido.get(),EntryIgresarEmail.get(),''):
                messagebox.showerror('Acceso','Ingrese un valor valido')
                conexion.close()
                Root.destroy()
            if valores == ('',EntryIgresarApellido.get(),'',''):
                messagebox.showerror('Acceso','Ingrese un valor valido')
                conexion.close()
                Root.destroy()
            if valores == ('',EntryIgresarApellido.get(),EntryIgresarEmail.get(),''):
                messagebox.showerror('Acceso','Ingrese un valor valido')
                conexion.close()
                Root.destroy()
            if valores == ('',EntryIgresarApellido.get(),EntryIgresarEmail.get(),EntryIgresarContraseña.get()):
                messagebox.showerror('Acceso','Ingrese un valor valido')
                conexion.close()
                Root.destroy()
            if valores == ('','',EntryIgresarEmail.get(),''):
                messagebox.showerror('Acceso','Ingrese un valor valido')
                conexion.close()
                Root.destroy()
            if valores == ('','',EntryIgresarEmail.get(),EntryIgresarContraseña.get()):
                messagebox.showerror('Acceso','Ingrese un valor valido')
                conexion.close()
                Root.destroy()
            if valores == ('','','',EntryIgresarContraseña.get()):
                messagebox.showerror('Acceso','Ingrese un valor valido')
                conexion.close()
                Root.destroy()
            if valores == (EntryIgresarNombre.get(),'','',EntryIgresarContraseña.get())
                messagebox.showerror('Acceso','Ingrese un valor valido')
                conexion.close()
                Root.destroy()
            cursor.execute(InsertarValores,valores)
            conexion.commit()
            if cursor.rowcount > 0:
                messagebox.showinfo('Registro','Registro completo')
                Root.destroy()

        BotonDeRegistrar = tk.Button(Root,text='Registrar',command=Acceso,font=('arial',12))
        BotonDeRegistrar.place(x=455,y=40)
        Root.mainloop()


    def VentanaTerciaria():
        #conecte su base de datos
        conexion = mysql.connector.connect(
        host="Host",
        user="Usuario",
        password="Contraseña",
        database="Base de datos",
        port='Puerto'
)
        Root = tk.Tk()
        Root.geometry('400x110')
        Root.resizable(0,0)
        Root.config(background='turquoise1')
        Root.title('Inicio de sesion')
        Root.iconbitmap('base-de-datos.ico')
        

        TextoIngresarEmail = tk.Label(Root, text='Ingresar Email',bg='turquoise1')
        TextoIngresarEmail.place(x=50,y=20)
        TextoIngresarContraseña = tk.Label(Root,text='Ingresar Contraseña',bg='turquoise1')
        TextoIngresarContraseña.place(x=50,y=50)

        EntryDeEmail = tk.Entry(Root,width=30)
        EntryDeEmail.place(x=180,y=20)
        EntryDeContraseña = tk.Entry(Root,width=30,show='*')
        EntryDeContraseña.place(x=180,y=50)
        def Acceso():
            cursor = conexion.cursor()
            BusquedaDeEmailYContraseña = "SELECT * FROM user WHERE email = %s AND contraseña = %s"
            valores = (EntryDeEmail.get(), EntryDeContraseña.get())
            cursor.execute(BusquedaDeEmailYContraseña, valores)
            resultado = cursor.fetchone()
            if cursor.rowcount > 0:
                messagebox.showinfo('Inicio de sesion','Felicidades ingresaste')
                Root.destroy()
            else:
                messagebox.showerror('Inicio de sesion','Inicio fallido')
        BotonDeIniciarSesion = tk.Button(Root,text='Iniciar Sesion',command=Acceso)
        BotonDeIniciarSesion.place(x=190,y=80)
    
    Root = tk.Tk()
    Root.config()
    Root.geometry('280x100')
    Root.resizable(0,0)
    Root.config(background='orange2')
    Root.title('Acceso')
    Root.iconbitmap('base-de-datos.ico')
    BotonDeInicioDeSesion = tk.Button(Root,text='Iniciar Sesion',command=VentanaTerciaria,bg='aqua')
    BotonDeInicioDeSesion.place(x=100,y=10)
    BotonDeRegistrar = tk.Button(Root,text='Registrar',command=VentanaSecundaria,bg='aqua')
    BotonDeRegistrar.place(x=110,y=50)
    

    Root.mainloop() 

