from ast import Continue, Pass
from tkinter import *
from random import randint


raiz=Tk()
raiz.title('Muertos y heridos múltiples modalidades')
raiz.config (bg="#006400")
raiz.geometry()

modoelegido=IntVar()
manualauto=IntVar()
cortar=False
noentrar=False
manualauto.set(2)
modoelegido.set(1)
digitosdefecto=IntVar()
intentosdefecto=IntVar()
digitosdefecto.set(4)
intentosdefecto.set(14)


frame=Frame(raiz, background="#004300")
frame.pack(fill="both", expand=True)
frame.grid_columnconfigure(0, weight=1)
frame.grid_columnconfigure(1, weight=1)
frame.grid_columnconfigure(2, weight=1)
frame.grid_columnconfigure(3, weight=1)
frame.grid_rowconfigure(0, weight=0)
frame.grid_rowconfigure(1, weight=0)
frame.grid_rowconfigure(2, weight=0)
frame.grid_rowconfigure(3, weight=0)
frame.grid_rowconfigure(4, weight=0)
frame.grid_rowconfigure(5, weight=0)
frame.grid_rowconfigure(6, weight=1)
frame.grid_rowconfigure(7, weight=1)
frame.grid_rowconfigure(8, weight=1)
frame.grid_rowconfigure(9, weight=1)
frame.grid_rowconfigure(10, weight=1)
frame.grid_rowconfigure(11, weight=1)
frame.grid_rowconfigure(12, weight=1)
frame.grid_rowconfigure(13, weight=1)
frame.grid_rowconfigure(14, weight=1)
frame.grid_rowconfigure(15, weight=1)


cabeceraframe=Frame(frame, background="#006400")
cabeceraframe.grid(row=0, column=0, rowspan=4, columnspan=4, sticky="nsew", padx=5, pady=5)
cabeceraframe.grid_columnconfigure(0, weight=1)
cabeceraframe.grid_columnconfigure(1, weight=1)
cabeceraframe.grid_columnconfigure(2, weight=2)
cabeceraframe.grid_columnconfigure(3, weight=2)
cabeceraframe.grid_rowconfigure(0, weight=1)
cabeceraframe.grid_rowconfigure(1, weight=1)
cabeceraframe.grid_rowconfigure(2, weight=0)
cabeceraframe.grid_rowconfigure(3, weight=1)


tituloframe=Frame(cabeceraframe, background="#88ff88")
tituloframe.grid(row=0, column=0, columnspan=2, rowspan=4, sticky="nsew", padx=0, pady=0)
tituloframe.grid_columnconfigure(0, weight=1)
tituloframe.grid_columnconfigure(1, weight=1)
tituloframe.grid_rowconfigure(0, weight=1)
tituloframe.grid_rowconfigure(1, weight=0)
tituloframe.grid_rowconfigure(2, weight=0)



titulolabel=Label(tituloframe, background="#54ADEB", text="MUERTOS Y HERIDOS", font=("",28))
titulolabel.grid(row=0, column=0, columnspan=2, pady=0, sticky="nsew")
fondojugadorlabel=Label(tituloframe, background="#BBDDEC")
fondojugadorlabel.grid(row=2, column=0, columnspan=2, pady=0, sticky="nsew")
jugadorlabel=Label(tituloframe, background="#BBDDEC", text="Nombre del jugador:", font=("",14))
jugadorlabel.grid(row=2, column=0, pady=3, sticky="nse")
jugadorentry=Entry(tituloframe, background="#DCDDFF", font=("",11))
jugadorentry.grid(row=2, column=1, padx=3, pady=3, sticky="nsew")
titulobotoninicio=Button(tituloframe, relief=GROOVE, bd=5, padx=0, pady=0, background="#EF8023", command=lambda:nuevojuego(), text="NUEVO JUEGO", font=("",18), )
titulobotoninicio.grid (row=1, column=1, sticky="nsew", padx=10, pady=7)
titulobotonsalir=Button(tituloframe, relief=GROOVE, bd=5, padx=0, pady=0, background="#E4E024", command=lambda:salir(), text="Mostrar número \n y acabar", font=("",15), )
titulobotonsalir.grid (row=1, column=0, padx=20, pady=7)

respuestaframe=Frame(cabeceraframe, background="#006400")
respuestaframe.grid(row=0, column=2, columnspan=2, rowspan=4, sticky="nsew", padx=5, pady=0)
respuestaframe.grid_columnconfigure(0, weight=1)
respuestaframe.grid_rowconfigure(0, weight=1)
respuestaframe.grid_rowconfigure(1, weight=1)
respuestaframe.grid_rowconfigure(2, weight=0)
respuestaframe.grid_rowconfigure(3, weight=1)

respuestalabel=Label(respuestaframe, background="#69F464", text="ESCRIBE UN NÚMERO", font= ("",23) )
respuestalabel.grid(row=0, column=0, columnspan=1, sticky="sew")
respuestaentry=Entry(respuestaframe, justify=CENTER, font= ("",25) )
respuestaentry.grid(row=1, column=0, columnspan=1, sticky="nsew", padx=10, pady=2)

labelrespuestaboton=Label(respuestaframe, bd=10,background="#46fbff")
labelrespuestaboton.grid(row=2, column=0,columnspan=1, padx=10, pady=0, sticky="nsew")
respuestaboton=Button(respuestaframe, relief=GROOVE, bd=10, padx=0, pady=0, background="red", command=lambda:pulsar(), text="   Pulsa   ", font= ("",20) )
respuestaboton.grid(row=2, column=0,columnspan=1)


