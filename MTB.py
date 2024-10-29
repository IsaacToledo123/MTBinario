import tkinter as tk
from tkinter import messagebox, ttk

def sumar_binarios(bin1, bin2):
    suma = bin(int(bin1, 2) + int(bin2, 2))[2:]
    return suma

def calcular_suma_acumulada():
    bin1 = entry_binario1.get()
    bin2 = entry_binario2.get()
    binarios_adicionales = entry_lista_binarios.get()

    if not bin1 or not bin2:
        messagebox.showerror("Error", "Ingresa los primeros dos números binarios.")
        return

    input_completo = f"{bin1} + {bin2} + {binarios_adicionales}"
    resultado = sumar_binarios(f"{bin1}{bin2}", binarios_adicionales)
    resultado_label = tk.Label(historial_frame, text=f"{input_completo} = {resultado}", bg="white", font=("Arial", 10))
    resultado_label.pack(anchor="w", padx=10, pady=2)

    entry_binario1.delete(0, tk.END)
    entry_binario2.delete(0, tk.END)
    entry_lista_binarios.delete(0, tk.END)

root = tk.Tk()
root.title("Calculadora Binaria")
root.geometry("500x500")
root.configure(bg="#f4f4f9")

notebook = ttk.Notebook(root)
notebook.pack(pady=10, expand=True)
calculadora_tab = tk.Frame(notebook, bg="#e0e0e0")
notebook.add(calculadora_tab, text="Calculadora")
input_frame = tk.Frame(calculadora_tab, bg="#e0e0e0", padx=20, pady=20)
input_frame.pack(fill="both", expand=True, padx=10, pady=10)
title_label = tk.Label(input_frame, text="Suma Binaria Acumulativa", font=("Arial", 16), bg="#e0e0e0", fg="#333")
title_label.pack(pady=10)
entry_label1 = tk.Label(input_frame, text="Primer Binario:", bg="#e0e0e0")
entry_label1.pack(anchor="w")
entry_binario1 = tk.Entry(input_frame, width=20)
entry_binario1.pack(anchor="w", pady=5)
entry_label2 = tk.Label(input_frame, text="Segundo Binario:", bg="#e0e0e0")
entry_label2.pack(anchor="w")
entry_binario2 = tk.Entry(input_frame, width=20)
entry_binario2.pack(anchor="w", pady=5)
entry_label3 = tk.Label(input_frame, text="Binarios Adicionales:", bg="#e0e0e0")
entry_label3.pack(anchor="w")
entry_lista_binarios = tk.Entry(input_frame, width=30)
entry_lista_binarios.pack(anchor="w", pady=5)
calcular_btn = tk.Button(input_frame, text="Calcular y Agregar al Historial", command=calcular_suma_acumulada, bg="#333", fg="white", font=("Arial", 10))
calcular_btn.pack(pady=20)
historial_tab = tk.Frame(notebook, bg="white")
notebook.add(historial_tab, text="Historial de Cálculos")
historial_frame = tk.Frame(historial_tab, bg="white", padx=10, pady=10)
historial_frame.pack(fill="both", expand=True)

historial_title = tk.Label(historial_frame, text="Operaciones Realizadas:", font=("Arial", 14), bg="white", fg="#333")
historial_title.pack(anchor="w")

root.mainloop() 