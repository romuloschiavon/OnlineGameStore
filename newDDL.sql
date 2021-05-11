CREATE TABLE DUBLAGEM (
ID_DUBLAGEM SERIAL PRIMARY KEY,
IDIOMA_DUBLAGEM VARCHAR(20)
);
--delete ok

CREATE TABLE CLASSIFICACAO (
ID_CLASS SERIAL PRIMARY KEY,
NOME_CLASS VARCHAR(20),
FAIXA_ETARIA VARCHAR(4),
DESCRICAO VARCHAR(200)
);
--delete ok

CREATE TABLE DISTRIBUIDORA (
ID_DISTR SERIAL PRIMARY KEY,
NOME_FANTASIA VARCHAR(30),
EMAIL VARCHAR(50) UNIQUE,
ENDERECO VARCHAR(50),
CNPJ NUMERIC UNIQUE
);
--delete ok

CREATE TABLE ITEM (
ID_ITEM SERIAL PRIMARY KEY,
ID_JOGO INTEGER,
DESCRICAO VARCHAR(200),
NOME VARCHAR(50),
VALOR NUMERIC
);
--delete ok

CREATE TABLE USUARIO (
ID_USER SERIAL PRIMARY KEY,
EMAIL VARCHAR(100) UNIQUE,
USERNAME VARCHAR(20),
NOME VARCHAR(50),
DATA_NASCIMENTO TIMESTAMP
);
--delete ok

CREATE TABLE CATEGORIA (
ID_CATEG SERIAL PRIMARY KEY,
DESCRICAO VARCHAR(200),
NOME VARCHAR(30)
);
--delete ok

CREATE TABLE JOGO (
ID_JOGO SERIAL PRIMARY KEY,
ID_DISTR INTEGER,
NOME VARCHAR(50),
DATA_DE_LANCAMENTO TIMESTAMP,
DESCRICAO VARCHAR(500),
VALOR NUMERIC,
FOREIGN KEY(ID_DISTR) REFERENCES DISTRIBUIDORA (ID_DISTR) ON UPDATE CASCADE ON DELETE SET NULL
);
--delete ok

CREATE TABLE REQUISITO (
ID_REQUIS SERIAL PRIMARY KEY,
PLACA_DE_VIDEO VARCHAR(50),
ARMAZENAMENTO VARCHAR(100),
OS VARCHAR(50),
MEMORIA VARCHAR(50),
PROCESSADOR VARCHAR(50)
);
--delete ok

CREATE TABLE EXPANSAO (
ID_EXPANSAO SERIAL PRIMARY KEY,
NOME VARCHAR(50),
DESCRICAO VARCHAR(200),
VALOR NUMERIC
);
--delete ok

CREATE TABLE TRADUCAO (
IDIOMA_TRADUCAO VARCHAR(20),
ID_TRADUCAO SERIAL PRIMARY KEY
);
--delete ok

CREATE TABLE DEV (
ID_DEV SERIAL PRIMARY KEY,
NOME_DEV VARCHAR(50)
);
--delete ok

CREATE TABLE AMIZADE (
ID_USER INTEGER,
possui_ID_USER INTEGER
);
--delete ok

CREATE TABLE COMPRA (
ID_USER INTEGER,
ID_ITEM INTEGER NULL,
ID_JOGO INTEGER NULL,
ID_PACOTE INTEGER NULL,
ID_COMPRA SERIAL UNIQUE,
DATA_COMPRA TIMESTAMP,
PRIMARY KEY(ID_COMPRA),
FOREIGN KEY(ID_USER) REFERENCES USUARIO (ID_USER) ON UPDATE CASCADE ON DELETE SET NULL,
FOREIGN KEY(ID_ITEM) REFERENCES ITEM (ID_ITEM) ON UPDATE CASCADE ON DELETE SET NULL,
FOREIGN KEY(ID_JOGO) REFERENCES JOGO (ID_JOGO) ON UPDATE CASCADE ON DELETE SET NULL
);
--delete ok

CREATE TABLE LISTA_DE_DESEJOS (
ID_JOGO INTEGER,
ID_USER INTEGER,
PRIMARY KEY(ID_JOGO,ID_USER),
FOREIGN KEY(ID_JOGO) REFERENCES JOGO (ID_JOGO) ON UPDATE CASCADE ON DELETE CASCADE,
FOREIGN KEY(ID_USER) REFERENCES USUARIO (ID_USER) ON UPDATE CASCADE ON DELETE CASCADE
);
--delete ok

