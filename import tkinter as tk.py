import tkinter as tk
from tkinter import messagebox

usuarios = {}
carrinho = []  # Lista para armazenar os produtos no carrinho

# Função para cadastrar um novo usuário
def cadastrar_usuario():
    nome = nome_entry.get()
    email = email_entry.get()
    senha = senha_entry.get()

    if not nome or not email or not senha:
        campos_em_branco = []
        if not nome:
            campos_em_branco.append("Nome")
        if not email:
            campos_em_branco.append("E-mail")
        if not senha:
            campos_em_branco.append("Senha")
        
        messagebox.showerror("Erro", f"Campos em branco: {', '.join(campos_em_branco)}")
    elif email in usuarios:
        messagebox.showerror("Erro", "Este e-mail já está cadastrado. Tente fazer login.")
    else:
        usuarios[email] = {
            "nome": nome,
            "senha": senha
        }
        messagebox.showinfo("Sucesso", "Cadastro realizado com sucesso!")
        mostrar_login()

# Função para fazer login
def fazer_login():
    email = email_login_entry.get()
    senha = senha_login_entry.get()

    if email in usuarios and usuarios[email]["senha"] == senha:
        messagebox.showinfo("Bem-vindo", f"Bem-vindo, {usuarios[email]['nome']}!")
        mostrar_tela_principal()
    else:
        messagebox.showerror("Erro", "E-mail ou senha incorretos. Tente novamente.")

# Function for upload of images
def upload_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.png")])
    if file_path:
        selected_resolution = select_resolution()  # Apply logic for resolution selection
        if selected_resolution:
            messagebox.showinfo("Image Uploaded", f"Image uploaded successfully with resolution: {selected_resolution[0]}x{selected_resolution[1]}")

# Function to display resolution options and return the selected resolution
def select_resolution():
    resolutions = {
        "256x256": (256, 256),
        "512x512": (512, 512),
        "1024x1024": (1024, 1024)
    }

    resolution_choice = messagebox.askoption("Select Resolution", "Select Image Resolution", icon='question', type='okcancel', choices=list(resolutions.keys()))
    
    if resolution_choice:
        return resolutions[resolution_choice]
    else:
        return None
        
# Função para mostrar detalhes do produto
def mostrar_detalhes_produto(nome_produto, preco_produto):
    detalhes = f"Produto: {nome_produto}\nPreço: {preco_produto}\n\nOpções de Pagamento:\n- Pix\n- Cartão de Crédito\n- Dinheiro"
    messagebox.showinfo("Detalhes do Produto", detalhes)

# Função para fazer login usando conta do Google
def fazer_login_google():
    # Lógica para fazer login usando uma conta do Google
    messagebox.showinfo("Login Google", "Fazer login com Google.")

# Função para cadastrar um novo usuário usando conta do Google
def cadastrar_google():
    # Lógica para cadastrar um usuário usando uma conta do Google
    messagebox.showinfo("Cadastro Google", "Cadastrar com Google.")

# Adicionando o botão "Continuar com o Google"
def adicionar_botao_continuar_google():
    global login_frame  # Declara login_frame como global para ser acessível aqui
    continuar_google_button = tk.Button(login_frame, text="Continuar com o Google", command=fazer_login_google, bg="#4285F4", fg="white")
    continuar_google_button.grid(row=3, columnspan=2, pady=10)

# Atualização da função para fazer login
def fazer_login():
    email = email_login_entry.get()
    senha = senha_login_entry.get()

    if email in usuarios and usuarios[email]["senha"] == senha:
        messagebox.showinfo("Bem-vindo", f"Bem-vindo, {usuarios[email]['nome']}!")
        mostrar_tela_principal()
    else:
        # Adicionando opção de login com Google
        if messagebox.askyesno("Login", "Login falhou. Deseja fazer login com uma conta do Google?"):
            fazer_login_google()
        else:
            messagebox.showerror("Erro", "E-mail ou senha incorretos. Tente novamente.")

