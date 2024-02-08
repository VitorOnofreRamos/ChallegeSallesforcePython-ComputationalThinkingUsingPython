# Vitor Onofre Ramos // RM553241

class Site:
    def __init__(self):
        self.logged_in = False
        self.current_page = "Página Inicial"
        self.user_info = {}

    def show_homepage(self):
        print("Executando Página Inicial")
        # Está será a página principal do site da Salesforce, é nela que o úsuario encontrara informações básicas sobre a impresa e o site, e podera ser redirecionado para as demais páginas do portal.
        self.current_page = "Página Inicial"

    def show_contacts(self):
        print("Executando Contatos:")
        # Uma página com informações de contato, e principais redes socias.
        self.current_page = "Contatos"

    def show_faqs(self):
        print("Executando FAQs:")
        # Essa página irá conter informações de contato e, possivelmente, um formulário para os visitantes preencherem e enviarem mensagens diretamente.
        self.current_page = "FAQs"

    def show_products(self):
        print("Executando Produtos:")
        # Uma ou mais páginas que detalham os produtos, serviços ou informações oferecidos pelo site.
        self.current_page = "Produtos"

    def show_about_us(self):
        print("Executando Sobre Nós:")
        # A página que irá fornecer informações sobre a empresa ou indivíduo que administra o site.
        self.current_page = "Sobre Nós"

    def cadastro(self):
        print("Executando Cadastro:")
        if self.logged_in:
            print("\nVocê precisa sair da conta atual antes de criar outra.")
        else:
            nomeusuario = input("Digite um nome de usuário: ")
            senha = input("Digite uma senha: ")

            # Salvar as informações do usuário (neste exemplo, em um dicionário)
            self.user_info[nomeusuario] = senha
            print("\nCadastro bem-sucedido!")

    def login(self):
        print("Executando Login:")
        if self.logged_in:
            print("\nVocê já está logado.")
        else:
            nomeusuario = input("Digite seu nome de usuário: ")
            senha = input("Digite sua senha: ")

            # Verifique as credenciais (neste exemplo, as credenciais são armazenadas em um dicionário)
            if nomeusuario in self.user_info and self.user_info[nomeusuario] == senha:
                self.logged_in = True
                print("\nLogin bem-sucedido!")
            else:
                print("\nCredenciais incorretas")

    def logout(self):
        print("Executando Logout")
        if self.logged_in:
            self.logged_in = False
            print("\nVocê saiu da conta.")
        else:
            print("\nVocê não está logado.")

    def trocar_conta(self):
        print("Executando Troca de Contas")
        self.logout()
        self.login()

    def opcoes_cadastrais(self):
        print("Executando opções de Login/Cadastro:")
        while True:
            print("\nEscolha uma da opções para Login ou Cadastro baixo:")
            print("1. Cadastro")
            print("2. Login")
            print("3. Logout")
            print("4. Switch Acount")
            print("0. Sair")

            escolha = input("Opção: ")

            match escolha:
                case "1":
                    self.cadastro()
                case "2":
                    self.login()
                case "3":
                    self.logout()
                case "4":
                    self.trocar_conta()
                case "0":
                    ("Saindo das opções de Login e Cadastro")
                    break
                case _:
                    print("\n*(Você deve informar uma das opções acima)")

    def chat_bot(self):
        print("Executando Chat Bot:")
        mensagem = input("Digite o que você deseja: \r\n")
        print(mensagem)

    def accessibility_menu(self):
        print("Executando Menu de Acessibilidade:")
        while True:
            print("\nEscolha uma opção:")
            print("1. Cores de alto contraste")
            print("2. Navegação por texto")
            print("0. Sair")

            escolha = input("Opção: ")

            match escolha:
                case "1":
                    print("Mudando Contraste da Página")
                case "2":
                    print("Iniciando Navegação por texto")
                case "3":
                    ("Saindo do Menu de Acessibilidade")
                    break
                case _:
                    print("\n*(Você deve informar uma das opções acima)")

    def run(self):
        while True:
            print("\nEscolha uma opção:")
            print("1. Página Inicial")
            print("2. Contatos")
            print("3. FAQs")
            print("4. Produtos")
            print("5. Sobre Nós")
            print("6. Opções de Login/Cadastro")
            print("7. Chat Bot")
            print("8. Menu de Acessibilidade")
            print("0. Sair")

            escolha = input("Opção: ")

            match escolha:
                case "1":
                    self.show_homepage()
                case "2":
                    self.show_contacts()
                case "3":
                    self.show_faqs()
                case "4":
                    self.show_products()
                case "5":
                    self.show_about_us()
                case "6":
                    self.opcoes_cadastrais()
                case "7":
                    self.chat_bot()
                case "8":
                    self.accessibility_menu()
                case "0":
                    print("Saindo do site. Adeus!")
                    break
                case _:
                    print('\n*(Você deve informar uma das opções acima)')

            print(f"\nVocê está na página: {self.current_page}")


site = Site()
site.run()
