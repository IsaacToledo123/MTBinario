import tkinter as tk
from tkinter import messagebox

class TuringMachine:
    def __init__(self, input_tape):
        self.tape = list(input_tape) + ['_'] * 10  
        self.head = 0  
        self.state = 'q0'
        self.result = ""  

    def binary_sum(self, num1, num2):
        max_len = max(len(num1), len(num2))
        num1 = num1.zfill(max_len)
        num2 = num2.zfill(max_len)

        result = ""
        carry = 0

        for i in range(max_len - 1, -1, -1):
            bit_sum = carry
            bit_sum += 1 if num1[i] == '1' else 0
            bit_sum += 1 if num2[i] == '1' else 0

            result = ('1' if bit_sum % 2 == 1 else '0') + result
            carry = 0 if bit_sum < 2 else 1

        if carry != 0:
            result = '1' + result
        return result

    def process(self):
        binary_numbers = ''.join(self.tape).split('_')[0].split()
        sum_result = binary_numbers[0]

        for binary_number in binary_numbers[1:]:
            sum_result = self.binary_sum(sum_result, binary_number)

        self.result = sum_result
        for i in range(len(sum_result)):
            self.tape[i] = sum_result[i]

    def get_result_binary(self):
        return ''.join(self.tape).strip('_')

    def get_result_decimal(self):
        return int(self.get_result_binary(), 2)

def calculate_sum():
    input_data = entry.get()
    if not input_data:
        messagebox.showerror("Error", "Por favor, ingresa números binarios.")
        return

    maquina = TuringMachine(input_data)
    maquina.process()
    result_binary = maquina.get_result_binary()
    result_decimal = maquina.get_result_decimal()
    result_label.config(text=f"Resultado binario: {result_binary} \nResultado decimal: {result_decimal}")

root = tk.Tk()
root.title("Máquina de Turing - Suma Binaria")

entry_label = tk.Label(root, text="Ingrese números binarios separados por espacios:")
entry_label.pack()

entry = tk.Entry(root, width=30)
entry.pack()

calculate_button = tk.Button(root, text="Calcular Suma", command=calculate_sum)
calculate_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
