##################################################################
#!                                                              !#
#!                                                              !#
#!                     MÓDULO PRINCIPAL                         !#
#!                                                              !#
#!                                                              !#
##################################################################

import db
import matplotlib.pyplot as plt
import numpy as np
from tkinter import *

import populate as pop
import update as upd
import delete as delt

#database.createDB()             #Cria o banco de dados           #!Executa o DDL
#pop.popular()                   #Popular o banco de dados        #!Printa instruções realizadas no console!#
#upd.atualizar()                 #Atualizar dados do banco        #!Printa instruções realizadas no console!#
#delt.excluir()                  #Deletar alguns dados do banco   #!Printa instruções realizadas no console!#

win = Tk()
win.title("VAPOR!")

########## Canvas ##############
canvas = Canvas(win, height=450, width=225)
canvas.pack()

frame = Frame()
frame.place(relx= 0.1, rely=0.1, relwidth=0.8, relheight=0.8)

label = Label(frame, text='Criar o banco de dados:')
label.grid(row=0, column=1)

label = Label(frame, text='Popular o banco de dados:')
label.grid(row=2, column=1)

label = Label(frame, text='Atualizar o banco de dados:')
label.grid(row=4, column=1)

label = Label(frame, text='Deletar alguns dados do banco:')
label.grid(row=6, column=1)

label = Label(frame, text='Consulta 1:')
label.grid(row=8, column=1)

label = Label(frame, text='Consulta 2:')
label.grid(row=10, column=1)

label = Label(frame, text='Consulta 3:')
label.grid(row=12, column=1)

Criar = Button(frame, text="Criar", command=lambda:db.createDB())
Criar.grid(row=1, column=1, sticky=W+E)

Popular = Button(frame, text="Popular", command=lambda:pop.popular())
Popular.grid(row=3, column=1, sticky=W+E)

Atualizar = Button(frame, text="Atualizar", command=lambda:upd.atualizar())
Atualizar.grid(row=5, column=1, sticky=W+E)

Excluir = Button(frame, text="Excluir", command=lambda:delt.excluir())
Excluir.grid(row=7, column=1, sticky=W+E)

Consulta1 = Button(frame, text="Consulta", command=lambda:Consulta1())
Consulta1.grid(row=9, column=1, sticky=W+E)

Consulta2 = Button(frame, text="Consulta 2", command=lambda:Consulta2())
Consulta2.grid(row=11, column=1, sticky=W+E)

Consulta3 = Button(frame, text="Consulta 3", command=lambda:Consulta3())
Consulta3.grid(row=13, column=1, sticky=W+E)

#######################################################################

def plotarGrafico_Redondo(data, descritivo, legenda, titulo):
    """
    Função criada para facilitar a plotagem de gráficos em pizza (piecharts)
    """
    fig1, ax1 = plt.subplots(figsize=(6, 6), subplot_kw=dict(aspect="equal"))

    def func(porcento, valores):
        # calc %
        absoluto = int(porcento/100.*np.sum(valores))
        return "{:.1f}%\n(R${:d})".format(porcento, absoluto)

    wedges, texts, autotexts = ax1.pie(data, autopct=lambda pct: func(pct, data), textprops=dict(color="w"))

    ax1.legend(
        wedges, descritivo,
        title=legenda,
        loc="center left",
        bbox_to_anchor=(1, 0, 0.5, 1)
    )
    plt.setp(autotexts, size=8)
    ax1.set_title(titulo)

    plt.show()

def plotarGrafico_barra(a,b, titulo):
    """
    Função utilizada para plotar o gráfico em barras
    """
    jogos = [a]
    devs = [b]

    font = {'family' : 'Roboto','weight' : 'bold', 'size': 8}

    plt.rc('font', **font)
    
    plt.bar(b,a,color="blue")
    plt.xticks(b)
    plt.title(titulo)
    plt.show()

def Consulta1():
    """
    O objetivo desta consulta é calcular utilizando as tabelas nome, inventario e item. O valor médio de cada inventário.
    """

    query = """
        SELECT u.nome as Nomes, AVG(item.valor) as MediaItens
        FROM inventario as inv, item, usuario as u
        WHERE inv.id_user = u.id_user and inv.id_item = item.id_item
        GROUP BY u.id_user
        ORDER BY MediaItens;
    """

    #QUERY RETORNADA NO TERMINAL!
    print("A instrução SQL realizada nesta consulta foi: ")
    print(query)

    db.cursor.execute(query)    
    ValorInventario = db.cursor.fetchall()
    
    nomes = []
    valorInv = []
    valorTotal = 0

    for v in ValorInventario:
        nome = v[0]
        nomes += [(nome)]

        valor = float(v[1])
        valorInv += [(valor)]

        valorTotal += float(v[1])

    plotarGrafico_Redondo(valorInv, nomes, "Usuários:", "Preço Médio dos Inventários")

def Consulta2():
    """
    Relacionar o número de desenvolvedores e o número de jogos criados por eles
    """
    
    query2 = """
        SELECT COUNT(jogo.id_jogo) as Quant_jogos, dev.nome_dev as Desenvolvedor 
        FROM jogo, distribuidora, dev, distribuidora_dev
        WHERE jogo.id_distr = distribuidora.id_distr
        AND distribuidora.id_distr = distribuidora_dev.id_distr
        AND distribuidora_dev.id_dev = dev.id_dev
        GROUP BY dev.nome_dev;
    """
    print("A instrução SQL realizada nesta consulta foi: ")
    print(query2)
    db.cursor.execute(query2)    
    quant_devs_game = db.cursor.fetchall()

    quant_games = []
    devs = []
    jogostotal = 0

    for q in quant_devs_game:
        games = int(q[0])
        quant_games += [(games)]

        jogostotal += int(q[0])
        dev = q[1]
        devs += [(dev)]

    plotarGrafico_barra(quant_games, devs, "Relação Jogos x Desenvolvedor")


def Consulta3():
    """
    Consulta para descobrir o valor total da lista de desejos dos usuários
    """

    query = """
        SELECT u.nome as Nomes, SUM(jo.valor) as ValorFuturo FROM lista_de_desejos as li, usuario as u, jogo as jo
        WHERE li.id_user= u.id_user and jo.id_jogo = li.id_jogo
        GROUP BY u.nome
        ORDER BY u.nome ASC;
    """
    db.cursor.execute(query)

    print("A instrução SQL realizada nesta consulta foi: ")
    print(query)

    consulta = db.cursor.fetchall()

    usuarios = []
    valores = []

    for retorno in consulta:
        usuarios.append(retorno[0])
        valores.append(float(retorno[1]))

    plotarGrafico_Redondo(valores, usuarios, "Usuários:", "Preço total da Lista de Desejos")


win.mainloop()
db.closeDB()              #Encerra a conexão com o banco de dados