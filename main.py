import tkinter as tk
from datetime import datetime

def adicionar_tarefa():
    tarefa = entrada_tarefa.get()
    if tarefa:
        agora = datetime.now()
        data_hora = agora.strftime("%Y-%m-%d %H:%M:%S")
        tarefa_com_data = f"{data_hora}: {tarefa}"
        
        lista_tarefas.insert(tk.END, tarefa_com_data)
        entrada_tarefa.delete(0, tk.END)
        salvar_tarefas()

def remover_tarefa():
    selecao = lista_tarefas.curselection()
    if selecao:
        lista_tarefas.delete(selecao)
        salvar_tarefas()

def salvar_tarefas():
    with open("tarefas.txt", "w") as arquivo:
        tarefas = lista_tarefas.get(0, tk.END)
        arquivo.writelines(tarefa + "\n" for tarefa in tarefas)

def carregar_tarefas():
    try:
        with open("tarefas.txt", "r") as arquivo:
            for linha in arquivo:
                tarefa = linha.strip()
                lista_tarefas.insert(tk.END, tarefa)

    except FileNotFoundError:
        pass

# Criando a janela principal
janela = tk.Tk()
janela.title("Lista de Tarefas")

# Aumentando o tamanho da janela para 800x600 pixels
largura = 800
altura = 600
janela.geometry(f"{1080}x{720}")

# Criando e configurando os widgets
frame = tk.Frame(janela)
frame.pack(pady=10)

lista_tarefas = tk.Listbox(frame, selectbackground="yellow")
lista_tarefas.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

lista_tarefas.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=lista_tarefas.yview)

entrada_tarefa = tk.Entry(janela, font=("Helvetica", 14))
entrada_tarefa.pack(pady=10)

botao_adicionar = tk.Button(janela, text="Adicionar Tarefa", command=adicionar_tarefa)
botao_adicionar.pack(pady=5)

botao_remover = tk.Button(janela, text="Remover Tarefa", command=remover_tarefa)
botao_remover.pack(pady=5)

# Carregar tarefas existentes
carregar_tarefas()

# Iniciar o loop principal
janela.mainloop()
