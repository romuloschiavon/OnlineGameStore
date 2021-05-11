<h1 align="center">Online Game Store Project</h1>
<p align="center"><strong>VAPOR</strong></p>

Vapor is the final project developed for my Database I course on UFSC. The projects was developed using python and postgresql, and it has the purpose of copying a few funcionalities of Steam. 

The main idea of the project was to design the conceptual model and the logic model of the database, create an application that communicates with the database (realizes inserts/updates/deletes) and return in some way a graph of selections that had a meaning on the long run.

## Conceptual model

<img src="https://i.imgur.com/UvwrXWR.jpg"></img>

The main ideia of the conceptual model was to revolve around the game (jogo). The issue to be altered in the application is generating orders with dates. As of right now it has a lot of problemns exceptionally when the order has a lot of itens, packages (expansions) and games.
The favorite list (Lista de Desejos) has issues and it should be changed as well.

## Logic Model

<img src="https://i.imgur.com/Pj3pc4x.jpg"></img>

The ideia of the logic model is to work around the errors of the conceptual model, so that the application can be runned even with the errors that should be fixed later.

## How to run

To run the application you should alter the params in ```db.py``` to your postgresql database. Such as username, password, host etc...

Install **[PsycoPg2](https://pypi.org/project/psycopg2/)**
Install **[MatPlotLib](https://matplotlib.org/stable/users/installing.html)**
Install **[NumPy](https://numpy.org/install/)**

After altered run ```main.py``` and it should create a GUI (in portuguese) with all the interactions thart can be runned withing the aplication.

In the console you should see a lot of prints, they're for the main purpose that the teacher wanted us to show him in console the creation, inserts, updates and deletes of the application.

## Graphs

The graphs are automatically generated using matplotlib. So check them running the application!

## For portuguese readers

If you know portuguese and want to see the full document with all the details and explanations that we (me and [Matheus](https://github.com/matheus1103)) gave to our teacher, check the document [Relatorio](https://github.com/romuloschiavon/LojaOnlineDeJogos/blob/main/Relatorio.pdf)
