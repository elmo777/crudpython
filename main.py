from tkinter import *
from tkinter import ttk
from conexion import *
db = DB()
root = Tk()
root.wm_title("Gestion Estudiantes")
root.geometry("600x500")
nombre=StringVar()
edad=StringVar()
celular=StringVar()
genero=StringVar()

def seleccionfila(event):
     id= listaestudiantes.selection()[0]
     if int(id)>0:
         nombre.set(listaestudiantes.item(id,"values")[1])
         edad.set(listaestudiantes.item(id,"values")[2])
         celular.set(listaestudiantes.item(id,"values")[3])
         genero.set(listaestudiantes.item(id,"values")[4])

marco=LabelFrame(root, text="Lista estudiantes")
marco.place(x=50,y=50, width=500,height=400)
lblNombre=Label(marco,text="Nombre").grid(column=0,row=0,padx=5,pady=5)
txtNombre=Entry(marco,textvariable=nombre)
txtNombre.grid(column=1,row=0)

lblEdad=Label(marco,text="Edad").grid(column=0,row=1,padx=5,pady=5)
txtEdad=Entry(marco,textvariable=edad)
txtEdad.grid(column=1,row=1)

lblCelular=Label(marco,text="Celular").grid(column=2,row=0,padx=5,pady=5)
txtCelular=Entry(marco,textvariable=celular)
txtCelular.grid(column=3,row=0)

lblGenero=Label(marco,text="Genero").grid(column=2,row=1,padx=5,pady=5)
txtGenero=ttk.Combobox(marco,values=["Masculino","Femenino"],textvariable=genero)
txtGenero.grid(column=3,row=1)
txtGenero.current(0)

txtMensaje=Label(marco,text="Lista de estudiantes",fg="Green")
txtMensaje.grid(column=0,row=2,columnspan=4)

listaestudiantes=ttk.Treeview(marco)
listaestudiantes.grid(column=0,row=3,columnspan=4)

listaestudiantes["columns"]=("ID","Nombre","Edad","Celular","Genero",)
listaestudiantes.column("#0",width=0,stretch="FALSE")
listaestudiantes.column("ID", width=50, anchor=CENTER)
listaestudiantes.column("Nombre", width=50, anchor=CENTER)
listaestudiantes.column("Edad", width=50, anchor=CENTER)
listaestudiantes.column("Celular", width=50, anchor=CENTER)
listaestudiantes.column("Genero", width=50, anchor=CENTER) 

listaestudiantes.heading("#0",text="")
listaestudiantes.heading("ID",text="ID", anchor=CENTER)
listaestudiantes.heading("Nombre",text="Nombre", anchor=CENTER)
listaestudiantes.heading("Edad",text="Edad", anchor=CENTER)
listaestudiantes.heading("Celular",text="Celular", anchor=CENTER)
listaestudiantes.heading("Genero",text="Genero", anchor=CENTER)
listaestudiantes.bind("<<TreeviewSelect>>",seleccionfila)

btnEliminar=Button(marco,text="Eliminar",command=lambda:Eliminar())
btnEliminar.grid(column=1,row=4)

btnEditar=Button(marco,text="Editar",command=lambda:Editar())
btnEditar.grid(column=2,row=4)

btnNuevo=Button(marco,text="Nuevo",command=lambda:Nuevo())
btnNuevo.grid(column=3,row=4)



def validar():
     return len(nombre.get()) and len(edad.get()) and len(celular.get()) 
          
def limpiar():
     nombre.set("")
     edad.set("")
     celular.set("")
     
def vaciar():
        filas = listaestudiantes.get_children()
        for fila in filas:
            listaestudiantes.delete(fila)
def llenar():
    vaciar() 
    sql="select * from estudiantes"
    db.cursor.execute(sql)
    filas=db.cursor.fetchall()
    for fila in filas:
         id= fila[0]
         listaestudiantes.insert("", END,id,text=id ,values=fila)

           
def Nuevo():
    
        if validar():
         val=(nombre.get(),edad.get(),celular.get(),genero.get())
         sql="insert into estudiantes(nombre,edad,celular,genero) values(%s,%s,%s,%s)"
         db.cursor.execute(sql,val)
         db.conexion.commit()
         txtMensaje.config(text="Se guardo mi pana",fg="Green")
         llenar()
         limpiar()
        else:
         txtMensaje.config(text= "No debe estar vacio",fg="Green")
   

def Editar():
    if validar():
         id= listaestudiantes.selection()[0]
         val=(nombre.get(),edad.get(),celular.get(),genero.get(),id)
         sql = "UPDATE estudiantes SET nombre=%s,edad=%s,celular=%s,genero=%s WHERE id=%s"
         db.cursor.execute(sql,val)
         db.conexion.commit()
         txtMensaje.config(text="Se guardo mi pana",fg="Green")
         llenar()
         limpiar()
    
    
def Eliminar():
    id= listaestudiantes.selection()[0]
    if int(id)>0:
         sql="delete from estudiantes where id="+id
         db.cursor.execute(sql)
         db.conexion.commit()
         listaestudiantes.delete(id)
         txtMensaje.config(text= "Se ha eliminado con exito")
    else:
         txtMensaje.config(text= "Usted es una weba")     
llenar()
root.mainloop()