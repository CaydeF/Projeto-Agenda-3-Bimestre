from Banco import Banco

class Clientes:
    def __init__(self, idcliente=0, nome="", nascimento="", cpf="", genero="", cidade=""):
        self.banco = Banco()
        self.idcliente = idcliente
        self.nome = nome
        self.nascimento = nascimento
        self.cpf = cpf
        self.genero = genero
        self.cidade = cidade

    def insertCliente(self):
        try:
            c = self.banco.conexao.cursor()
            c.execute("INSERT INTO tbl_clientes (nome, nascimento, cpf, genero, cidade) VALUES (?, ?, ?, ?, ?)",
                      (self.nome, self.nascimento, self.cpf, self.genero, self.cidade))
            self.banco.conexao.commit()
            c.close()
            return "Cliente cadastrado com sucesso!"
        except Exception as e:
            return f"Ocorreu um erro na inserção do cliente: {e}"

    def updateCliente(self):
        try:
            c = self.banco.conexao.cursor()
            c.execute("UPDATE tbl_clientes SET nome = ?, nascimento = ?, cpf = ?, genero = ?, cidade = ? WHERE idcliente = ?",
                      (self.nome, self.nascimento, self.cpf, self.genero, self.cidade, self.idcliente))
            self.banco.conexao.commit()
            c.close()
            return "Cliente atualizado com sucesso!"
        except Exception as e:
            return f"Ocorreu um erro na alteração do cliente: {e}"

    def deleteCliente(self):
        try:
            c = self.banco.conexao.cursor()
            c.execute("DELETE FROM tbl_clientes WHERE idcliente = ?", (self.idcliente,))
            self.banco.conexao.commit()
            c.close()
            return "Cliente excluído com sucesso!"
        except Exception as e:
            return f"Ocorreu um erro na exclusão do cliente: {e}"

    def selectCliente(self, idcliente):
        try:
            c = self.banco.conexao.cursor()
            c.execute("SELECT * FROM tbl_clientes WHERE idcliente = ?", (idcliente,))
            linha = c.fetchone()
            if linha:
                self.idcliente = linha[0]
                self.nome = linha[1]
                self.nascimento = linha[2]
                self.cpf = linha[3]
                self.genero = linha[4]
                self.cidade = linha[5]
                c.close()
                return "Busca feita com sucesso!"
            else:
                c.close()
                return "Cliente não encontrado."
        except Exception as e:
            return f"Ocorreu um erro na busca do cliente: {e}"

    def selectAllClientes(self):
        try:
            c = self.banco.conexao.cursor()
            c.execute("SELECT * FROM tbl_clientes")
            linhas = c.fetchall()
            c.close()
            return linhas
        except Exception as e:
            return f"Ocorreu um erro na recuperação dos clientes: {e}"

    def selectCidades(self):
        try:
            c = self.banco.conexao.cursor()
            c.execute("SELECT cidade FROM tbl_cidades")
            cidades = c.fetchall()
            c.close()
            return [cidade[0] for cidade in cidades]  # Retorna uma lista de nomes de cidades
        except Exception as e:
            return f"Ocorreu um erro na recuperação das cidades: {e}"