respuestadialogo=Label(respuestaframe, background="#95ff7f", font= ("",19), width=20)
respuestadialogo.grid(row=3, column=0, columnspan=1, sticky="nsew", padx=10, pady=2)

informacionframe=Frame(frame, background="green")
informacionframe.grid(row=4, column=2, columnspan=2, rowspan=12, sticky="nsew", padx=2, pady=2)
informacionframe.grid_columnconfigure(0, weight=1)
informacionframe.grid_columnconfigure(1, weight=1)
informacionframe.grid_columnconfigure(2, weight=1)
informacionframe.grid_columnconfigure(3, weight=1)
informacionframe.grid_rowconfigure(4, weight=1)
informacionframe.grid_rowconfigure(5, weight=1)
informacionframe.grid_rowconfigure(6, weight=1)
informacionframe.grid_rowconfigure(7, weight=1)
informacionframe.grid_rowconfigure(8, weight=1)
informacionframe.grid_rowconfigure(9, weight=1)
informacionframe.grid_rowconfigure(10, weight=1)
informacionframe.grid_rowconfigure(11, weight=1)
informacionframe.grid_rowconfigure(12, weight=1)
informacionframe.grid_rowconfigure(13, weight=1)
informacionframe.grid_rowconfigure(14, weight=1)
informacionframe.grid_rowconfigure(15, weight=1)

informacionencabezado1=Label(informacionframe, background="brown", text="Números", font= ("",17), width=9)
informacionencabezado1.grid(row=4, column=0, sticky="nsew")
informacionencabezado2=Label(informacionframe, background="brown", text="Muertos", font= ("",17), width=9)
informacionencabezado2.grid(row=4, column=1,  sticky="nsew")
informacionencabezado3=Label(informacionframe, background="brown", text="Heridos", font= ("",17), width=9)
informacionencabezado3.grid(row=4, column=2, sticky="nsew")
informacionencabezado4=Label(informacionframe, background="brown", text="Intentos", font= ("",17), width=9)
informacionencabezado4.grid(row=4, column=3, sticky="nsew")
informacioninfo1=Listbox (informacionframe, background= "#c0f0ca", font= ("",16), width=9, borderwidth=0, highlightthickness=0, justify="center")
informacioninfo1.grid(row=5, column=0, rowspan=11, columnspan=1, sticky="nsew")
informacioninfo2=Listbox (informacionframe, background= "#c0f0ca", font= ("",16), width=9, borderwidth=0, highlightthickness=0, justify="center")
informacioninfo2.grid(row=5, column=1, rowspan=11, columnspan=1, sticky="nsew")
informacioninfo3=Listbox (informacionframe, background= "#c0f0ca", font= ("",16), width=9, borderwidth=0, highlightthickness=0, justify="center")
informacioninfo3.grid(row=5, column=2, rowspan=11, columnspan=1, sticky="nsew")
informacioninfo4=Listbox (informacionframe, background= "#c0f0ca", font= ("",16), width=9, borderwidth=0, highlightthickness=0, justify="center")
informacioninfo4.grid(row=5, column=3, rowspan=11, columnspan=1, sticky="nsew")


seleccionframe=Frame(frame, background="#9ff8ff")
seleccionframe.grid(row=4, column=0, rowspan=6, columnspan=2, sticky="nsew", padx=2, pady=2)
seleccionframe.grid_rowconfigure(0, weight=0)
seleccionframe.grid_rowconfigure(1, weight=0)
seleccionframe.grid_rowconfigure(2, weight=1)
seleccionframe.grid_rowconfigure(3, weight=1)
seleccionframe.grid_rowconfigure(4, weight=1)
seleccionframe.grid_rowconfigure(5, weight=1)
seleccionframe.grid_rowconfigure(6, weight=1)
seleccionframe.grid_rowconfigure(7, weight=1)
seleccionframe.grid_rowconfigure(8, weight=1)
seleccionframe.grid_rowconfigure(9, weight=1)
seleccionframe.grid_rowconfigure(10, weight=1)
seleccionframe.grid_columnconfigure(0, weight=0)
seleccionframe.grid_columnconfigure(1, weight=1)
seleccionframe.grid_columnconfigure(2, weight=1)
seleccionframe.grid_columnconfigure(3, weight=1)

seleccionnumerolabel=Label(seleccionframe, text='''Selección 
de solución''', font=("",12), background="#9ff8ff")
seleccionnumerolabel.grid(row=0, column=0, rowspan= 2,sticky="nsew", padx=4, pady=0)
manualradiobutton=Radiobutton(seleccionframe, text="Manual", justify="left", variable=manualauto, value=1, command=lambda:mostrarautoradiobutton(), background="#9ff8ff")
manualradiobutton.grid(row=0, column=1, sticky="nsw", padx=0, pady=0)
automaticoradiobutton=Radiobutton(seleccionframe, text="Automático", justify="left", variable=manualauto, value=2, command=lambda:ocultarautoradiobutton(), background="#9ff8ff")
automaticoradiobutton.grid(row=1, column=1, sticky="nsw", padx=0, pady=0)

eligenumerosolucionlabel=Label(seleccionframe, background="#9ff8ff", fg="#7A9598", text="Elige número:", font=("",13))
eligenumerosolucionlabel.grid(row=2, column=0, rowspan=2, pady=3, sticky="nsw")
eligenumerosolucionentry=Entry (seleccionframe, background="#FFFFFF", state="disable", font=("",11), fg="black", disabledforeground="#9ff8ff", disabledbackground="#9ff8ff")
eligenumerosolucionentry.grid(row=2, column=1, rowspan=2, padx=3, pady=3, sticky="nsew")