# Função para criar a tela principal
def mostrar_tela_principal():
    login_frame.pack_forget()
    pesquisa_frame.pack()
    carrinho_frame.pack()
    
    principal_frame = tk.Frame(root, bg="#E6E6E6")  # Cor de fundo harmoniosa
    principal_frame.pack(pady=20, padx=20, fill="both", expand=True)
    
    produtos = [
        {"nome": "Camiseta Vermelha", "preço": "$10.00", "cor": "Vermelha"},
        {"nome": "Camiseta Azul", "preço": "$15.00", "cor": "Azul"},
        {"nome": "Camiseta Verde", "preço": "$12.00", "cor": "Verde"},
        {"nome": "Brigadeiro Chocolate", "preço": "$1.50"},
        {"nome": "Sobremesa com Uvas", "preço": "$5.00"},
        {"nome": "Brigadeiro Leite Ninho", "preço": "$1.50"},
        {"nome": "Brigadeiro Morango", "preço": "$1.50"},
    ]
    
    for i, produto in enumerate(produtos):
        produto_frame = tk.Frame(principal_frame, bg="#E6E6E6")
        produto_frame.grid(row=i, column=0, padx=10, pady=10, sticky="w")
        
        label_produto = tk.Label(produto_frame, text=produto["nome"], bg="#E6E6E6")
        label_produto.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        
        label_preço = tk.Label(produto_frame, text=produto["preço"], bg="#E6E6E6")
        label_preço.grid(row=0, column=1, padx=10, pady=5, sticky="w")
        
        botao_pedido = tk.Button(produto_frame, text="Pedido", command=lambda p=produto["nome"], pr=produto["preço"]: adicionar_ao_carrinho(p, pr), bg="#007ACC", fg="white")
        botao_pedido.grid(row=0, column=2, padx=10, pady=5)
    
    ajuda_icon = tk.PhotoImage(file="ajuda.png")  # Substitua com o caminho do seu ícone
    suporte_icon = tk.PhotoImage(file="suporte.png")  # Substitua com o caminho do seu ícone
    detalhes_icon = tk.PhotoImage(file="detalhes.png")  # Substitua com o caminho do seu ícone
    
    ajuda_button = tk.Button(principal_frame, image=ajuda_icon, command=mostrar_ajuda, bg="#E6E6E6")  # Cor de fundo harmoniosa
    ajuda_button.grid(row=0, column=1, padx=10, pady=10)
    
    suporte_button = tk.Button(principal_frame, image=suporte_icon, command=mostrar_suporte, bg="#E6E6E6")  # Cor de fundo harmoniosa
    suporte_button.grid(row=0, column=2, padx=10, pady=10)
    
    detalhes_button = tk.Button(principal_frame, image=detalhes_icon, command=mostrar_detalhes, bg="#E6E6E6")  # Cor de fundo harmoniosa
    detalhes_button.grid(row=0, column=3, padx=10, pady=10)
    
    carrinho_label = tk.Label(principal_frame, text=f"Carrinho: {len(carrinho)}", bg="#E6E6E6")  # Cor de fundo harmoniosa
    carrinho_label.grid(row=0, column=4, padx=10, pady=10)
    
    carrinho_canvas = tk.Canvas(principal_frame, width=40, height=40, bg="#E6E6E6", highlightthickness=0)
    carrinho_canvas.grid(row=0, column=5, padx=10, pady=10)
    carrinho_canvas.create_rectangle(10, 10, 30, 30, fill="blue")
    carrinho_canvas.create_polygon(10, 10, 20, 0, 30, 10, fill="blue")

# Função para adicionar um produto ao carrinho
def adicionar_ao_carrinho(produto, preço):
    carrinho.append((produto, preço))
    messagebox.showinfo("Pedido", f"{produto} adicionado ao carrinho!")
    carrinho_label.config(text=f"Carrinho: {len(carrinho)}")

def mostrar_ajuda():
    messagebox.showinfo("Ajuda", "Você clicou em Ajuda!")

def mostrar_suporte():
    messagebox.showinfo("Suporte", "Você clicou em Suporte!")

def mostrar_detalhes():
    messagebox.showinfo("Detalhes do Site", "Você clicou em Detalhes do Site!")

# List of search suggestions
search_suggestions = ["Camiseta", "Vermelha", "Azul", "Verde"]

# Function to show search suggestions
def show_search_suggestions():
    term = entrada.get().lower()
    suggestions = [s for s in search_suggestions if term in s.lower()]
    if suggestions:
        messagebox.showinfo("Sugestões de Pesquisa", "Sugestões: " + ", ".join(suggestions))

