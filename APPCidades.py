from Banco import Banco

class Cidades:
    def __init__(self, idcidade=0, cidade="", uf=""):
        self.banco = Banco()
        self.idcidade = idcidade
        self.cidade = cidade
        self.uf = uf

    def insertCidade(self):
        try:
            c = self.banco.conexao.cursor()
            c.execute("INSERT INTO tbl_cidades (cidade, uf) VALUES (?, ?)",
                      (self.cidade, self.uf))
            self.banco.conexao.commit()
            c.close()
            return "Cidade cadastrada com sucesso!"
        except Exception as e:
            return f"Ocorreu um erro na inserção da cidade: {e}"

    def updateCidade(self):
        try:
            c = self.banco.conexao.cursor()
            c.execute("UPDATE tbl_cidades SET cidade = ?, uf = ? WHERE idcidade = ?",
                      (self.cidade, self.uf, self.idcidade))
            self.banco.conexao.commit()
            c.close()
            return "Cidade atualizada com sucesso!"
        except Exception as e:
            return f"Ocorreu um erro na alteração da cidade: {e}"

    def deleteCidade(self):
        try:
            c = self.banco.conexao.cursor()
            c.execute("DELETE FROM tbl_cidades WHERE idcidade = ?", (self.idcidade,))
            self.banco.conexao.commit()
            c.close()
            return "Cidade excluída com sucesso!"
        except Exception as e:
            return f"Ocorreu um erro na exclusão da cidade: {e}"

    def selectCidade(self, idcidade):
        try:
            c = self.banco.conexao.cursor()
            c.execute("SELECT * FROM tbl_cidades WHERE idcidade = ?", (idcidade,))
            linha = c.fetchone()
            if linha:
                self.idcidade = linha[0]
                self.cidade = linha[1]
                self.uf = linha[2]
                c.close()
                return "Busca feita com sucesso!"
            else:
                c.close()
                return "Cidade não encontrada."
        except Exception as e:
            return f"Ocorreu um erro na busca da cidade: {e}"

    def selectAllCidades(self):
        try:
            c = self.banco.conexao.cursor()
            c.execute("SELECT * FROM tbl_cidades")
            linhas = c.fetchall()
            c.close()
            return linhas
        except Exception as e:
            return f"Ocorreu um erro na recuperação das cidades: {e}"