digitoslabel=Label(seleccionframe, text="Número de dígitos", font=("",14), background="#9ff8ff")
digitoslabel.grid(row=0, rowspan= 2, column=2, sticky="nsw", padx=0, pady=0)
digitosentry=Entry(seleccionframe, justify="center", textvariable=digitosdefecto, font=("",15), width=5)
digitosentry.grid(row=0, rowspan=2, column=3, sticky="w", padx=3, pady=2)

intentoslabel=Label(seleccionframe, text="Número de intentos", font=("",14), background="#9ff8ff")
intentoslabel.grid(row=2, column=2, sticky="nsw", padx=0, pady=0)
intentosentry=Entry(seleccionframe, justify="center", textvariable=intentosdefecto, font=("",15), width=5)
intentosentry.grid(row=2, column=3, rowspan=2, sticky="w", padx=3, pady=0)


fondomodolabel=Label(seleccionframe,background="#f0f0f0")
fondomodolabel.grid(row=4, column=0, columnspan=4, rowspan=7, sticky="nsew", padx=0, pady=0)
modolabel=Label(seleccionframe, text="Elige modo de juego", font=("",14))
modolabel.grid(row=4, column=0, rowspan=7, columnspan=2, sticky="ns", padx=0, pady=0)
modoradiobutton1=Radiobutton(seleccionframe, text="Sin repetición", justify="left", variable=modoelegido, value=1)
modoradiobutton1.grid(row=4, column=2, columnspan=2, sticky="w", padx=0, pady=0)
modoradiobutton2=Radiobutton(seleccionframe, text="Repetición uno solo", variable=modoelegido, value=2)
modoradiobutton2.grid(row=5, column=2, columnspan=2, sticky="w", padx=0, pady=0)
modoradiobutton3=Radiobutton(seleccionframe, text="Repetición uno solo cada efecto", variable=modoelegido, value=3)
modoradiobutton3.grid(row=6, column=2, columnspan=2, sticky="w", padx=0, pady=0)
modoradiobutton4=Radiobutton(seleccionframe, text="Repetición uno a uno", variable=modoelegido, value=4)
modoradiobutton4.grid(row=7, column=2, columnspan=2, sticky="w", padx=0, pady=0)
modoradiobutton5=Radiobutton(seleccionframe, text="Repetición uno a todos", variable=modoelegido, value=5)
modoradiobutton5.grid(row=8, column=2, columnspan=2, sticky="w", padx=0, pady=0)
modoradiobutton6=Radiobutton(seleccionframe, text="Repetición todos a uno", variable=modoelegido, value=6)
modoradiobutton6.grid(row=9, column=2, columnspan=2, sticky="w", padx=0, pady=0)
modoradiobutton7=Radiobutton(seleccionframe, text="Repetición todos a todos", variable=modoelegido, value=7)
modoradiobutton7.grid(row=10, column=2, columnspan=2, sticky="w", padx=0, pady=0)


instruccionesframe=Frame(frame, background="yellow")
instruccionesframe.grid(row=10, column=0, rowspan=6, columnspan=2, sticky="nsew", padx=2, pady=2)
instruccionesframe.grid_columnconfigure(0, weight=1)
instruccionesframe.grid_rowconfigure(0, weight=1)
instruccioneslabel=Label(instruccionesframe, background="lightblue", justify="left", anchor="nw", font=("",11), text='''Hay que adivinar el número solución.
SIEMPRE que un dígito coincida en valor (cifra) y posición, suma un 
muerto (M) por cada coincidencia.
Los que coincidan en cifra pero no en posición, sumarán
un herido (H), ninguno o varios, según el modo elegido.
Sin repetición: No hay cifras repetidas en la solución.
Repetición uno solo: Una cifra solo suma 1 H. Si esa
cifra ya sumó muertos (M), no suma heridos (H).
Repetición uno solo cada efecto: Igual pero sí suma 1 H
aunque también haya sumado muertos (M).
Repetición uno a uno: Se suma un herido por cada
repetición en solución e intento (descontando muertos).
Repetición uno a todos: Cada cifra de intento afecta a 
todas en solución. Estas solo se hieren o mueren una vez.
Repetición todos a uno: Cada dígito de solución puede
ser muerto y herido por todos los de intento. Pero los
de intento solo pueden herir o matar a uno de solución.
Repetición todos a todos: Toda coincindencia suma.''')

instruccioneslabel.grid(row=0, column=0, sticky="nsew", padx=0, pady=0)

muertos=None
heridos=None
intento=None
intentos=0
cantidad=None


def ocultarautoradiobutton():
    #eligenumerosolucionentry.config(fg="#9ff8ff", bg="#FFFFFF", disabledforeground="#9ff8ff", disabledbackground="#9ff8ff")
    eligenumerosolucionentry["state"]="disable"
    eligenumerosolucionlabel.config(fg="#7A9598")


def mostrarautoradiobutton():
    eligenumerosolucionlabel.config(fg="#000000")
    eligenumerosolucionentry["state"]="normal"



