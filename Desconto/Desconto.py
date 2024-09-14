import tkinter as tk
from tkinter import messagebox

# Função para calcular o valor da compra com desconto
def calcular_valor_compra():
    try:
        valor_compra = int(entry_valor_compra.get())

        if valor_compra <= 50:
            resultado = "Sem desconto - R$" + str(valor_compra)
        elif 50 < valor_compra < 5000:
            valor_compra_taxa = valor_compra * 0.10
            valor_compra = valor_compra - valor_compra_taxa
            resultado = "Com desconto de 10% - R$" + str(valor_compra)
        else:
            valor_compra_taxa = valor_compra * 0.20
            valor_compra = valor_compra - valor_compra_taxa
            resultado = "Com desconto de 20% - R$" + str(valor_compra)

        # Exibe o resultado em um popup
        messagebox.showinfo("Resultado", resultado)
    except ValueError:
        # Caso o valor inserido não seja válido
        messagebox.showerror("Erro", "Por favor, insira um valor numérico válido.")

# Criação da janela principal
app = tk.Tk()
app.title("Calculadora de Desconto")
app.geometry("400x250")  # Define o tamanho da janela

# Definindo cores e fontes
bg_color = "#F0F8FF"  # Cor de fundo da janela
button_color = "#4682B4"  # Cor dos botões
font_label = ("Arial", 14, "bold")
font_entry = ("Arial", 12)
font_button = ("Arial", 12, "bold")

# Configuração de cor de fundo da janela
app.config(bg=bg_color)

# Título
label_titulo = tk.Label(app, text="Calculadora de Desconto", font=("Arial", 16, "bold"), bg=bg_color)
label_titulo.pack(pady=10)

# Campo para entrada do valor da compra
label_valor_compra = tk.Label(app, text="Informe o valor da compra:", font=font_label, bg=bg_color)
label_valor_compra.pack(pady=10)

entry_valor_compra = tk.Entry(app, font=font_entry, width=20)
entry_valor_compra.pack(pady=10)

# Botão para calcular o desconto
button_calcular = tk.Button(app, text="Calcular", font=font_button, bg=button_color, fg="white", command=calcular_valor_compra)
button_calcular.pack(pady=20)

# Inicia o loop da aplicação
app.mainloop()
