# Importando a biblioteca Tkinter
import tkinter as tk
import webbrowser

# Criando a janela do aplicativo
janela = tk.Tk()

# Criando uma função para abrir o arquivo no link fornecido
def abrir_arquivo():
    url = 'https://github.com/rfg24/urna-eleitoral.git'  
    webbrowser.open(url)

# Criando o menu
menu = tk.Menu(janela)
janela.config(menu=menu)

# Criando a opção do menu
opcao_menu = tk.Menu(menu, tearoff=0)
opcao_menu.add_command(label="Abrir Arquivo", command=abrir_arquivo)
menu.add_cascade(label="Opções", menu=opcao_menu)

# Iniciando o loop do aplicativo
janela.mainloop()