# Function to perform search when "Search" button is clicked
def pesquisar():
    term = entrada.get().lower()
    produtos_encontrados = []

    produtos = [
        {"nome": "Camiseta Vermelha", "preço": "$10.00", "cor": "Vermelha"},
        {"nome": "Camiseta Azul", "preço": "$15.00", "cor": "Azul"},
        {"nome": "Camiseta Verde", "preço": "$12.00", "cor": "Verde"},
        {"nome": "Brigadeiro Chocolate", "preço": "$1.50"},
        {"nome": "Sobremesa com Uvas", "preço": "$5.00"},
        {"nome": "Brigadeiro Leite Ninho", "preço": "$1.50"},
    ]

    for produto in produtos:
        if term in produto["cor"].lower():
            produtos_encontrados.append(produto)

    if produtos_encontrados:
        atualizar_lista_produtos(produtos_encontrados)
    else:
        messagebox.showinfo("Pesquisa", "Nenhum produto encontrado com essa cor.")

# Function to update the product list based on the search
def atualizar_lista_produtos(produtos):
    for widget in principal_frame.winfo_children():
        widget.destroy()

    for i, produto in enumerate(produtos):
        produto_frame = tk.Frame(principal_frame, bg="#E6E6E6")
        produto_frame.grid(row=i, column=0, padx=10, pady=10, sticky="w")
        
        label_produto = tk.Label(produto_frame, text=produto["nome"], bg="#E6E6E6")
        label_produto.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        
        label_preço = tk.Label(produto_frame, text=produto["preço"], bg="#E6E6E6")
        label_preço.grid(row=0, column=1, padx=10, pady=5, sticky="w")
        
        botao_pedido = tk.Button(produto_frame, text="Pedido", command=lambda p=produto["nome"], pr=produto["preço"]: adicionar_ao_carrinho(p, pr), bg="#007ACC", fg="white")
        botao_pedido.grid(row=0, column=2, padx=10, pady=5)

# Function to perform search in the cart
def pesquisar_no_carrinho():
    term = entrada_pesquisa_carrinho.get().lower()
    produtos_encontrados = []

    for produto, preço in carrinho:
        if term in produto.lower():
            produtos_encontrados.append((produto, preço))

    if produtos_encontrados:
        atualizar_lista_carrinho(produtos_encontrados)
    else:
        messagebox.showinfo("Pesquisa", "Nenhum produto encontrado no carrinho.")

# Function to update the cart list based on the search
def atualizar_lista_carrinho(produtos):
    lista_carrinho.delete(0, tk.END)  # Limpar a lista atual

    for produto, preço in produtos:
        lista_carrinho.insert(tk.END, f"{produto} - {preço}")

# Função para realizar a pesquisa
def pesquisar():
    termo = entrada.get().lower()
    produtos_encontrados = []

    for produto in produtos:
        if termo in produto["nome"].lower():
            produtos_encontrados.append(produto)

    if produtos_encontrados:
        atualizar_lista_produtos(produtos_encontrados)
    else:
        messagebox.showinfo("Pesquisa", "Nenhum produto encontrado com esse termo.")

def pesquisar():
    termo = entrada.get().lower()
    resultado.delete(1.0, tk.END)
    for item in lista_itens:
        if termo in item[1].lower():
            resultado.insert(tk.END, f"{item[0]}. {item[1]}\n")

def notificar():
    selecionado = resultado.get(tk.ACTIVE).split('. ')[1]
    print(f"Você selecionou: {selecionado}")

# Lista de itens
lista_itens = [(1, "Pote da Felicidade, pote de 250ml. vem com creme de ninho uvas sem semente e creme  chocolate - R$ 10,00"),
               (2, "Brigadeiro no Pote, 100ml, brigadeiro de creme  ninho e outras variacoes 14,99"),
               (3, "sençacao/moramgo, de 250ml, vem creme ninho moramgos e creme de chocolate - R$ 11,99"),
               (4, "maracuja desidratado, de 250ml, vem creme chocolate maracuja desidratado e creme ninho - R$ 11,99 ")]

# Criar janela principal
root = tk.Tk()
root.title("Pesquisa de Itens")

# Entrada e botão de pesquisa
entrada = tk.Entry(root, width=30)
entrada.pack(pady=10)
botao_pesquisar = tk.Button(root, text="Pesquisar", command=pesquisar)
botao_pesquisar.pack()

# Resultado da pesquisa
resultado = tk.Text(root, width=50, height=10)
resultado.pack(pady=10)

# Botão de notificação
botao_notificar = tk.Button(root, text="Notificar", command=notificar)
botao_notificar.pack()

# Configuração da janela principal
root = tk.Tk()
root.title("Compra de Camiseta")

# Crie um menu superior
menu_superior = tk.Menu(root)
root.config(menu=menu_superior)

