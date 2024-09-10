from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from Usuarios import *
import os
class Application:
    def __init__(self, master=None):
        self.master = master
        self.master.title("Formulário de Usuários")

        # Frame para o formulário
        self.janela1 = Frame(master)
        self.janela1.pack(padx=10, pady=10)

        # Título
        self.msg1 = Label(self.janela1, text="Informe os dados:")
        self.msg1["font"] = ("Verdana", "14", "bold")
        self.msg1.pack()

        # Frame para a busca
        self.janela2 = Frame(master)
        self.janela2["padx"] = 20
        self.janela2.pack()

        self.idusuario_label = Label(self.janela2, text="Id usuário:")
        self.idusuario_label.pack(side="left")
        self.idusuario = Entry(self.janela2, width=20)
        self.idusuario.pack(side="left")

        self.busca = Button(self.janela2)
        self.busca["text"] = "Buscar"
        self.busca["command"] = self.buscarUsuario
        self.busca.pack()

        # Frames para os campos de dados
        self.janela3 = Frame(master)
        self.janela3["padx"] = 20
        self.janela3.pack()

        self.nome_label = Label(self.janela3, text="Nome:")
        self.nome_label.pack(side="left")
        self.nome = Entry(self.janela3, width=30)
        self.nome.pack(side="left")

        self.janela5 = Frame(master)
        self.janela5["padx"] = 20
        self.janela5.pack(pady=5)

        self.telefone_label = Label(self.janela5, text="Telefone:")
        self.telefone_label.pack(side="left")
        self.telefone = Entry(self.janela5, width=28)
        self.telefone.pack(side="left")

        self.janela6 = Frame(master)
        self.janela6["padx"] = 20
        self.janela6.pack()

        self.email_label = Label(self.janela6, text="E-mail:")
        self.email_label.pack(side="left")
        self.email = Entry(self.janela6, width=30)
        self.email.pack(side="left")

        self.janela7 = Frame(master)
        self.janela7["padx"] = 20
        self.janela7.pack(pady=5)

        self.usuario_label = Label(self.janela7, text="Usuário:")
        self.usuario_label.pack(side="left")
        self.usuario = Entry(self.janela7, width=29)
        self.usuario.pack(side="left")

        self.janela4 = Frame(master)
        self.janela4["padx"] = 20
        self.janela4.pack(pady=5)

        self.senha_label = Label(self.janela4, text="Senha:")
        self.senha_label.pack(side="left")
        self.senha = Entry(self.janela4, width=30)
        self.senha["show"] = "*"
        self.senha.pack(side="left")

        # Frame para os botões
        self.janela10 = Frame(master)
        self.janela10["padx"] = 20
        self.janela10.pack()

        self.autentic = Label(self.janela10, text="")
        self.autentic["font"] = ("Verdana", "10", "italic", "bold")
        self.autentic.pack()

        self.janela11 = Frame(master)
        self.janela11["padx"] = 20
        self.janela11.pack()

        self.botao = Button(self.janela11, width=10, text="Inserir", command=self.inserirUsuario)
        self.botao.pack(side="left")

        self.botao2 = Button(self.janela11, width=10, text="Alterar", command=self.alterarUsuario)
        self.botao2.pack(side="left")

        self.botao3 = Button(self.janela11, width=10, text="Excluir", command=self.excluirUsuario)
        self.botao3.pack(side="left")

        self.botao4 = Button(self.janela11, width=10, text="Gerar PDF", command=self.gerar_pdf)
        self.botao4.pack(side="left")

        # Frame para a tabela
        self.janela12 = Frame(master)
        self.janela12["padx"] = 20
        self.janela12.pack(pady=10)

        self.tree = ttk.Treeview(self.janela12, columns=("ID", "Nome", "Telefone", "E-mail", "Usuário", "Senha"),
                                 show='headings')
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nome", text="Nome")
        self.tree.heading("Telefone", text="Telefone")
        self.tree.heading("E-mail", text="E-mail")
        self.tree.heading("Usuário", text="Usuário")
        self.tree.heading("Senha", text="Senha")
        self.tree.pack()

        # Evento de clique na linha da tabela
        self.tree.bind("<ButtonRelease-1>", self.selecionar_linha)

        # Atualiza a tabela quando a aplicação é carregada
        self.atualizarTabela()

        self.janela13 = Frame(master)
        self.janela13["padx"] = 20
        self.janela13.pack(pady=10)

        self.botao4 = Button(self.janela13, width=10, text="Voltar", command=self.voltarmenu)
        self.botao4.pack(side="left")

    def atualizarTabela(self):
        user = Usuarios()
        usuarios = user.selectAllUsers()
        self.tree.delete(*self.tree.get_children())
        for u in usuarios:
            self.tree.insert("", "end", values=(u[0], u[1], u[2], u[3], u[4], u[5]))

    def selecionar_linha(self, event):
        """Preenche os campos de entrada com os dados da linha selecionada na tabela."""
        selected_item = self.tree.selection()  # Captura o item selecionado
        if selected_item:
            item = self.tree.item(selected_item[0])  # Obtém o primeiro item selecionado
            valores = item['values']  # Obtém os valores da linha selecionada

            # Verifique se a linha possui dados
            if valores:
                # Preenche os campos de entrada com os dados da linha selecionada
                self.idusuario.delete(0, END)
                self.idusuario.insert(END, valores[0])
                self.nome.delete(0, END)
                self.nome.insert(END, valores[1])
                self.telefone.delete(0, END)
                self.telefone.insert(END, valores[2])
                self.email.delete(0, END)
                self.email.insert(END, valores[3])
                self.usuario.delete(0, END)
                self.usuario.insert(END, valores[4])
                self.senha.delete(0, END)
                self.senha.insert(END, valores[5])

    def buscarUsuario(self):
        user = Usuarios()
        idusuario = self.idusuario.get()
        result = user.selectUser(idusuario)
        if result:
            self.autentic["text"] = "Usuário encontrado!"
            self.idusuario.delete(0, END)
            self.idusuario.insert(INSERT, result[0])
            self.nome.delete(0, END)
            self.nome.insert(INSERT, result[1])
            self.telefone.delete(0, END)
            self.telefone.insert(INSERT, result[2])
            self.email.delete(0, END)
            self.email.insert(INSERT, result[3])
            self.usuario.delete(0, END)
            self.usuario.insert(INSERT, result[4])
            self.senha.delete(0, END)
            self.senha.insert(INSERT, result[5])
        else:
            self.autentic["text"] = "Usuário não encontrado!"

        # Atualiza a tabela com o usuário encontrado
        self.atualizarTabela()

    def inserirUsuario(self):
        user = Usuarios()
        user.nome = self.nome.get()
        user.telefone = self.telefone.get()
        user.email = self.email.get()
        user.usuario = self.usuario.get()
        user.senha = self.senha.get()
        self.autentic["text"] = user.insertUser()
        self.limparCampos()
        self.atualizarTabela()
        messagebox.showinfo("Inserir", "Usuário inserido com sucesso!")

    def alterarUsuario(self):
        user = Usuarios()
        user.idusuario = self.idusuario.get()
        user.nome = self.nome.get()
        user.telefone = self.telefone.get()
        user.email = self.email.get()
        user.usuario = self.usuario.get()
        user.senha = self.senha.get()
        user.updateUser()  # Atualiza o usuário
        messagebox.showinfo("Alterar", "Usuário alterado com sucesso!")
        self.limparCampos()
        self.atualizarTabela()

    def excluirUsuario(self):
        user = Usuarios()
        user.idusuario = self.idusuario.get()
        user.deleteUser()  # Exclui o usuário
        messagebox.showinfo("Excluir", "Usuário excluído com sucesso!")
        self.limparCampos()
        self.atualizarTabela()

    def limparCampos(self):
        self.idusuario.delete(0, END)
        self.nome.delete(0, END)
        self.telefone.delete(0, END)
        self.email.delete(0, END)
        self.usuario.delete(0, END)
        self.senha.delete(0, END)
        self.tree.delete(*self.tree.get_children())

    def gerar_pdf(self):
        # Cria o canvas do PDF
        nome_arquivo = "formulario.pdf"
        c = canvas.Canvas(nome_arquivo, pagesize=letter)
        width, height = letter

        # Define a posição inicial
        x = 50
        y = height -50
        c.setFont("Helvetica", 8)

        # Adiciona o título
        c.drawString(x, y, "Relatório de Usuários")
        y -= 30

        # Adiciona os cabeçalhos
        headers = ["ID", "nome", "nascimento", "email", "usuário", "senha"]
        for i, header in enumerate(headers):
            c.drawString(x + i * 100, y, header)
        y -= 15

        # Adiciona os dados da tabela
        for item in self.tree.get_children():
            values = self.tree.item(item, 'values')
            for i, value in enumerate(values):
                c.drawString(x + i * 100, y, str(value))
            y -= 20

        # Salva o PDF
        c.save()
        messagebox.showinfo("PDF", f"PDF gerado: {nome_arquivo}")

        # Pergunta se o usuário deseja visualizar o PDF
        resposta = messagebox.askyesno("Visualizar PDF", "Deseja visualizar o arquivo PDF gerado?")
        if resposta:
            # Tenta abrir o PDF com o aplicativo padrão do sistema
            if os.name == 'nt':  # Para Windows
                os.startfile(nome_arquivo)
            elif os.name == 'posix':  # Para Unix-like (Linux, macOS)
                try:
                    os.system(f'open "{nome_arquivo}"')  # macOS
                except:
                    os.system(f'xdg-open "{nome_arquivo}"')  # Linux
            else:
                messagebox.showwarning("Aviso", "Não foi possível abrir o arquivo PDF automaticamente.")

    def voltarmenu(self):
        self.master.destroy()

# Inicializa a aplicação
if __name__ == "__main__":
    root = Tk()
    app = Application(master=root)
    root.mainloop()