def nuevojuegosin():

    global intentos
    global muertos
    global heridos
    global solucion
    global intento
    global lista
    global pantalla21
    global pantalla22
    global pantalla23
    global pantalla24
    global intentoselegidos
    global cantidad
    global cortar
    global manualauto
    global respuestadialogo
    global manu
    
    if manu==1:

        solucion=eligenumerosolucionentry.get()
        repite=False
        comprobacion=[]
        for i in solucion:
            if i in comprobacion:
                repite=True
            comprobacion.append(i)

        if cantidad>10:
            respuestadialogo['text'] ="Sin repetición elige menos de 11 dígitos"
            cortar==True
            noentrar=True
        elif len(solucion)!=cantidad:
            respuestadialogo['text'] =(f"Elige un valor solución de {cantidad} dígitos")
            cortar=True
            noentrar=True
        elif solucion.isdigit()==False:
            respuestadialogo['text']="Elige un valor solución correcto"
            cortar=True
            noentrar=True
        elif repite==True:
            respuestadialogo['text'] =(f"No repitas dígitos en esta opción")
            cortar=True
            noentrar==True
        else:
            respuestadialogo["text"]="Jugando. Llevas 0 intentos"

    elif manu==2:

        if cantidad>10:
            respuestadialogo["text"]="Sin repetición elige menos de 11 dígitos"
            cortar=True
            noentrar=True
        else:
            digitos=[]
            for i in range (cantidad):
                digito=randint(0,9)
                while digito in digitos:
                    digito=randint(0,9)
                digitos.append(digito)
            solucion="".join(map(str,digitos))
            respuestadialogo["text"]="Jugando. Llevas 0 intentos"

    else:
        respuestadialogo['text'] ="Selecciona manual/automático"
        cortar=True
        noentrar=True
        

    intentos=0
    muertos=0
    heridos=0
    lista=[]
    pantalla21=[]
    pantalla22=[]
    pantalla23=[]
    pantalla24=[]
    
    
    informacioninfo1.delete (0,informacioninfo1.size())
    informacioninfo2.delete (0,informacioninfo2.size())
    informacioninfo3.delete (0,informacioninfo3.size())
    informacioninfo4.delete (0,informacioninfo4.size())
    eligenumerosolucionentry.delete(0,"end")


def nuevojuego():

    global cortar
    cortar=False
    global noentrar
    noentrar=False
    respuestaentry.delete(0,"end")
    global modoel
    global cantidad
    global intentoselegidos
    global manualauto
    global manu
    


    if manualauto.get() == 1:
        manu=1
    elif manualauto.get() == 2:
        manu=2
    else:
        respuestadialogo['text']="Elige manual o automático"
        manu=0



    if modoelegido.get()==1:
        modoel=1
    elif modoelegido.get()==2:
        modoel=2
    elif modoelegido.get()==3:
        modoel=3
    elif modoelegido.get()==4:
        modoel=4
    elif modoelegido.get()==5:
        modoel=5
    elif modoelegido.get()==6:
        modoel=6
    elif modoelegido.get()==7:
        modoel=7
    else:
        respuestadialogo['text']="Elige un modo de juego"
        noentrar=True


    if intentosentry.get().isdigit()==False or digitosentry.get().isdigit()==False:
        respuestadialogo['text']="Elige intentos y dígitos correctos"
        cortar=True
        noentrar=True
    
    elif (modoelegido.get()!=1 and modoelegido.get()!=2 and modoelegido.get()!=3 and modoelegido.get()!=4 and modoelegido.get()!=5 and modoelegido.get()!=6 and modoelegido.get()!=7):
        respuestadialogo['text'] ="Rellena los datos"
        cortar=True
        noentrar=True

    elif manu!=1 and manu!=2:
        respuestadialogo['text']="Selecciona manual/automático"
        cortar=True
        noentrar=True

    elif int(intentosentry.get())<1:
        respuestadialogo['text']="Elige un número de intentos válido"
        cortar=True
        noentrar=True

    elif int(digitosentry.get())<1:
        respuestadialogo['text']="Elige un número de dígitos válido"
        cortar=True
        noentrar=True

    else:
        intentoselegidos=IntVar()
        intentoselegidos=int(intentosentry.get())
        cantidad=IntVar()
        cantidad=int(digitosentry.get())

        if modoel==1:
            nuevojuegosin()
        elif modoel==2:
            nuevojuegocon()
        elif modoel==3:
            nuevojuegocon()
        elif modoel==4:
            nuevojuegocon()
        elif modoel==5:
            nuevojuegocon()
        elif modoel==6:
            nuevojuegocon()
        elif modoel==7:
            nuevojuegocon()
        else:
            respuestadialogo['text']="Elige un modo de juego"
            noentrar=True

    #if (modoel!=1 and modoel!=2 and modoel!=3  and modoel!=4  and modoel!=5  and modoel!=6  and modoel!=7) or (manu!=1 and manu!=2)

def nuevojuegocon():

    global intentos
    global muertos
    global heridos
    global solucion
    global intento
    global lista
    global pantalla21
    global pantalla22
    global pantalla23
    global pantalla24
    global intentoselegidos
    global cantidad
    global cortar
    global manualauto
    global respuestadialogo
    global manu
    global noentrar

    if manu==1:
        solucion=eligenumerosolucionentry.get()

        if cantidad != len(solucion):
            respuestadialogo['text']=f"Elige un valor solución de {cantidad} dígitos"
            cortar=True
            noentrar=True
        
        elif solucion.isdigit()==False:
            respuestadialogo['text']="Elige un valor solución correcto"
            cortar=True
            noentrar=True
        else:
            respuestadialogo["text"]="Jugando. Llevas 0 intentos"

    elif manu==2:
        digitos=[]
        for i in range (cantidad):
            digito=randint(0,9)
            digitos.append(digito)
        solucion="".join(map(str,digitos))
        respuestadialogo["text"]="Jugando. Llevas 0 intentos"

    else:
        respuestadialogo['text']="Selecciona manual/automático"
        cortar=True
        noentrar=True


    intentos=0
    muertos=0
    heridos=0
    lista=[]
    pantalla21=[]
    pantalla22=[]
    pantalla23=[]
    pantalla24=[]
    
    
    informacioninfo1.delete (0,informacioninfo1.size())
    informacioninfo2.delete (0,informacioninfo2.size())
    informacioninfo3.delete (0,informacioninfo3.size())
    informacioninfo4.delete (0,informacioninfo4.size())
    eligenumerosolucionentry.delete(0,"end")


