import tkinter as tk
from tkinter import messagebox

# Função que calcula o salário com base nas condições
def calcular_salario():
    try:
        salario = int(entry_salario.get())

        if salario <= 2000:
            resultado = "Insento - R$" + str(salario)
        elif salario > 2000 and salario < 5000:
            salario_taxa = salario * 0.10
            salario = salario + salario_taxa
            resultado = "Cobrada taxa - R$" + str(salario)
        else:
            salario_taxa = salario * 0.20
            salario = salario + salario_taxa
            resultado = "Cobrado taxa - R$" + str(salario)

        # Exibe o resultado
        messagebox.showinfo("Resultado", resultado)
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um valor numérico válido.")

# Criação da interface gráfica
app = tk.Tk()
app.title("Calculadora de Salário")
app.geometry("400x250")  # Define o tamanho da janela

# Definindo cores e fontes
bg_color = "#F0F8FF"  # Cor de fundo da janela
button_color = "#4682B4"  # Cor dos botões
font_label = ("Arial", 14, "bold")
font_entry = ("Arial", 12)
font_button = ("Arial", 12, "bold")

# Configuração de cor de fundo
app.config(bg=bg_color)

# Título
label_titulo = tk.Label(app, text="Calculadora de Salário", font=("Arial", 16, "bold"), bg=bg_color)
label_titulo.pack(pady=10)

# Campo para entrada do salário
label_salario = tk.Label(app, text="Insira seu salário:", font=font_label, bg=bg_color)
label_salario.pack(pady=10)

entry_salario = tk.Entry(app, font=font_entry, width=20)
entry_salario.pack(pady=10)

# Botão para calcular
button_calcular = tk.Button(app, text="Calcular", font=font_button, bg=button_color, fg="white", command=calcular_salario)
button_calcular.pack(pady=20)

# Inicia o loop da aplicação
app.mainloop()

