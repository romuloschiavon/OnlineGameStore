#TODO TABELAS
#Usuario            OK
#DEV                OK
#DISTRI             OK
#CLASS              OK 
#CATEGORIA          OK
#TRADUCAO           OK
#DUBLAGEM           OK
#REQUISITOS         OK
#EXPANSAO           OK
#JOGO               OK
#ITEM               OK
#INVENTARIO         OK
#AMIZADE            OK
#PACOTE             OK
#COMPRA             OK
#LISTA_DE_DESEJOS   OK
#DISTR_DEV          OK
#CARACTERISTICA     OK
#COMENTARIO         OK

#Todas as inserções foram realizadas da mesma maneira, utilizando arrays e for que realiza a inserção de todo o array.

import db

def popular():
    ######################## USUARIOS ###################################

    usuarios = [
        ('mariazinha@gmail.com', 'mariaah', 'Maria das Dores', '1999-06-06'), 
        ('joaninha@gmail.com', 'joanadarkgamer', 'Joana Kamilla', '2003-04-10'), 
        ('kleberbambam@gmail.com', 'MAROMBEIRO', 'Kleber de Paula Pedra', '1978-02-14'), 
        ('faustaoolocomeu@gmail.com', 'faustaooficial', 'Fausto Silva', '1950-05-02'), 
        ('ratinho@gmail.com', 'xaropinhoGamer', 'Ratinho Jr', '2001-10-10'), 
        ('zeca_camargo@gmail.com', 'zequinha', 'Zeca Margo', '1999-09-20'), 
        ('celso_por_ti_olhe@gmail.com', 'celsoportiolli', 'Ceslso Portiolli', '1980-05-23'), 
        ('josemaria@gmail.com', 'JoseSilva', 'Jose Maria da Silva Sauro', '2005-02-20') 
        ]

    print("\n ################ INSERÇÃO DE USUARIOS ################ ")
    print("\nA instrução realizada no BANCO DE DADOS foi:")
    for u in usuarios:
        db.cursor.execute("INSERT INTO usuario VALUES (default, %s, %s, %s, %s)", (u[0], u[1], u[2], u[3]))
        print(f"INSERT INTO usuario VALUES {u}")

    db.conn.commit()


    ######################## DESENVOLVEDORES ###################################

    dev = [
        ('Rodrigo Fernandes'), 
        ('Leandro Rodolfo'), 
        ('José Geraldo'), 
        ('Maria Julia'), 
        ('Matheus Francisco'),
        ('Romulo Schiavon'),
        ('Rogerio Mendonça'),
        ('Ana Carolina'),
        ('Livia Barbosa'),
        ('Arthur Padilha'),
        ('Henrique Lima'),
        ('Joaquim Muller'),
        ('Ana Vitória'),
        ('Alessandro Jatoba')
         
        ]

    print("\n ################ INSERÇÃO DE DESENVOLVEDORES ################ ")
    print("\nA instrução realizada no BANCO DE DADOS foi:")
    for d in dev:
        db.cursor.execute(f"INSERT INTO dev VALUES (default, %s)", (d,))
        print(f"INSERT INTO dev VALUES {d}")

    db.conn.commit()

    ######################## DISTRIBUIDORAS ###################################

    print("\n ################ INSERÇÃO DE DISTRIBUIDORAS ################ ")
    print("\nA instrução realizada no BANCO DE DADOS foi:")
    distribuidoras = [
        ('BluePrintCO', 'bluepco@gmail.com', 'Rua alex moreira, São Paulo - SP', '11111111111111'), 
        ('CupCup', 'CupCup@gmail.com', 'Av presidente, Curitiba-PR,', '22222222222222'), 
        ('Kootly', 'kootly@gmail.com', 'Rua Sena Madureira, São Paulo - SP', '33333333333333'), 
        ('Ubsoft', 'ubsoft@gmail.com', '28 Rue Armand Carrel,Montreuil - França', '44444444444444'), 
        ('Eletronic Arts', 'EA@gmail.com', 'Austin, TX 78729, Estados Unidos', '55555555555555')
        ]

    for dist in distribuidoras:
        db.cursor.execute("INSERT INTO distribuidora VALUES (default, %s, %s, %s, %s)", (dist[0], dist[1], dist[2], dist[3]))
        print(f"INSERT INTO distribuidora VALUES {dist}")

    db.conn.commit()

    ######################## CLASSIFICACOES ###################################

    print("\n ################ INSERÇÃO DE CLASSIFICACOES ################ ")
    print("\nA instrução realizada no BANCO DE DADOS foi:")
    classificacao = [
        ('Livre', '+0', 'Classificação livre para todos os publicos.'), 
        ('10', '+7', 'Classificação indicada para crianças com mais de 7 anos de idade.'),
        ('14', '+13', 'Classificação indicada para adolecentes acom mais de 13 anos de idade.'), 
        ('16', '+16', 'Classificação indicada para jovens com mais de 16 anos de idade.'), 
        ('18', '+18', 'Classificação indicada para adultos.')
        ]

    for c in classificacao:
        db.cursor.execute("INSERT INTO classificacao VALUES (default, %s, %s, %s)", (c[0], c[1], c[2]))
        print(f"INSERT INTO classificacao VALUES {c}")

    db.conn.commit()

    ######################## CATEGORIAS ###################################

    print("\n ################ INSERÇÃO DE CATEGORIAS ################ ")
    print("\nA instrução realizada no BANCO DE DADOS foi:")
    categoria = [
        (' Massively Multiplayer Online Game', 'MMO'), 
        (' Role Playing Game', 'RPG'),
        ('First-Person Shooters', 'FPS'),
        ('Multiplayer online battle arena', 'MOBA'),
        ('Simulate real life events in game', 'Simulation'),
        ('You are free to create whatever you want', 'SandBox'),
        ('Real time strategy', 'RTS'),
        ('Action game', 'Action'),
        ('Fight game', 'Fight'),
        ('Adventure game', 'Adventure'),
        ('Horror and terror game', 'Horror'),
        ('Online multiplayer', 'Multiplayer'),
        ('Local solo-Play', 'Sigle Player'),
        ]

    for cat in categoria:
        db.cursor.execute("INSERT INTO categoria VALUES (default, %s, %s)", (cat[0], cat[1]))
        print(f"INSERT INTO categoria VALUES {cat}")

    db.conn.commit()

    ######################## TRADUCOES ###################################

    print("\n ################ INSERÇÃO DE TRADUÇÕES ################ ")
    print("\nA instrução realizada no BANCO DE DADOS foi:")
    traducao = [
        ('Portugues - BR'),
        ('Portugues - PT'), 
        ('Inglês'), 
        ('Francês'), 
        ('Italiano'), 
        ('Alemão'), 
        ('Espanhol - ESP'), 
        ('Árabe'),
        ('Japonês'),
        ('Coreano'),
        ('Russo'),   
        ('Polonês'),   
        ]

    for t in traducao:
        db.cursor.execute(f"INSERT INTO traducao VALUES (%s, default)", (t,))
        print(f"INSERT INTO traducao VALUES {t}")

    db.conn.commit()

    ######################## DUBLAGENS ###################################

    print("\n ################ INSERÇÃO DE DUBLAGENS ################ ")
    print("\nA instrução realizada no BANCO DE DADOS foi:")
    dublagem = [
        ('Portugues - BR'),
        ('Portugues - PT'), 
        ('Inglês'), 
        ('Francês'), 
        ('Italiano'), 
        ('Alemão'), 
        ('Espanhol - ESP'), 
        ('Árabe'),
        ('Japonês'),
        ('Coreano'),
        ('Russo'),   
        ('Polonês'),   
        ]

    for dub in dublagem:
        db.cursor.execute(f"INSERT INTO dublagem VALUES (default, %s)", (dub,))
        print(f"INSERT INTO dublagem VALUES {dub}")

    db.conn.commit()

    ######################## REQUISITOS ###################################

    print("\n ################ INSERÇÃO DE REQUISITOS ################ ")
    print("\nA instrução realizada no BANCO DE DADOS foi:")
    requisitos = [
        ('Nvidia GPU GeForce GTX 660', '50GB', 'Windows 10, linux', '8GB','Intel CPU Core i7 3770 3.4 GHz'), 
        ('AMD GPU Radeon HD 7870', '20GB', 'Windows 10, linux', '6GB','AMD CPU AMD FX-8350 4 GHz'),
        ('Nvidia GPU GeForce GTX 3080', '100GB', 'Windows 10', '12GB','Intel CPU Core i9 10770 5.4 GHz'), 
        ('AMD GPU RX3500', '90GB', 'Windows 10', '12GB','AMD CPU AMD FX-10000 5 GHz'), 
        ]

    for req in requisitos:
        db.cursor.execute("INSERT INTO requisito VALUES (default, %s, %s, %s, %s, %s)", (req[0], req[1], req[2], req[3], req[4]))
        print(f"INSERT INTO requisito VALUES {req}")

    db.conn.commit()

    ######################## EXPANSOES ###################################

    print("\n ################ INSERÇÃO DE EXPANSOES ################ ")
    print("\nA instrução realizada no BANCO DE DADOS foi:")
    expansao = [
        ('Divindo da morte', 'Jogue novas aventuras em mapas e inimigos ineditos', '100'), 
        ('Final Mascarade', 'Novos Mapas', '30'), 
        ('Shake it Now! Expansion!', 'Dance! Dance! Dance!', '20'), 
        ('New Divide', 'Itens ineditos, colecionaveis e muito mais', '200'), 
        ]

    for ex in expansao:
        db.cursor.execute("INSERT INTO expansao VALUES (default, %s, %s, %s)", (ex[0], ex[1], ex[2]))
        print(f"INSERT INTO expansao VALUES {ex}")

    db.conn.commit()

    ######################## JOGOS ###################################

    print("\n ################ INSERÇÃO DE JOGOS ################ ")
    print("\nA instrução realizada no BANCO DE DADOS foi:")
    jogo = [
        ('2', 'Rolling Fight','11-03-2020','Um jogo extremamente divertido e carismático que você vai adorar!!!', '100'), 
        ('5', 'The wizard 3', '18-05-2018','Enquanto a guerra assola todos os Reinos do Norte,você enfrenta o maior conflito de sua vida: ir em busca da criança da profecia, uma arma senciente capaz de alterar o mundo.', '150'), 
        ('3', 'Dance! Dance! Dance!', '20-08-2018','Dance musicas incriveis sozinho ou com seus amigos!!!!', '30'), 
        ('1', 'Fall Persons', '02-02-2019','Fall Persons é um party game para multijogador com até 60 jogadores online, em uma louca corrida free-for-all, com rounds e rounds cada vez mais caóticos até sobrar um único vencedor!', '19.99'), 
        ('4', 'Amoung They', '05-12-2017','An online and local party game of teamwork and betrayal for 4-10 players...in earth!', '10'), 
        ('4', 'NearCry', '04-12-2012','Discover the dark secrets of a lawless island ruled by violence and take the fight to the enemy as you try to escape. You’ll need more than luck to escape alive!', '200'), 
        ('5', 'FIFA 25', '15-05-2021','Jogue com os times mais famosos do mundo agora mesmo!', '350'), 
        ('4', 'OurCraft', '10-11-2010','Free game with uncount possibilites', '30'), 
        ('3', 'FreeFas', '20-01-2020','BR FreeFas é um jogo eletrônico de ação-aventura do gênero battle royale visto numa perspectiva em terceira pessoa.', '500'), 
        ]

    for j in jogo:
        db.cursor.execute("INSERT INTO jogo VALUES (default, %s, %s, %s, %s, %s)", (j[0], j[1], j[2], j[3], j[4]))
        print(f"INSERT INTO jogo VALUES {j}")

    db.conn.commit()

    ######################## DISTR_DEV ###################################

    print("\n ################ INSERÇÃO DA RELAÇÃO DISTRIBUIDORA_DEV ################ ")
    print("\nA instrução realizada no BANCO DE DADOS foi:")
    distdevs=[
        ('1','2'),
        ('2','2'),
        ('4','1'),
        ('3','5'),
        ('5','4'),
        ('6','1'),
        ('7','1'),
        ('8','5'),
        ('9','2'),
        ('10','4'),
        ('11','4'),
        ('12','1'),
        ('13','5'),
        ('14','3'),
        ('1','3'),
        ('10','2'),
        ('8','5'),
        ('6','2'),
        ('4','2'),
        ('2','1'),
        ('6','5'),
        ('3','4'),
        ('1','2'),
        ('1','1')
    ]

    for ddev in distdevs:
        db.cursor.execute("INSERT INTO distribuidora_dev VALUES (%s, %s)", (ddev[0], ddev[1]))
        print(f"INSERT INTO distribuidora_dev VALUES {ddev}")

    db.conn.commit()

    ######################## LISTA_DE_DESEJOS ###################################

    print("\n ################ INSERÇÃO DAS LISTA_DE_DESEJOS ################ ")
    print("\nA instrução realizada no BANCO DE DADOS foi:")
    lista_de_desejos = [
        ('1','4'),
        ('1','2'),
        ('2','5'),
        ('3','3'),
        ('4','8'),
        ('5','7'),
        ('1','7'),
        ('7','7'),
        ('8','6'),
        ('9','6'),
        ('7','6'),
        ('6','5'),
        ('5','5'),
        ('7','5'),
        ('9','4'),
        ('3','4'),
        ('2','4'),
        ('5','3'),
        ('6','3'),
        ('4','3'),
        ('4','2'),
        ('5','2'),
        ('6','2'),
        ('7','1'),
        ('8','8'),
        ('9','8'),
        ('6','7'),
        ('7','4'),
        ('9','2'),
        ('2','3'),
        ('3','1'),
        ('2','6'),
        ('4','7')
    ]

    for like in lista_de_desejos:
        db.cursor.execute("INSERT INTO lista_de_desejos VALUES (%s, %s)", (like[0], like[1]))
        print(f"INSERT INTO lista_de_desejos VALUES {like}")

    db.conn.commit()

    ######################## ITENS ###################################

    print("\n ################ INSERÇÃO DE ITENS ################ ")
    print("\nA instrução realizada no BANCO DE DADOS foi:")
    iten = [
        ('2', 'A big sword','Infinity Sword','50'), 
        ('7', 'Jogador 5 estrelas do PSG', 'Neymar-10','500'), 
        ('4', 'A bealtiful skin from Sonic the Movie', 'Sonic','2'), 
        ('8', 'Picareta de Roxomantium Lendaria', 'PicAxe Legendary','20'), 
        ('1', 'Uniforme do Ryu SS reverso power turbo 2.0', 'ElRYUZON','200'), 
        ('3', 'Poster Nivy Estephan dançando Dance Dance Dance em live com Castanhari', 'POSTER NC','35'), 
        ('5', 'Adicional PET: Cachorro que te segue', 'AmongCachorro','25'), 
        ('5', 'Adicional PET: Tartaruga que segue', 'AmongTartaruga','25'), 
        ('5', 'Adicional PET: Gato que te segue', 'AmongGato','25'), 
        ('7', 'Marquinhos, Jogador 4 ESTRELAS, Tropa do Ney', 'Marquinhos-4','300'), 
        ('7', 'Mbappe (tartaruga ninja) 5 ESTRELAS, Tropa do Ney ', 'Mbappe-7','400'), 
        ('7', 'Di-Maria (argentino) 3 ESTRELAS, Tropa do Ney', 'DiMaria-11','250')
        ]

    for i in iten:
        db.cursor.execute("INSERT INTO item VALUES (default, %s, %s, %s, %s)", (i[0], i[1], i[2], i[3]))
        print(f"INSERT INTO item VALUES {i}")

    db.conn.commit()

    ######################## INVENTÁRIO ###################################

    print("\n ################ INSERÇÃO DE INVENTÁRIOS ################ ")
    print("\nA instrução realizada no BANCO DE DADOS foi:")
    inventario = [
        ('1', '1'), 
        ('1', '1'), 
        ('1', '2'),
        ('2', '3'), 
        ('2', '3'),  
        ('3', '4'),
        ('3', '4'), 
        ('4', '2'), 
        ('4', '12'),
        ('4', '11'), 
        ('4', '10'),  
        ('5', '2'),  
        ('5', '10'),  
        ('5', '5'),  
        ('5', '6'),  
        ('6', '7'),  
        ('6', '8'),  
        ('6', '9'),  
        ('6', '9'),  
        ('7', '5'),  
        ('7', '6'),  
        ('7', '9'),  
        ('7', '10'),  
        ('7', '12'),  
        ('5', '11'),  
        ('6', '7'),  
        ('7', '6'),  
        ('7', '8'),  
        ('4', '10') 
        ]

    for inv in inventario:
        db.cursor.execute("INSERT INTO inventario VALUES (%s, %s)", (inv[0], inv[1]))
        print(f"INSERT INTO inventario VALUES {inv}")

    db.conn.commit()

    ######################## AMIZADES ###################################

    print("\n ################ INSERÇÃO DE AMIZADES ################ ")
    print("\nA instrução realizada no BANCO DE DADOS foi:")
    amizade = [
        ('1', '2'),
        ('2', '3'),
        ('4', '1'),
        ('3', '5'),
        ('5', '2')
    ]
    for amiz in amizade:
        db.cursor.execute("INSERT INTO amizade VALUES (%s, %s)", (amiz[0], amiz[1]))
        print(f"INSERT INTO amizade VALUES {amiz}")

    db.conn.commit()

    ######################## PACOTE ###################################

    print("\n ################ INSERÇÃO DE PACOTES ################ ")
    print("\nA instrução realizada no BANCO DE DADOS foi:")
    pacotes = [
        ('1', '1', '-5'),
        ('1', '2', '-5'),
        ('2', '3', '-3'),
        ('3', '4', '-5'),
        ('4', '4', '-3'),
        ('5', '1', '-1.99'),
        ('6', '3', '-1.87'),
        ('6', '4', '2.39'),
        ('7', '2', '-9.38'),
        ('5', '1', '-10.00'),
        ('2', '2', '-5.64')
    ]

    for p in pacotes:
        db.cursor.execute("INSERT INTO pacote VALUES (default, %s, %s, %s)", (p[0], p[1], p[2]))
        print(f"INSERT INTO pacote VALUES {p}")

    db.conn.commit()

    ######################## COMPRAS ###################################

    print("\n ################ INSERÇÃO DE COMPRAS ################ ")
    print("\nA instrução realizada no BANCO DE DADOS foi:")
    compra = [
        ('1', '1', '2', '2', '2021-03-08'),
        ('1', None, '4', '5', '2021-04-10'),
        ('2', '2', '5', None, '2021-04-19'),
        ('3', '3', '8', None, '2021-06-28'),
        ('3', None, '3', '4', '2021-01-27'),
        ('4', '2', '1', '1', '2021-02-01'),
        ('4', '2', '2', '3', '2021-02-01'),
        ('4', '2', '3', '9', '2021-02-01'),
        ('4', '1', '4', '5', '2021-02-01'),
        ('4', '3', '7', None, '2021-12-15'),
        ('5', None, '8', None, '2021-08-17')
    ]

    for com in compra:
        db.cursor.execute("INSERT INTO compra VALUES (%s, %s, %s, %s, default, %s)", (com[0], com[1], com[2], com[3], com[4]))
        print(f"INSERT INTO compra VALUES {com}")

    db.conn.commit()

    ######################## COMENTÁRIOS ###################################

    print("\n ################ INSERÇÃO DE COMENTÁRIOS ################ ")
    print("\nA instrução realizada no BANCO DE DADOS foi:")
    comentario = [
        ('1', '1', '10', 'Jogo muito bom mesmo, melhor experiencia da minha vida, parecia até que o jogo foi feito pra mim, realmente um jogoe excelente!'),
        ('4', '4', '6', 'TOP!'),
        ('4', '5', '7', 'Jogo mediano meu, parece aquele comediante que foi no meu programa o ED GAMA essa fera meu!'),
        ('4', '6', '2', 'OLOCO BIXO! QUE JOGO RUIM MEU!'),
        ('4', '7', '8', 'É bixo, esse jogo é bom mas nem tanto, ri muito jogando, parece até que estou nos RECLAMES DO PLIMPLIM! ESSA FERA MEU'),
        ('4', '8', '10', 'ESSA FERA AI EM MEU! OLOCO BIXO! QUE JOGAO VIU MEU!'),
    ]

    for coment in comentario:
        db.cursor.execute("INSERT INTO comentario VALUES(default, %s, %s, %s, %s)", (coment[0], coment[1], coment[2], coment[3]))
        print(f"INSERT INTO comentario VALUES {coment}")

    ######################## RELAÇÕES JOGO/CARACTERISTICA ###################################

    #existem:       12 traduções e dublagens
    #               4 requisitos
    #               13 categorias
    #               5 classificacoes

    print("\n ################ INSERÇÃO DAS RELAÇÕES JOGO/CARACTERISTICA ################ ")
    trad_dub_jogo = [
        ('1', '1'),
        ('2', '1'),
        ('3', '1'),
        ('4', '1'),
        ('9', '2'),
        ('3', '2'),
        ('9', '2'),
        ('12', '3'),
        ('7', '3'),
        ('3', '3'),
        ('4', '4'),
        ('5', '4'),
        ('6', '4'),
        ('5', '5'),
        ('9', '5'),
        ('6', '6'),
        ('10', '6'),
        ('11', '6'),
        ('2', '7'),
        ('1', '7'),
        ('5', '7'),
        ('6', '8'),
        ('8', '8'),
        ('9', '8'),
        ('3', '8')
    ]

    print("\nA instrução realizada no BANCO DE DADOS foi:")
    for tj in trad_dub_jogo:
        db.cursor.execute("INSERT INTO trad_jogo VALUES(%s, %s)", (tj[0], tj[1]))
        print(f"INSERT INTO trad_jogo VALUES {tj}")

    print("\nA instrução realizada no BANCO DE DADOS foi:")
    for dj in trad_dub_jogo:
        db.cursor.execute("INSERT INTO dub_jogo VALUES(%s, %s)", (dj[0], dj[1]))
        print(f"INSERT INTO dub_jogo VALUES {dj}")

    req_jogo = [
        ('1', '2'),
        ('2', '3'),
        ('3', '1'),
        ('4', '4'),
        ('5', '3'),
        ('6', '2'),
        ('7', '1'),
        ('8', '2')
    ]

    print("\nA instrução realizada no BANCO DE DADOS foi:")
    for rj in req_jogo:
        db.cursor.execute("INSERT INTO req_jogo VALUES(%s, %s)", (rj[0], rj[1]))
        print(f"INSERT INTO req_jogo VALUES {rj}")

    cat_jogo = [
        ('1', '1'),
        ('13', '2'),
        ('10', '3'),
        ('9', '4'),
        ('5', '5'),
        ('3', '6'),
        ('11', '7'),
        ('4', '8')
    ]

    print("\nA instrução realizada no BANCO DE DADOS foi:")
    for cj in cat_jogo:
        db.cursor.execute("INSERT INTO cat_jogo VALUES(%s, %s)", (cj[0], cj[1]))
        print(f"INSERT INTO cat_jogo VALUES {cj}")

    class_jogo = [
        ('1', '1'),
        ('3', '2'),
        ('4', '3'),
        ('5', '4'),
        ('2', '5'),
        ('3', '6'),
        ('1', '7'),
        ('3', '8')
    ]

    print("\nA instrução realizada no BANCO DE DADOS foi:")
    for classj in class_jogo:
        db.cursor.execute("INSERT INTO class_jogo VALUES(%s, %s)", (classj[0], classj[1]))
        print(f"INSERT INTO class_jogo VALUES {classj}")

    ######################## FIM DAS INSERÇÕES ###################################

    print("BANCO POPULADO COM SUCESSO!")
    db.conn.commit()            #Comita todas as inserções