menu_produtos = tk.Menu(menu_superior, tearoff=0)
menu_superior.add_cascade(label="Produtos", menu=menu_produtos)
menu_produtos.add_command(label="Tela Principal", command=mostrar_tela_principal)
menu_produtos.add_separator()
menu_produtos.add_command(label="Sair", command=root.quit)

# Frames para organizar a interface
cadastro_frame = tk.Frame(root, bg="#E6E6E6")
login_frame = tk.Frame(root, bg="#E6E6E6")
pesquisa_frame = tk.Frame(root, bg="#E6E6E6")
carrinho_frame = tk.Frame(root, bg="#E6E6E6")

# Configuração dos elementos do frame de cadastro
nome_label = tk.Label(cadastro_frame, text="Nome:", bg="#E6E6E6")
nome_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")
nome_entry = tk.Entry(cadastro_frame)
nome_entry.grid(row=0, column=1, padx=10, pady=10)

email_label = tk.Label(cadastro_frame, text="E-mail:", bg="#E6E6E6")
email_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")
email_entry = tk.Entry(cadastro_frame)
email_entry.grid(row=1, column=1, padx=10, pady=10)

senha_label = tk.Label(cadastro_frame, text="Senha:", bg="#E6E6E6")
senha_label.grid(row=2, column=0, padx=10, pady=10, sticky="e")
senha_entry = tk.Entry(cadastro_frame, show="*")
senha_entry.grid(row=2, column=1, padx=10, pady=10)

cadastrar_button = tk.Button(cadastro_frame, text="Cadastrar", command=cadastrar_usuario, bg="#007ACC", fg="white")
cadastrar_button.grid(row=3, columnspan=2, pady=10)

# Configuração dos elementos do frame de login
email_login_label = tk.Label(login_frame, text="E-mail:", bg="#E6E6E6")
email_login_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")
email_login_entry = tk.Entry(login_frame)
email_login_entry.grid(row=0, column=1, padx=10, pady=10)

senha_login_label = tk.Label(login_frame, text="Senha:", bg="#E6E6E6")
senha_login_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")
senha_login_entry = tk.Entry(login_frame, show="*")
senha_login_entry.grid(row=1, column=1, padx=10, pady=10)

login_button = tk.Button(login_frame, text="Fazer Login", command=fazer_login, bg="#007ACC", fg="white")
login_button.grid(row=2, columnspan=2, pady=10)

# Configuração dos elementos do frame de pesquisa
label = tk.Label(pesquisa_frame, text="Pesquisar:", bg="#E6E6E6", fg="#333333")
label.grid(row=0, column=0, padx=10, pady=10, sticky="e")

entrada = tk.Entry(pesquisa_frame, width=30)
entrada.grid(row=0, column=1, padx=5, pady=10)

botao_pesquisar = tk.Button(pesquisa_frame, text="Pesquisar", bg="#4CAF50", fg="white", command=pesquisar)
botao_pesquisar.grid(row=0, column=2, padx=10, pady=10)

botao_sugestoes = tk.Button(pesquisa_frame, text="Sugestões", bg="#FFC107", fg="black", command=show_search_suggestions)
botao_sugestoes.grid(row=0, column=3, padx=10, pady=10)

# Configuração dos elementos do frame do carrinho
carrinho_label = tk.Label(carrinho_frame, text=f"Carrinho: {len(carrinho)}", bg="#E6E6E6")
carrinho_label.grid(row=0, column=0, padx=10, pady=10)

label_pesquisa_carrinho = tk.Label(carrinho_frame, text="Pesquisar no Carrinho:", bg="#E6E6E6", fg="#333333")
label_pesquisa_carrinho.grid(row=0, column=1, padx=10, pady=10, sticky="e")

entrada_pesquisa_carrinho = tk.Entry(carrinho_frame, width=30)
entrada_pesquisa_carrinho.grid(row=0, column=2, padx=5, pady=10)

botao_pesquisar_carrinho = tk.Button(carrinho_frame, text="Pesquisar", bg="#4CAF50", fg="white", command=pesquisar_no_carrinho)
botao_pesquisar_carrinho.grid(row=0, column=3, padx=10, pady=10)

lista_carrinho = tk.Listbox(carrinho_frame, width=40, height=10)
lista_carrinho.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

# Add a button for image upload
botao_upload_imagem = tk.Button(pesquisa_frame, text="Upload Image", bg="#4CAF50", fg="white", command=upload_image)
botao_upload_imagem.grid(row=0, column=4, padx=10, pady=10)

# Inicialmente, mostra o frame de cadastro
cadastro_frame.pack()
login_frame.pack()

root.mainloop()
