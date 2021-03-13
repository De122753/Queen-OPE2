--Autor: Fabiano Sato
--DataCreate: 09/03/2021
--Objetivo: Script para criar Banco de Dados, Tabelas e Seus relacionamentos conforme documentação

USE master
GO

/*#################################################### Criar Banco de Dados ####################################################################*/

CREATE DATABASE SIIC
GO

USE SIIC
/*######################################################## Criar Tabelas #######################################################################*/
GO
--Cria Tabela Usuario
/*CREATE TABLE [dbo].[Usuario]
	(
		[id] INT NOT NULL IDENTITY(1,1),
		[nome] VARCHAR(255) NOT NULL UNIQUE,
		[username] VARCHAR(50) NOT NULL,
		[senha] VARCHAR(255) NOT NULL,
		[funcao] VARCHAR(255) NOT NULL,
		[nivel] VARCHAR(50) NOT NULL,
		[data_registro] DATETIME NOT NULL, 
		[data_exclusao] DATETIME NULL,
		CONSTRAINT PK_id_usuario PRIMARY KEY (id)
	)
*/
GO
--Cria Tabela Pedido
/*CREATE TABLE [dbo].[Pedido]
	(
		[id] INT NOT NULL IDENTITY (1,1),
		[num_pedido] INT NOT NULL,
		[data_pedido] DATETIME NOT NULL,
		[usuario_id] INT NOT NULL,
		[produto_id] INT NOT NULL,
		[produto_qtd] INT NOT NULL,
		[produto_desconto] DECIMAL (6,2) NOT NULL,
		[preco_frete] DECIMAL (6,2) NOT NULL,
		[fornecedor_id] INT NOT NULL,
		[preco_item] DECIMAL (6,2) NOT NULL,
		[preco_total] AS [produto_qtd] * [preco_item] PERSISTED,
		[pedido_validacao] BIT NOT NULL,
		[nota_fiscal] INT NOT NULL,
		CONSTRAINT PK_id_pedido PRIMARY KEY (id)
	)
*/
GO
--Cria Tabela Fornecedor
/*CREATE TABLE [dbo].[Fornecedor]
	(
		[id] INT NOT NULL IDENTITY (1,1),
		[nome] VARCHAR(255) NOT NULL UNIQUE, 
		[cnpj] VARCHAR(50) NOT NULL UNIQUE,
		[telefone] INT NOT NULL,
		[email] VARCHAR(50) NOT NULL,
		[logradouro] VARCHAR(255) NULL,
		[numero] INT NULL,
		[complemento] VARCHAR(255) NULL,
		[cidade] VARCHAR(255) NULL,
		[estado] VARCHAR(255) NULL,
		[cep] INT NULL,
		[data_inclusao] DATETIME NOT NULL,
		CONSTRAINT PK_id_fornecedor PRIMARY KEY (id)
	)
*/
GO
--Cria Tabela Tabela Protudo
/*CREATE TABLE [dbo].[Produto]
	(
		[id] [INT] NOT NULL IDENTITY(1,1),
		[identificador] INT NOT NULL,
		[nome] VARCHAR(255) NOT NULL,
		[categoria] VARCHAR(255) NOT NULL,
		[tamanho] CHAR(3) NOT NULL,
		[cor] CHAR(50) NOT NULL,
		[descricao] VARCHAR(255) NOT NULL,
		[preco_compra] DECIMAL(6,2) NOT NULL,
		[preco_venda] DECIMAL(6,2) NOT NULL,
		[quantidade_minima] INT NOT NULL,
		[fornecedor_id] INT NOT NULL,
		PK_id_produto PRIMARY KEY (id),
	)
*/
GO
--Cria Tabela Movimentacao
/*CREATE TABLE [dbo].[Movimentacao]
	(
		[id] INT NOT NULL IDENTITY(1,1),
		[produto_id] INT NOT NULL,
		[qtd_produto] INT NOT NULL,
		[data_movimento] DATETIME NOT NULL,
		[tipo_movimento] VARCHAR(255) NOT NULL,
		[nota_fiscal] INT NOT NULL,
		CONSTRAINT PK_id_movimentacao PRIMARY KEY (id), 
	)
*/
GO
--Cria Tabela Estoque
/*CREATE TABLE [dbo].[Estoque]
	(
		[id] [INT] NOT NULL IDENTITY(1,1),
		[produto_id] INT NOT NULL,
		[quantidade] INT NOT NULL,
		[dataEntrada] DATETIME NOT NULL,
		[dataSaida] DATETIME NOT NULL,
		CONSTRAINT PK_id_estoque PRIMARY KEY (id), 

	)
*/
GO

