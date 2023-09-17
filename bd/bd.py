import mysql.connector

conexao = mysql.connector.connect(host = 'localhost', user = 'root', password = 'admin')

cursor = conexao.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS bd_despysas")
print('Banco de dados bd_despysas criado')

cursor.execute('USE bd_despysas')

cursor.execute('''CREATE TABLE IF NOT EXISTS PERFILACESSO (
                idperfilacesso INT NOT NULL AUTO_INCREMENT PRIMARY KEY, 
                descricaoperfilacesso VARCHAR(100)
                );''')
print('Tabela PERFILACESSO criada')

cursor.execute('''CREATE TABLE IF NOT EXISTS USUARIO ( 
                idusuario INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                login VARCHAR(100),
                senha VARCHAR(100),
                idperfilacesso INT,
                FOREIGN KEY (idperfilacesso) REFERENCES PERFILACESSO(idperfilacesso)
                );''')
print('Tabela USUARIO criada')

cursor.execute('''CREATE TABLE IF NOT EXISTS LUCRO ( 
                idlucro INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                nomelucro VARCHAR(50),
                descricaolucro VARCHAR(100),
                valorlucro VARCHAR(10)
                );''')
print('Tabela LUCRO criada')

cursor.execute('''CREATE TABLE IF NOT EXISTS CAPITAL ( 
                idcapital INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                idlucro INT,
                FOREIGN KEY (idlucro) REFERENCES LUCRO(idlucro)
                );''')
print('Tabela CAPITAL criada')

cursor.execute('''CREATE TABLE IF NOT EXISTS CATEGORIA ( 
                idcategoria INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                nomecategoria VARCHAR(100)
                );''')
print('Tabela CATEGORIA criada')
        
cursor.execute('''CREATE TABLE IF NOT EXISTS DESPESA ( 
                iddespesa INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                nomedespesa VARCHAR(50),
                descricaodespesa VARCHAR(100),
                valordespesa VARCHAR(10),
                datainiciodespesa VARCHAR(11),
                dataFIMdespesa VARCHAR(11),
                idnpago INT,
                idcategoria INT,
                FOREIGN KEY (idcategoria) REFERENCES CATEGORIA(idcategoria)
                );''')
print('Tabela DESPESA criada')

cursor.execute('''CREATE TABLE IF NOT EXISTS PARCELA ( 
                idparcela INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                numeroparcela INT,
                idusuario INT,
                iddespesa INT,
                FOREIGN KEY (idusuario) REFERENCES USUARIO(idusuario),
                FOREIGN KEY (iddespesa) REFERENCES DESPESA(iddespesa)
                );''')
print('Tabela PARCELA criada')

cursor.execute('''INSERT INTO PERFILACESSO(descricaoperfilacesso) 
                  VALUES    ("Administrador do sistema"),
                            ("Usuário padrão");''')

conexao.commit()
print('Inserção deu certo')