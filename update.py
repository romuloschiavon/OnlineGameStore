import db

################### JOGO E SUAS CARACTERISTICAS #############################
#Como nossas caracteristica do jogo (tradução, dublagem, classificacao, categoria e requisito)
#tem a propriedade de ON UPDATE CASCADE não é necesário criar updates para as relações (JOGO/CARACTERISTICAS)
#pois essas já sofrerão alterações ao alterar id's de usuarios, ou até mesmo id's de suas características.

#jogo
def atualizar():
    print("\n##############   ATUALIZANDO JOGOS   ##############")
    jogo_update = [
        """
            UPDATE jogo 
            SET nome = 'UBSOFT GAME' from distribuidora
            WHERE jogo.id_distr = distribuidora.id_distr 
            and distribuidora.id_distr =  '4'
        """,
        """
            UPDATE jogo 
            SET nome = 'the bruxo 3' 
            WHERE  nome = 'The witcher 3'
        """
    ]

    for gameup in jogo_update:
        db.cursor.execute(gameup)
        print(f"A instrução executada foi: {gameup}")

    ##CARACTERISTICAS

    #classificações
    print("\n##############   ATUALIZANDO CLASSIFICACOES   ##############")
    classi_update = [
        """
        UPDATE classificacao 
        SET descricao = 'Classificação livre para todos os publicos. Indicado principalmente para crianças' 
        WHERE nome_class = 'Livre' ;
        """,
        """
        UPDATE classificacao
        SET id_class = '2100', nome_class = '21+ anos'
        WHERE nome_class = '18';
        """
    ]

    for c in classi_update:
        db.cursor.execute(c)
        print(f"A instrução executada foi: {c}")

    #dublagens
    print("\n##############   ATUALIZANDO DUBLAGENS   ##############")
    dub_updates = [
        """
        UPDATE dublagem
        SET idioma_dublagem = 'pt_BR', id_dublagem = '2100'
        WHERE idioma_dublagem = 'Portugues - BR';
        """,
        """
        UPDATE dublagem
        set idioma_dublagem = 'en_US', id_dublagem = '3000'
        WHERE idioma_dublagem = 'Inglês';
        """
    ]

    for d in dub_updates:
        db.cursor.execute(d)
        print(f"A instrução executada foi: {d}")

    #traducoes
    print("\n##############   ATUALIZANDO TRADUCOES   ##############")
    trad_updates = [
        """
        UPDATE traducao
        SET idioma_traducao = 'pt_BR', id_traducao = '2100'
        WHERE idioma_traducao = 'Portugues - BR';
        """,
        """
        UPDATE traducao
        set idioma_traducao = 'en_US', id_traducao = '3000'
        WHERE idioma_traducao = 'Inglês';
        """
    ]

    for t in trad_updates:
        db.cursor.execute(t)
        print(f"A instrução executada foi: {t}")

    #categorias
    print("\n##############   ATUALIZANDO CATEGORIAS   ##############")
    categoria_updates = [
        """
        UPDATE categoria
        SET id_categ = '10102020'
        WHERE id_categ = '1' or nome LIKE '%MMORPG%';
        """,
        """
        UPDATE categoria
        SET nome = 'MMORPG'
        WHERE descricao LIKE '%Massively%';
        """
    ]

    for categ in categoria_updates:
        db.cursor.execute(categ)
        print(f"A instrução executada foi: {categ}")

    #requisitos
    print("\n##############   ATUALIZANDO REQUISITOS   ##############")
    requisito_updates = [
        """
        UPDATE requisito
        SET os = 'Windows 10, Linux and MacOS'
        WHERE os LIKE '%linux%' and processador LIKE '%Intel%';
        """,
        """
        UPDATE requisito
        set placa_de_video = 'nVidia GEFORCE GTX 2080 SUPER'
        where armazenamento LIKE '%50%' or armazenamento LIKE '%20%__' or armazenamento LIKE '%60%__' and os LIKE '%Windows%';
        """
    ]

    for requis in requisito_updates:
        db.cursor.execute(requis)
        print(f"A instrução executada foi: {requis}")


    #desenvolvedores
    print("\n##############   ATUALIZANDO DESENVOLVEDORES   ##############")
    dev_updates = [
        """
        UPDATE dev
        SET id_dev = '99999'
        WHERE nome_dev = 'Ana Vitória';
        """,
        """
        UPDATE dev
        SET nome_dev = 'Calouro UFSC Rodrigo Fernandes'
        WHERE id_dev = '1';
        """,
    ]

    for dev in dev_updates:
        db.cursor.execute(dev)
        print(f"A instrução executada foi: {dev}")

    #itens                  aqui o objetivo é editar o jogo que "dropa" o determinado item, ou as caracteristicas dele, como valor etc...
    print("\n##############   ATUALIZANDO ITENS   ##############")
    item_updates = [
        """
        UPDATE item
        SET valor = '1243'
        WHERE nome LIKE '%Neymar%' or id_jogo = '3';
        """,
        """
        UPDATE item
        SET nome = 'Picareta de diamante', descricao='Picareta de diamante do minecraft', valor = '350'
        WHERE id_item = '4' or id_jogo = '1';
        """
    ]

    for it in item_updates:
        db.cursor.execute(it)
        print(f"A instrução executada foi: {it}")

    #amizades
    print("\n##############   ATUALIZANDO AMIZADES   ##############")
    amizade_updates = [
        """
        UPDATE amizade
        SET id_user = '1', possui_id_user = '2'
        WHERE id_user = '5';
        """,
        """
        UPDATE amizade
        SET id_user = '4', possui_id_user = '1'
        WHERE possui_id_user = '2';
        """
    ]

    for amigs in amizade_updates:
        db.cursor.execute(amigs)
        print(f"A instrução executada foi: {amigs}")

    #lista de desejos
    #print("\n##############   ATUALIZANDO LISTA_DE_DESEJOS   ##############")
    #desejos_updates = [
    #    """
    #    UPDATE lista_de_desejos
    #    SET id_jogo = '7'
    #    WHERE id_user = '5' or id_jogo = '3';
    #    """,
    #    """
    #    UPDATE lista_de_desejos
    #    SET id_jogo = '5'
    #    WHERE id_jogo = '4' and id_user = '2';
    #    """
    #]
    #
    #for desejos in desejos_updates:
    #    db.cursor.execute(desejos)
    #    print(f"A instrução executada foi: {desejos}")

    #inventario
    print("\n##############   ATUALIZANDO INVENTARIO   ##############")
    inventario_updates = [
        """
        UPDATE inventario
        SET id_item = '2'
        WHERE id_user = '4';
        """,
        """
        UPDATE inventario
        SET id_user = '2'
        WHERE id_item = '1' and id_user='1';
        """
    ]

    for inventario in inventario_updates:
        db.cursor.execute(inventario)
        print(f"A instrução executada foi: {inventario}")

    #distribuidoras
    print("\n##############   ATUALIZANDO DISTRIBUIDORAS   ##############")
    distr_update = [
        """
            UPDATE distribuidora 
            SET endereco = 'Rua alcino de abreu, 2555, Sao Paulo' 
            WHERE NOME_FANTASIA = 'Kootly' 
        """,
        """
            UPDATE distribuidora SET NOME_FANTASIA  = 'EASPORTS' 
            WHERE cnpj = '55555555555555' 
        """
    ]

    for du in distr_update:
        db.cursor.execute(du)
        print(f"A instrução executada foi: {du}")

    #usuarios
    print("\n##############   ATUALIZANDO USUARIOS   ##############")
    user_update = [
        """
            UPDATE usuario 
            SET username = 'XxXMariahXxX' 
            WHERE email = 'mariazinha@gmail.com' 
        """,
            """
            UPDATE usuario 
            SET email = 'jozerodrigo@gmail.com' 
            WHERE id_user = '5' and data_nascimento = '2005-02-20'
        """
    ]

    for us in user_update:
        db.cursor.execute(us)
        print(f"A instrução executada foi: {us}")

    #expansao
    print("\n##############   ATUALIZANDO EXPANSÕES   ##############")
    expansao_update = [
        """
            UPDATE expansao 
            SET descricao = 'Expansão em manutenção, favor esperar.' 
            from pacote,jogo WHERE jogo.id_jogo = 3
            and pacote.id_jogo = jogo.id_jogo
            and  expansao.id_expansao = pacote.id_expansao
        """
    ]

    for exup in expansao_update:
        db.cursor.execute(exup)
        print(f"A instrução executada foi: {exup}")

    #compra
    print("\n##############   ATUALIZANDO COMPRAS   ##############")
    compra_update = [
        """
            UPDATE compra 
            SET id_jogo = '2'
            WHERE id_jogo = '3'
        """,
        """
            UPDATE compra 
            SET id_item = '4'
            WHERE id_item = '1'
        """
    ]

    for comup in compra_update:
        db.cursor.execute(comup)
        print(f"A instrução executada foi: {comup}")

    #Atualização desnecessária devido ao CASCADE
    #Relação DIST_DEV
    #print("\n##############   ATUALIZANDO DISTRIBUIDORA_DEV   ##############")
    #
    #distDev_update = [
    #    """
    #        UPDATE distribuidora_dev 
    #        SET id_dev = '2'
    #        WHERE id_distr = '4' and id_dev = 5
    #    """,
    #      """
    #        UPDATE distribuidora_dev 
    #        SET id_distr = '2'
    #        WHERE id_distr = '1' and id_dev = 4
    #    """
    #]
    #
    #for distrDevUp in distDev_update:
    #    db.cursor.execute(distrDevUp)
    #    print(f"A instrução executada foi: {distrDevUp}")

    #comentario
    print("\n##############   ATUALIZANDO COMENTARIOS   ##############")
    comentario_updates = [
        """
            UPDATE comentario 
            SET nota = '5', descricao = 'agora achei ruim *-*  '
            WHERE id_user = '1'
        """
    ]

    for coment in comentario_updates:
        db.cursor.execute(coment)
        print(f"as alterações foram: {coment}")

    #pacotes
    print("\n##############   ATUALIZANDO PACOTES   ##############")
    pacote_update = [
        """
            UPDATE pacote 
            SET desconto_pac = '-3.99' 
            WHERE id_jogo = '1'
        """
    ]

    for pac_up in pacote_update:
        db.cursor.execute(pac_up)
        print(f"as alterações foram: {pac_up}")

    print("BANCO ATUALIZADO COM SUCESSO!")
    db.conn.commit()