def pulsar():

    global solucion
    global modoel
    global manu
    global solucion
    global cortar
    global noentrar

    if cantidad==None or intentoselegidos==None or solucion==None or len(solucion)!=cantidad or solucion.isdigit()==False or (modoel!=1 and modoel!=2 and modoel!=3 and modoel!=4 and modoel!=5 and modoel!=6 and modoel!=7):
        respuestadialogo['text']="Rellena los datos y pulsa nuevo juego"
        cortar=True

    elif manu!=1 and manu!=2:
        respuestadialogo['text']="Selecciona manual/automático"
        cortar=True

    if noentrar==True:
        respuestadialogo['text']="Elige datos correctos y pulsa nuevo juego"
        cortar=True


    else:
        if manu==1:
            if solucion==None or solucion.isdigit()==False:
                respuestadialogo['text']=f"Rellena las opciones necesarias"
                cortar=True

            elif cantidad!=len(solucion):
                respuestadialogo['text']=f"Elige un número de {cantidad} dígitos"
                cortar=True
            
            elif solucion.isdigit()==False:
                respuestadialogo['text']="Introduce solo números"
                cortar=True
            else:
                if modoel==1:
                    disparar1()
                elif modoel==2:
                    disparar2()
                elif modoel==3:
                    disparar3()
                elif modoel==4:
                    disparar4()
                elif modoel==5:
                    disparar5()
                elif modoel==6:
                    disparar6()
                elif modoel==7:
                    disparar7()
                else:
                    respuestadialogo['text']="Elige un modo de juego"

        elif manu==2:
            if modoel==1:
                disparar1()
            elif modoel==2:
                disparar2()
            elif modoel==3:
                disparar3()
            elif modoel==4:
                disparar4()
            elif modoel==5:
                disparar5()
            elif modoel==6:
                disparar6()
            elif modoel==7:
                disparar7()
            else:
                respuestadialogo['text']="Elige un modo de juego"

        else:
            respuestadialogo['text']="Selecciona manual/automático"
            cortar=True

    

def disparar1(): #sin repetición
    global intentos
    global intentoselegidos
    global cortar
    global muertos
    global heridos
    global solucion
    global intento
    global cantidad
    intentos +=1
    if cortar==True:
        respuestadialogo['text'] ="Pulsa nuevo juego"
    else:

        muertos=0
        heridos=0
        intento=respuestaentry.get()
        repite=False
        comprobacion=[]
        for i in intento:
            if i in comprobacion:
                repite=True
            comprobacion.append(i)
        
        if intento.isdigit()==False:
            respuestadialogo['text'] ="Mete solo números"
            intentos-=1
        elif len(intento)!=cantidad:
            respuestadialogo['text']= (f"Mete {cantidad} dígitos, no más ni menos")
            intentos-=1
        elif repite==True:
            respuestadialogo['text'] ="No metas dígitos repetidos"
            intentos-=1

        else:
            respuestadialogo["text"]=(f"Jugando. Llevas {intentos} intentos")
            for i in intento:
                for j in solucion:
                    if i == j:
                        heridos+=1
            for i in range(cantidad):
                if intento[i] == solucion [i]:
                    muertos+=1
                    heridos-=1
            if heridos<0:
                heridos=0
            
            lista =[intento, muertos, heridos]
            
            for i in range(intentos):
                pantalla11=f"{lista[0]}"
                pantalla12=f"{lista[1]}"
                pantalla13=f"{lista[2]}"
                pantalla14=f"{intentos} intentos"
                pantalla21=[]
                pantalla22=[]
                pantalla23=[]
                pantalla24=[]
                pantalla21.append(pantalla11)
                pantalla22.append(pantalla12)
                pantalla23.append(pantalla13)
                pantalla24.append(pantalla14)

            informacioninfo1.insert(0,*pantalla21)
            informacioninfo2.insert(0,*pantalla22)
            informacioninfo3.insert(0,*pantalla23)
            informacioninfo4.insert(0,*pantalla24)
            
            if muertos == cantidad:
                
                pantalla21=[]
                pantalla22=[]
                pantalla23=[]
                pantalla24=[]
                respuestadialogo["text"]="Ganaste"
                pantalla21.append("Ganaste")
                pantalla22.append((f" {intentos} " ))
                pantalla23.append("intentos")
                pantalla24.append("")

                
                informacioninfo1.insert(0,*pantalla21)
                informacioninfo2.insert(0,*pantalla22)
                informacioninfo3.insert(0,*pantalla23)
                informacioninfo4.insert(0,*pantalla24)
                cortar=True

            else:
                if intentos<intentoselegidos:
                    Continue
                else:
                    respuestadialogo["text"]=f"{intentos} fallos. Perdiste. Sol: {solucion}"
                    cortar=True
            
            
        respuestaentry.delete (0,"end")


