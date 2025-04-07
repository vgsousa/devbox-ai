import joblib

# Carregar o modelo salvo
modelo = joblib.load("task_classifier.joblib")

# Novo exemplo
titulo = "Adicionar validação de CPF"
descricao = "O formulário de cadastro não está verificando se o CPF do usuário é valido."
texto_completo = titulo + " - " + descricao

# Classificar
categoria_prevista = modelo.predict([texto_completo])[0]
print(f"Categoria prevista: {categoria_prevista}")