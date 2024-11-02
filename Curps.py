import tkinter as tk
from tkinter import messagebox

def es_bisiesto(anio: int) -> bool:
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)

def validar_fecha(fecha: str) -> bool:
    try:
        anio = int(fecha[:2])
        mes = int(fecha[2:4])
        dia = int(fecha[4:])
        anio_completo = 1900 + anio if anio > 23 else 2000 + anio
        
        if not (1 <= mes <= 12):
            return False
        if mes == 2:
            max_dia = 29 if es_bisiesto(anio_completo) else 28
        elif mes in {4, 6, 9, 11}:
            max_dia = 30
        else:
            max_dia = 31
        return 1 <= dia <= max_dia
    except ValueError:
        return False

def validar_curp(curp: str) -> bool:
    if len(curp) != 18:
        return False
    letras = curp[:4].isalpha()
    fecha_valida = validar_fecha(curp[4:10])
    genero = curp[10] in "HM"
    entidad = curp[11:13].isalpha()
    homonimo = curp[13:16].isalnum()
    verificador = curp[17].isalnum()
    return letras and fecha_valida and genero and entidad and homonimo and verificador

def verificar_curp():
    curp = entry_curp.get().upper()
    if validar_curp(curp):
        messagebox.showinfo("Validación de CURP", "La CURP ingresada es válida.")
    else:
        messagebox.showerror("Validación de CURP", "La CURP ingresada no es válida.")

def generar_curp():
    nombre = entry_nombre.get().strip().upper()
    apellido_paterno = entry_apellido_paterno.get().strip().upper()
    apellido_materno = entry_apellido_materno.get().strip().upper()
    fecha_nacimiento = entry_fecha_nacimiento.get().strip()
    genero = entry_genero.get().strip().upper()
    entidad = entry_entidad.get().strip().upper()

    if not (nombre and apellido_paterno and apellido_materno and validar_fecha(fecha_nacimiento) and genero in "HM" and entidad):
        messagebox.showerror("Error", "Por favor, ingrese todos los datos correctamente.")
        return

    curp = (apellido_paterno[0] +
            primer_vocal(apellido_paterno) +
            apellido_materno[0] +
            nombre[0] +
            fecha_nacimiento +
            genero +
            entidad +
            "X00") 

    messagebox.showinfo("Generar CURP", f"CURP generada: {curp}")

def primer_vocal(texto: str) -> str:
    for char in texto[1:]:
        if char in "AEIOU":
            return char
    return "X"  

ventana = tk.Tk()
ventana.title("Validación y Generación de CURP")
ventana.geometry("400x400")

frame_validacion = tk.LabelFrame(ventana, text="Validación de CURP", padx=10, pady=10)
frame_validacion.pack(padx=10, pady=10, fill="both", expand="yes")

label_curp = tk.Label(frame_validacion, text="Ingresa la CURP:")
label_curp.pack(pady=5)

entry_curp = tk.Entry(frame_validacion, width=20)
entry_curp.pack(pady=5)

boton_verificar = tk.Button(frame_validacion, text="Verificar CURP", command=verificar_curp)
boton_verificar.pack(pady=10)

frame_generacion = tk.LabelFrame(ventana, text="Generación de CURP", padx=10, pady=10)
frame_generacion.pack(padx=10, pady=10, fill="both", expand="yes")

label_nombre = tk.Label(frame_generacion, text="Nombre:")
label_nombre.grid(row=0, column=0, padx=5, pady=5, sticky="e")
entry_nombre = tk.Entry(frame_generacion, width=20)
entry_nombre.grid(row=0, column=1, padx=5, pady=5)

label_apellido_paterno = tk.Label(frame_generacion, text="Apellido Paterno:")
label_apellido_paterno.grid(row=1, column=0, padx=5, pady=5, sticky="e")
entry_apellido_paterno = tk.Entry(frame_generacion, width=20)
entry_apellido_paterno.grid(row=1, column=1, padx=5, pady=5)

label_apellido_materno = tk.Label(frame_generacion, text="Apellido Materno:")
label_apellido_materno.grid(row=2, column=0, padx=5, pady=5, sticky="e")
entry_apellido_materno = tk.Entry(frame_generacion, width=20)
entry_apellido_materno.grid(row=2, column=1, padx=5, pady=5)

label_fecha_nacimiento = tk.Label(frame_generacion, text="Fecha de Nacimiento (AAMMDD):")
label_fecha_nacimiento.grid(row=3, column=0, padx=5, pady=5, sticky="e")
entry_fecha_nacimiento = tk.Entry(frame_generacion, width=20)
entry_fecha_nacimiento.grid(row=3, column=1, padx=5, pady=5)

label_genero = tk.Label(frame_generacion, text="Género (H/M):")
label_genero.grid(row=4, column=0, padx=5, pady=5, sticky="e")
entry_genero = tk.Entry(frame_generacion, width=20)
entry_genero.grid(row=4, column=1, padx=5, pady=5)

label_entidad = tk.Label(frame_generacion, text="Entidad Federativa:")
label_entidad.grid(row=5, column=0, padx=5, pady=5, sticky="e")
entry_entidad = tk.Entry(frame_generacion, width=20)
entry_entidad.grid(row=5, column=1, padx=5, pady=5)

boton_generar = tk.Button(frame_generacion, text="Generar CURP", command=generar_curp)
boton_generar.grid(row=6, column=0, columnspan=2, pady=10)

ventana.mainloop()