def disparar2(): #uno solo
    global intentos
    global intentoselegidos
    global cortar
    global muertos
    global heridos
    global solucion
    global intento
    global cantidad
    intentos +=1
    if cortar==True:
        respuestadialogo['text'] ="Pulsa nuevo juego"
    else:

        muertos=0
        heridos=0
        intento=respuestaentry.get()
        if intento.isdigit()==False:
            respuestadialogo['text'] ="Mete solo números"
            intentos-=1
        elif len(intento)!=cantidad:
            respuestadialogo['text']= (f"Mete {cantidad} dígitos, no más ni menos")
            intentos-=1
        
        else:
            respuestadialogo["text"]=(f"Jugando. Llevas {intentos} intentos")
            listacoincidencias=[]
            for i in intento:
                for j in solucion:
                    if i==j:
                        if j in listacoincidencias:
                            pass
                        else:
                            listacoincidencias.append(j)
                    else:
                        pass
            heridos=len(listacoincidencias)
            for i in range (len(intento)):
                if intento[i]==solucion[i]:
                    muertos+=1
                    heridos-=1
            if heridos<0:
                heridos=0

            lista =[intento, muertos, heridos]
            

            for i in range(intentos):
                pantalla11=f"{lista[0]}"
                pantalla12=f"{lista[1]}"
                pantalla13=f"{lista[2]}"
                pantalla14=f"{intentos} intentos"
                pantalla21=[]
                pantalla22=[]
                pantalla23=[]
                pantalla24=[]
                pantalla21.append(pantalla11)
                pantalla22.append(pantalla12)
                pantalla23.append(pantalla13)
                pantalla24.append(pantalla14)

            informacioninfo1.insert(0,*pantalla21)
            informacioninfo2.insert(0,*pantalla22)
            informacioninfo3.insert(0,*pantalla23)
            informacioninfo4.insert(0,*pantalla24)
            
            if muertos == cantidad:
                
                pantalla21=[]
                pantalla22=[]
                pantalla23=[]
                pantalla24=[]
                respuestadialogo["text"]="Ganaste"
                pantalla21.append("Ganaste")
                pantalla22.append((f" {intentos} " ))
                pantalla23.append("intentos")
                pantalla24.append("")

                
                informacioninfo1.insert(0,*pantalla21)
                informacioninfo2.insert(0,*pantalla22)
                informacioninfo3.insert(0,*pantalla23)
                informacioninfo4.insert(0,*pantalla24)
                cortar=True

            else:
                if intentos<intentoselegidos:
                    Continue
                else:
                    respuestadialogo["text"]=f"{intentos} fallos. Perdiste. Sol: {solucion}"
                    cortar=True
        
        respuestaentry.delete (0,"end")



def disparar3(): #uno solo cada efecto
    global intentos
    global intentoselegidos
    global cortar
    global muertos
    global heridos
    global solucion
    global intento
    global cantidad
    intentos +=1
    if cortar==True:
        respuestadialogo['text'] ="Pulsa nuevo juego"
    else:

        muertos=0
        heridos=0
        intento=respuestaentry.get()
        if intento.isdigit()==False:
            respuestadialogo['text'] ="Mete solo números"
            intentos-=1
        elif len(intento)!=cantidad:
            respuestadialogo['text']= (f"Mete {cantidad} dígitos, no más ni menos")
            intentos-=1
        

        else:
            respuestadialogo["text"]=(f"Jugando. Llevas {intentos} intentos")
            listacoincidencias3=[]  
            intentocopia=intento
            solucioncopia=solucion
            intentosinmuertos=list(intentocopia)
            solucionsinmuertos=list(solucioncopia)
            for i in range (len(intentosinmuertos)-1,-1,-1):
                if intento[i]==solucion[i]:
                    muertos+=1
                    del intentosinmuertos[i]
                    del solucionsinmuertos[i]
            
            for i in intentosinmuertos:
                for j in solucionsinmuertos:
                    if i==j:
                        if j in listacoincidencias3:
                            pass
                        else:
                            listacoincidencias3.append(j)
                    else:
                        pass
            heridos=len(listacoincidencias3)  

            lista =[intento, muertos, heridos]
            

            for i in range(intentos):
                pantalla11=f"{lista[0]}"
                pantalla12=f"{lista[1]}"
                pantalla13=f"{lista[2]}"
                pantalla14=f"{intentos} intentos"
                pantalla21=[]
                pantalla22=[]
                pantalla23=[]
                pantalla24=[]
                pantalla21.append(pantalla11)
                pantalla22.append(pantalla12)
                pantalla23.append(pantalla13)
                pantalla24.append(pantalla14)

            informacioninfo1.insert(0,*pantalla21)
            informacioninfo2.insert(0,*pantalla22)
            informacioninfo3.insert(0,*pantalla23)
            informacioninfo4.insert(0,*pantalla24)
            
            if muertos == cantidad:
                
                pantalla21=[]
                pantalla22=[]
                pantalla23=[]
                pantalla24=[]
                respuestadialogo["text"]="Ganaste"
                pantalla21.append("Ganaste")
                pantalla22.append((f" {intentos} " ))
                pantalla23.append("intentos")
                pantalla24.append("")

                
                informacioninfo1.insert(0,*pantalla21)
                informacioninfo2.insert(0,*pantalla22)
                informacioninfo3.insert(0,*pantalla23)
                informacioninfo4.insert(0,*pantalla24)
                cortar=True

            else:
                if intentos<intentoselegidos:
                    Continue
                else:
                    respuestadialogo["text"]=f"{intentos} fallos. Perdiste. Sol: {solucion}"
                    cortar=True
        
        respuestaentry.delete (0,"end")              
            