CREATE TABLE DISTRIBUIDORA_DEV (
ID_DEV INTEGER,
ID_DISTR INTEGER,
FOREIGN KEY(ID_DEV) REFERENCES DEV (ID_DEV) ON UPDATE CASCADE ON DELETE CASCADE,
FOREIGN KEY(ID_DISTR) REFERENCES DISTRIBUIDORA (ID_DISTR) ON UPDATE CASCADE ON DELETE CASCADE
);
--delete ok

CREATE TABLE INVENTARIO (
ID_USER INTEGER,
ID_ITEM INTEGER,
FOREIGN KEY(ID_USER) REFERENCES USUARIO (ID_USER) ON UPDATE CASCADE ON DELETE SET NULL,
FOREIGN KEY(ID_ITEM) REFERENCES ITEM (ID_ITEM) ON UPDATE CASCADE ON DELETE CASCADE
);
--delete ok

CREATE TABLE COMENTARIO (
ID_COMENT SERIAL PRIMARY KEY,
ID_USER INTEGER,
ID_JOGO INTEGER,
NOTA NUMERIC,
DESCRICAO VARCHAR(200),
FOREIGN KEY(ID_USER) REFERENCES USUARIO (ID_USER) ON UPDATE CASCADE ON DELETE CASCADE,
FOREIGN KEY(ID_JOGO) REFERENCES JOGO (ID_JOGO) ON UPDATE CASCADE ON DELETE CASCADE
);
--delete ok

CREATE TABLE PACOTE (
ID_PACOTE SERIAL PRIMARY KEY,
ID_JOGO INTEGER,
ID_EXPANSAO INTEGER,
DESCONTO_PAC NUMERIC,
FOREIGN KEY(ID_JOGO) REFERENCES JOGO (ID_JOGO) ON UPDATE CASCADE ON DELETE SET NULL,
FOREIGN KEY(ID_EXPANSAO) REFERENCES EXPANSAO (ID_EXPANSAO) ON UPDATE CASCADE ON DELETE CASCADE
);
--delete ok

CREATE TABLE CLASS_JOGO (
ID_CLASS INTEGER,
ID_JOGO INTEGER,
FOREIGN KEY(ID_CLASS) REFERENCES CLASSIFICACAO (ID_CLASS) ON UPDATE CASCADE ON DELETE CASCADE,
FOREIGN KEY(ID_JOGO) REFERENCES JOGO (ID_JOGO) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE TRAD_JOGO (
ID_TRADUCAO INTEGER,
ID_JOGO INTEGER,
FOREIGN KEY(ID_TRADUCAO) REFERENCES TRADUCAO (ID_TRADUCAO) ON UPDATE CASCADE ON DELETE CASCADE,
FOREIGN KEY(ID_JOGO) REFERENCES JOGO (ID_JOGO) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE DUB_JOGO (
ID_DUBLAGEM INTEGER,
ID_JOGO INTEGER,
FOREIGN KEY(ID_DUBLAGEM) REFERENCES DUBLAGEM (ID_DUBLAGEM) ON UPDATE CASCADE ON DELETE CASCADE,
FOREIGN KEY(ID_JOGO) REFERENCES JOGO (ID_JOGO) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE CAT_JOGO (
ID_CATEG INTEGER,
ID_JOGO INTEGER,
FOREIGN KEY(ID_CATEG) REFERENCES CATEGORIA (ID_CATEG) ON UPDATE CASCADE ON DELETE CASCADE,
FOREIGN KEY(ID_JOGO) REFERENCES JOGO (ID_JOGO) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE REQ_JOGO (
ID_JOGO INTEGER,
ID_REQUIS INTEGER,
FOREIGN KEY(ID_JOGO) REFERENCES JOGO (ID_JOGO) ON UPDATE CASCADE ON DELETE CASCADE,
FOREIGN KEY(ID_REQUIS) REFERENCES REQUISITO (ID_REQUIS) ON UPDATE CASCADE ON DELETE CASCADE
);

ALTER TABLE ITEM ADD FOREIGN KEY(ID_JOGO) REFERENCES JOGO (ID_JOGO) ON UPDATE CASCADE ON DELETE CASCADE;
ALTER TABLE COMPRA ADD FOREIGN KEY(ID_PACOTE) REFERENCES PACOTE (ID_PACOTE) ON UPDATE CASCADE ON DELETE SET NULL;
