import tkinter as tk

def suma():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    result.set(num1 + num2)

def resta():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    result.set(num1 - num2)

# Crear ventana
root = tk.Tk()
root.title("Calculadora")

# Crear campos de entrada
entry_num1 = tk.Entry(root)
entry_num1.pack()

entry_num2 = tk.Entry(root)
entry_num2.pack()

# Crear botones de operaciones
btn_suma = tk.Button(root, text="Suma", command=suma)
btn_suma.pack()

btn_resta = tk.Button(root, text="Resta", command=resta)
btn_resta.pack()

# Mostrar resultado
result = tk.StringVar()
label_result = tk.Label(root, textvariable=result)
label_result.pack()

# Iniciar bucle de eventos
root.mainloop()