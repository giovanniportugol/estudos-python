# Exercício: Cadastro simples
# Objetivo: praticar entrada de dados, listas e organização de informações

usuarios = []

nome = input("Digite o nome do usuário: ")
email = input("Digite o e-mail do usuário: ")
curso = input("Digite o curso do usuário: ")

usuario = {
    "nome": nome,
    "email": email,
    "curso": curso
}

usuarios.append(usuario)

print("\nUsuário cadastrado com sucesso!")
print("Nome:", usuario["nome"])
print("E-mail:", usuario["email"])
print("Curso:", usuario["curso"])