def disparar4(): #uno a uno
    global intentos
    global intentoselegidos
    global cortar
    global muertos
    global heridos
    global solucion
    global intento
    global cantidad
    intentos +=1
    if cortar==True:
        respuestadialogo['text'] ="Pulsa nuevo juego"
    else:
 
        muertos=0
        heridos=0
        intento=respuestaentry.get()
        if intento.isdigit()==False:
            respuestadialogo['text'] ="Mete solo números"
            intentos-=1
        elif len(intento)!=cantidad:
            respuestadialogo['text']= (f"Mete {cantidad} dígitos, no más ni menos")
            intentos-=1

        else:
            respuestadialogo["text"]=(f"Jugando. Llevas {intentos} intentos")

            listacoincidencias=[]
            for i in intento:
                for j in solucion:
                    if i==j:
                        if j in listacoincidencias:
                            pass
                        else:
                            listacoincidencias.append(j)
                    else:
                        pass
            cantidadjintento=0
            cantidadksolucion=0
            for i in listacoincidencias:
                for j in intento:
                    if j==i:
                        cantidadjintento+=1
                for k in solucion:
                    if k==i:
                        cantidadksolucion+=1
                if cantidadjintento<cantidadksolucion:
                    heridos+=cantidadjintento
                else:
                    heridos+=cantidadksolucion
                cantidadjintento=0
                cantidadksolucion=0

            for i in range(cantidad):
                if intento[i] == solucion [i]:
                    muertos+=1
                    heridos-=1
            if heridos<0:
                heridos=0
            lista =[intento, muertos, heridos]
            
            for i in range(intentos):
                pantalla11=f"{lista[0]}"
                pantalla12=f"{lista[1]}"
                pantalla13=f"{lista[2]}"
                pantalla14=f"{intentos} intentos"
                pantalla21=[]
                pantalla22=[]
                pantalla23=[]
                pantalla24=[]
                pantalla21.append(pantalla11)
                pantalla22.append(pantalla12)
                pantalla23.append(pantalla13)
                pantalla24.append(pantalla14)

            informacioninfo1.insert(0,*pantalla21)
            informacioninfo2.insert(0,*pantalla22)
            informacioninfo3.insert(0,*pantalla23)
            informacioninfo4.insert(0,*pantalla24)
            
            if muertos == cantidad:
                
                pantalla21=[]
                pantalla22=[]
                pantalla23=[]
                pantalla24=[]
                respuestadialogo["text"]="Ganaste"
                pantalla21.append("Ganaste")
                pantalla22.append((f" {intentos} " ))
                pantalla23.append("intentos")
                pantalla24.append("")

                
                informacioninfo1.insert(0,*pantalla21)
                informacioninfo2.insert(0,*pantalla22)
                informacioninfo3.insert(0,*pantalla23)
                informacioninfo4.insert(0,*pantalla24)
                cortar=True

            else:
                if intentos<intentoselegidos:
                    Continue
                else:
                    respuestadialogo["text"]=f"{intentos} fallos. Perdiste. Sol: {solucion}"
                    cortar=True
        
        respuestaentry.delete (0,"end")                


def disparar5(): #uno a todos
    global intentos
    global intentoselegidos
    global cortar
    global muertos
    global heridos
    global solucion
    global intento
    global cantidad
    intentos +=1
    if cortar==True:
        respuestadialogo['text'] ="Pulsa nuevo juego"
    else:
        muertos=0
        heridos=0
        intento=respuestaentry.get()
        if intento.isdigit()==False:
            respuestadialogo['text'] ="Mete solo números"
            intentos-=1
        elif len(intento)!=cantidad:
            respuestadialogo['text']= (f"Mete {cantidad} dígitos, no más ni menos")
            intentos-=1
        
        else:
            respuestadialogo["text"]=(f"Jugando. Llevas {intentos} intentos")
            comprobacion2=[]
            for i in intento:
                if i in comprobacion2:
                    pass
                else:
                    for j in solucion:
                        if i == j:
                            heridos+=1
                comprobacion2.append(i)
            for i in range(cantidad):
                if intento[i] == solucion [i]:
                    muertos+=1
                    heridos-=1  

            if heridos<0:
                heridos=0        
            lista =[intento, muertos, heridos]
            

            for i in range(intentos):
                pantalla11=f"{lista[0]}"
                pantalla12=f"{lista[1]}"
                pantalla13=f"{lista[2]}"
                pantalla14=f"{intentos} intentos"
                pantalla21=[]
                pantalla22=[]
                pantalla23=[]
                pantalla24=[]
                pantalla21.append(pantalla11)
                pantalla22.append(pantalla12)
                pantalla23.append(pantalla13)
                pantalla24.append(pantalla14)

            informacioninfo1.insert(0,*pantalla21)
            informacioninfo2.insert(0,*pantalla22)
            informacioninfo3.insert(0,*pantalla23)
            informacioninfo4.insert(0,*pantalla24)
            
            if muertos == cantidad:
                
                pantalla21=[]
                pantalla22=[]
                pantalla23=[]
                pantalla24=[]
                respuestadialogo["text"]="Ganaste"
                pantalla21.append("Ganaste")
                pantalla22.append((f" {intentos} " ))
                pantalla23.append("intentos")
                pantalla24.append("")

                
                informacioninfo1.insert(0,*pantalla21)
                informacioninfo2.insert(0,*pantalla22)
                informacioninfo3.insert(0,*pantalla23)
                informacioninfo4.insert(0,*pantalla24)
                cortar=True

            else:
                if intentos<intentoselegidos:
                    Continue
                else:
                    respuestadialogo["text"]=f"{intentos} fallos. Perdiste. Sol: {solucion}"
                    cortar=True
        
        respuestaentry.delete (0,"end")