/*############################################### Criar Relacionamento das Tabelas ############################################################*/
/*
ALTER TABLE [dbo].[Produto] WITH CHECK ADD CONSTRAINT FK_Produto_Fornecedor FOREIGN KEY (fornecedor_id) REFERENCES Fornecedor (id)
GO
ALTER TABLE [dbo].[Movimentacao] WITH CHECK ADD  CONSTRAINT FK_Movimentacao_Produto FOREIGN KEY (produto_id) REFERENCES Produto (id)
GO
ALTER TABLE [dbo].[Estoque] WITH CHECK ADD CONSTRAINT FK_Estoque_Produto FOREIGN KEY (produto_id) REFERENCES Produto (id)
GO
ALTER TABLE [dbo].[Pedido] WITH CHECK ADD CONSTRAINT FK_Pedido_Usuario FOREIGN KEY (usuario_id) REFERENCES Usuario (id)
GO
ALTER TABLE [dbo].[Pedido] WITH CHECK ADD CONSTRAINT FK_Pedido_Produto FOREIGN KEY (produto_id) REFERENCES Produto (id)
GO
ALTER TABLE [dbo].[Pedido] WITH CHECK ADD CONSTRAINT FK_Pedido_Fornecedor FOREIGN KEY (fornecedor_id) REFERENCES Fornecedor (id)
*/
GO
/*############################################### Deletar Relacionamento das Tabelas #########################################################*/

/*
ALTER TABLE [dbo].[Produto] DROP CONSTRAINT FK_Produto_Fornecedor
GO
ALTER TABLE [dbo].[Movimentacao] DROP CONSTRAINT FK_Movimentacao_Produto
GO
ALTER TABLE [dbo].[Estoque]  DROP CONSTRAINT FK_Estoque_Produto
GO
ALTER TABLE [dbo].[Pedido]  DROP CONSTRAINT FK_Pedido_Usuario
GO
ALTER TABLE [dbo].[Pedido]  DROP CONSTRAINT FK_Pedido_Produto
GO
ALTER TABLE [dbo].[Pedido]  DROP CONSTRAINT FK_Pedido_Fornecedor
*/
GO
/*######################################################### Deletar Tabelas #################################################################*/

/*
DROP TABLE [dbo].[Usuario]
GO
DROP TABLE [dbo].[Pedido]
GO
DROP TABLE [dbo].[Fornecedor]
GO
DROP TABLE [dbo].[Produto]
GO
DROP TABLE [dbo].[Movimentacao]
GO
DROP TABLE [dbo].[Estoque]

*/
GO
/*##################################################### Deletar Banco de Dados #############################################################*/

--DROP DATABASE SIIC
GO
/*########################################################## INSERT DADOS ##################################################################*/
GO

