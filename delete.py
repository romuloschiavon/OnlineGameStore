import db 

def excluir():
    ##################################################################
    #! CLASSIFICACAO
    ##################################################################

    delete_classificacao = [
        """
        DELETE FROM classificacao
        WHERE id_class = 1
        """,
        """
        DELETE FROM classificacao 
        WHERE faixa_etaria = '+18'
        """
    ]
    for del_clas in delete_classificacao:
        db.cursor.execute(del_clas)
        print(f"A instrução executada foi:\n {del_clas}")

    ##################################################################
    #! DISTRIBUIDORA
    ##################################################################

    delete_distr = [
        """
        DELETE FROM distribuidora
        WHERE nome_fantasia = 'UBSOFT'
        """,
        """
        DELETE FROM distribuidora 
        WHERE email = 'bluepco@gmail.com'
        """
    ]
    for del_distr in delete_distr:
        db.cursor.execute(del_distr)
        print(f"A instrução executada foi:\n {del_distr}")

    ##################################################################
    #! USUARIO
    ##################################################################

    delete_usuario = [
        """ 
        DELETE FROM usuario
        WHERE email = 'josemaria@gmail.com'
        """
    ]
    for del_user in delete_usuario:
        db.cursor.execute(del_user)
        print(f"A instrução executada foi:\n {del_user}")

    ##################################################################
    #! JOGO
    ##################################################################
    delete_jogo = [
        """ 
        DELETE FROM jogo
        WHERE nome = 'UBSOFT GAME'
        """,
        """ 
        DELETE FROM JOGO 
        WHERE id_jogo = '4'
        """
    ]
    for del_jogo in delete_jogo:
        db.cursor.execute(del_jogo)
        print(f"A instrução executada foi:\n {del_jogo}")

    ##################################################################
    #! EXPANSAO
    ##################################################################
    delete_expansao = [
        """ 
        DELETE FROM expansao
        WHERE nome = 'Divindo da morte'
        """,
        """
        DELETE FROM expansao 
        WHERE id_expansao = '4'
        """
    ]
    for del_exp in delete_expansao:
        db.cursor.execute(del_exp)
        print(f"A instrução executada foi:\n {del_exp}")

    ##################################################################
    #! COMPRA
    ##################################################################
    delete_compra = [
        """ 
        DELETE FROM compra
        WHERE id_user = '4' and id_pacote='3'
        """
        ]
    for del_compra in delete_compra:
        db.cursor.execute(del_compra)
        print(f"A instrução executada foi:\n {del_compra}")

    ##################################################################
    #! DISTR-DEV
    ##################################################################
    delete_dist_dev = [
        """ 
        DELETE FROM distribuidora_dev
        WHERE id_dev = '2' and id_distr='2'
        """
        ]
    for del_dist_dev in delete_dist_dev:
        db.cursor.execute(del_dist_dev)
        print(f"A instrução executada foi:\n {del_dist_dev}")

    ##################################################################
    #! COMENTARIO
    ##################################################################
    delete_comentario = [
        """ 
        DELETE FROM comentario
        WHERE id_user = '4'
        """
        ]
    for del_coment in delete_comentario:
        db.cursor.execute(del_coment)
        print(f"A instrução executada foi:\n {del_coment}")

    ##################################################################
    #! PACOTE
    ##################################################################
    delete_pacote = [
        """ 
        DELETE FROM pacote
        WHERE id_expansao = '2' and desconto_pac > -10 
        """
        ]
    for del_pac in delete_pacote:
        db.cursor.execute(del_pac)
        print(f"A instrução executada foi:\n {del_pac}")

    ##################################################################
    #! DUBLAGEM
    ##################################################################
    delete_dublagem = [
        """ 
        DELETE FROM dublagem
        WHERE idioma_dublagem = 'Japonês'
        """
        ]
    for del_dub in delete_dublagem:
        db.cursor.execute(del_dub)
        print(f"A instrução executada foi:\n {del_dub}")

    ##################################################################
    #! TRADUCAO
    ##################################################################
    delete_traducao = [
        """ 
        DELETE FROM traducao
        WHERE id_traducao = '5'
        """
        ]
    for del_trad in delete_traducao:
        db.cursor.execute(del_trad)
        print(f"A instrução executada foi:\n {del_trad}")

    ##################################################################
    #! DEV
    ##################################################################
    delete_dev = [
        """ 
        DELETE FROM  dev
        WHERE id_dev = '4';
        """,
        """
        DELETE FROM  dev
        WHERE id_dev = '1';    
        """
        ]
    for del_dev in delete_dev:
        db.cursor.execute(del_dev)
        print(f"A instrução executada foi:\n {del_dev}")

    ##################################################################
    #! ITEM
    ##################################################################
    delete_item = [
        """ 
        DELETE FROM  item
        WHERE id_item = '4'
        """
        ]
    for del_item in delete_item:
        db.cursor.execute(del_item)
        print(f"A instrução executada foi:\n {del_item}")

    ##################################################################
    #! CATEGORIA
    ##################################################################

    delete_categ = [
        """ 
        DELETE FROM  categoria
        WHERE id_categ >=12 
        """,
        """
        DELETE FROM  categoria
        WHERE nome = 'Single Player' or nome ='MMO'
        """
        ]
    for del_cat in delete_categ:
        db.cursor.execute(del_cat)
        print(f"A instrução executada foi:\n {del_cat}")

    ##################################################################
    #! REQUISITO
    ##################################################################

    delete_req = [
        """
        DELETE FROM  requisito
        WHERE id_requis = '3';
        """,
        """
        DELETE FROM  requisito
        WHERE memoria = '8GB';
        """    
    ]

    for del_req in delete_req:
        db.cursor.execute(del_req)
        print(f"A instrução executada foi:\n {del_req}")

    ##################################################################
    #! AMIZADE
    ##################################################################

    delete_amizade = [
        """
        DELETE from amizade
        WHERE possui_id_user = '5'
        """,
        """
        DELETE from amizade
        WHERE possui_id_user = '3'
        """
    ]

    for del_amiz in delete_amizade:
        db.cursor.execute(del_amiz)
        print(f"A instrução executada foi:\n {del_amiz}")

    ##################################################################
    #! LISTA_DE_DESEJOS
    ##################################################################

    delete_lista_de_desejos = [
        """
        DELETE FROM lista_de_desejos
        WHERE ID_JOGO = '5';
        """,
        """
        DELETE FROM lista_de_desejos
        WHERE ID_USER = '2';
        """
    ]

    for del_lista_de_desejos in delete_lista_de_desejos:
        db.cursor.execute(del_lista_de_desejos)
        print(f"A instrução executada foi:\n {del_lista_de_desejos}")

    ##################################################################
    #! INVENTARIO
    ##################################################################

    delete_inventario = [
        """
        DELETE FROM inventario
        WHERE ID_USER = '1';
        """
    ]

    for del_inv in delete_inventario:
        db.cursor.execute(del_inv)
        print(f"A instrução executada foi:\n {del_inv}")

    ##################################################################
    #! Para as relações entre jogo/carac e dev/distr não foram criados deletes,
    #! Pois assim como no update é válido dizer que como são sempre duas chaves secundárias
    #! Para esse tipo de UPDATE/DELETE, ao colocarmos o CASCADE as alterações realizadas
    #! Na sua origem se refletem nas relações.
    ##################################################################

    print("ALGUNS DADOS DO BANCO FORAM EXCLUIDOS COM SUCESSO!")
    db.conn.commit()