def disparar6(): #todos a uno
    global intentos
    global intentoselegidos
    global cortar
    global muertos
    global heridos
    global solucion
    global intento
    global cantidad
    intentos +=1
    if cortar==True:
        respuestadialogo['text'] ="Pulsa nuevo juego"
    else:
            
        muertos=0
        heridos=0
        intento=respuestaentry.get()
        if intento.isdigit()==False:
            respuestadialogo['text'] ="Mete solo números"
            intentos-=1
        elif len(intento)!=cantidad:
            respuestadialogo['text']= (f"Mete {cantidad} dígitos, no más ni menos")
            intentos-=1
        
        else:
            respuestadialogo["text"]=(f"Jugando. Llevas {intentos} intentos")
            comprobacion2=[]
            for i in solucion:
                for j in intento:
                    if j in comprobacion2:
                        pass
                    else:
                        if i == j:
                            heridos+=1
                comprobacion2.append(i)
       
            for i in range(cantidad):
                if intento[i] == solucion [i]:
                    muertos+=1
                    heridos-=1           
            if heridos<0:
                heridos=0
            lista =[intento, muertos, heridos]
            
            for i in range(intentos):
                pantalla11=f"{lista[0]}"
                pantalla12=f"{lista[1]}"
                pantalla13=f"{lista[2]}"
                pantalla14=f"{intentos} intentos"
                pantalla21=[]
                pantalla22=[]
                pantalla23=[]
                pantalla24=[]
                pantalla21.append(pantalla11)
                pantalla22.append(pantalla12)
                pantalla23.append(pantalla13)
                pantalla24.append(pantalla14)

            informacioninfo1.insert(0,*pantalla21)
            informacioninfo2.insert(0,*pantalla22)
            informacioninfo3.insert(0,*pantalla23)
            informacioninfo4.insert(0,*pantalla24)
            
            if muertos == cantidad:
                
                pantalla21=[]
                pantalla22=[]
                pantalla23=[]
                pantalla24=[]
                respuestadialogo["text"]="Ganaste"
                pantalla21.append("Ganaste")
                pantalla22.append((f" {intentos} " ))
                pantalla23.append("intentos")
                pantalla24.append("")

                
                informacioninfo1.insert(0,*pantalla21)
                informacioninfo2.insert(0,*pantalla22)
                informacioninfo3.insert(0,*pantalla23)
                informacioninfo4.insert(0,*pantalla24)
                cortar=True

            else:
                if intentos<intentoselegidos:
                    Continue
                else:
                    respuestadialogo["text"]=f"{intentos} fallos. Perdiste. Sol: {solucion}"
                    cortar=True
        
        respuestaentry.delete (0,"end")

def disparar7():  #todos a todos 
    global intentos
    global intentoselegidos
    global cortar
    global muertos
    global heridos
    global solucion
    global intento
    global cantidad
    intentos +=1
    if cortar==True:
        respuestadialogo['text'] ="Pulsa nuevo juego"
    else:
            
        muertos=0
        heridos=0
        intento=respuestaentry.get()
        if intento.isdigit()==False:
            respuestadialogo['text'] ="Mete solo números"
            intentos-=1
        elif len(intento)!=cantidad:
            respuestadialogo['text']= (f"Mete {cantidad} dígitos, no más ni menos")
            intentos-=1
        else:
            respuestadialogo["text"]=(f"Jugando. Llevas {intentos} intentos")
            for i in intento:
                for j in solucion:
                    if i == j:
                        heridos+=1
            for i in range(cantidad):
                if intento[i] == solucion [i]:
                    muertos+=1
                    heridos-=1
            if heridos<0:
                heridos=0
            lista =[intento, muertos, heridos]
            
            for i in range(intentos):
                pantalla11=f"{lista[0]}"
                pantalla12=f"{lista[1]}"
                pantalla13=f"{lista[2]}"
                pantalla14=f"{intentos} intentos"
                pantalla21=[]
                pantalla22=[]
                pantalla23=[]
                pantalla24=[]
                pantalla21.append(pantalla11)
                pantalla22.append(pantalla12)
                pantalla23.append(pantalla13)
                pantalla24.append(pantalla14)

            informacioninfo1.insert(0,*pantalla21)
            informacioninfo2.insert(0,*pantalla22)
            informacioninfo3.insert(0,*pantalla23)
            informacioninfo4.insert(0,*pantalla24)
            
            if muertos == cantidad:
                
                pantalla21=[]
                pantalla22=[]
                pantalla23=[]
                pantalla24=[]
                respuestadialogo["text"]="Ganaste"
                pantalla21.append("Ganaste")
                pantalla22.append((f" {intentos} " ))
                pantalla23.append("intentos")
                pantalla24.append("")

                
                informacioninfo1.insert(0,*pantalla21)
                informacioninfo2.insert(0,*pantalla22)
                informacioninfo3.insert(0,*pantalla23)
                informacioninfo4.insert(0,*pantalla24)
                cortar=True

            else:
                if intentos<intentoselegidos:
                    Continue
                else:
                    respuestadialogo["text"]=f"{intentos} fallos. Perdiste. Sol: {solucion}"
                    cortar=True
        
        respuestaentry.delete (0,"end")





def salir():
    global cortar
    cortar=True
    respuestadialogo['text']= (f"La solución es {solucion}")


raiz.mainloop()