--Inserir Dados Tabela Usuário
/*
INSERT INTO Usuario (nome, username, senha, funcao, nivel, data_registro, data_exclusao) VALUES ('Fabiano','fsato','teste@123','DBA','ADMIN',GETDATE(),NULL)
GO
INSERT INTO Usuario (nome, username, senha, funcao, nivel, data_registro, data_exclusao) VALUES ('Alex','acarvalho','teste@321','DEVELOPER','ADMIN',GETDATE(),NULL)
GO
INSERT INTO Usuario (nome, username, senha, funcao, nivel, data_registro, data_exclusao) VALUES ('Maria','msouza','teste@111','ESTOQUISTA','USUARIO',GETDATE(),NULL)
GO
INSERT INTO Usuario (nome, username, senha, funcao, nivel, data_registro, data_exclusao) VALUES ('João','jcosta','teste@321','ENCARREGADO','USUARIO',GETDATE(),NULL)
GO
--INSERT INTO Usuario (nome, username, senha, funcao, nivel, data_registro, data_exclusao) VALUES ('Fabiano','fsato',hashbytes('sha2_512','teste@123'),'') alterar na tabela o campo senha para varbinary(1000) 
*/
GO

--Inserir Dados Tabela Fornecedor
/*
INSERT INTO [dbo].[Fornecedor]([nome],[cnpj],[telefone],[email],[logradouro],[numero],[complemento],[cidade],[estado],[cep],[data_inclusao])
     VALUES
           ('KingEstoque','111114444444/0001-22',11222233,'corporativo@kingestoque.com.br','Rua brasil',41,'Prédio 2','São Bernardo do Campo','São Paulo',333333333,GETDATE())
*/
GO

--Inserir Dados Tabela Produto
/*
INSERT INTO [dbo].[Produto]([identificador],[nome],[categoria],[tamanho],[cor],[descricao],[preco_compra],[preco_venda],[quantidade_minima],[fornecedor_id])
     VALUES
           (00001,'Calça','Jeans','M','Azul','Coleção de Inverno',35.5,64,5,1)
*/
GO

--Inserir Dados Tabela Pedido
/*
INSERT INTO Pedido ([num_pedido],[data_pedido],[usuario_id],[produto_id],[produto_qtd],[produto_desconto],[preco_frete],[fornecedor_id],
[preco_item],[pedido_validacao],[nota_fiscal])
     VALUES
           (1,GETDATE(),1,2,2,2.5,12,1,25,0,1)
*/
GO

--Inserir Dados Tabela Estoque
/*
INSERT INTO [dbo].[Estoque]([produto_id],[quantidade],[dataEntrada],[dataSaida])
     VALUES
           (2,7,'2021-02-15 16:37:00.000','2021-03-10 22:57:16.800')
*/
GO

--Inserir Dados Tabela Movimentacao
/*
INSERT INTO [dbo].[Movimentacao]([produto_id],[qtd_produto],[data_movimento],[tipo_movimento],[nota_fiscal])
     VALUES
           (2,2,'2021-03-10 22:57:16.800','VENDA',1)
*/
GO

/*########################################################## CONSULTA DADOS #################################################################*/
--PESQUISA
SELECT * FROM Usuario
GO
SELECT * FROM Fornecedor
GO
SELECT * FROM Produto
GO
SELECT * FROM Pedido
GO
SELECT * FROM Estoque
GO
SELECT * FROM Movimentacao
GO
/*##################################################### Limpeza de Dados Tabela ##############################################################*/
GO
--delete Usuario where id = 1
--delete Produto where 
--TRUNCATE TABLE Usuario

GO

/*######################################################## Trigger de Tabelas ################################################################*/
GO
--Criar Trigger na tabela Pedido para atualizar tabela de Movimento
/*
CREATE TRIGGER TGR_INSERT_MOVIMENTO
ON Pedido
FOR INSERT
AS
BEGIN
    DECLARE
    @produto_id INT,
	@produto_qtd INT,
	@DATA DATETIME,
	@tipo_movimento VARCHAR(255),
	@NF INT
 
    SELECT @produto_id = produto_id, @produto_qtd = produto_qtd, @DATA = GETDATE(), @tipo_movimento = 'VENDA', @NF = nota_fiscal FROM INSERTED
 
    INSERT INTO [dbo].[Movimentacao]([produto_id],[qtd_produto],[data_movimento],[tipo_movimento],[nota_fiscal])
		VALUES (@produto_id, @produto_qtd, @DATA, @tipo_movimento, @NF)
END
*/
GO