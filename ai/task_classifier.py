# Instalar dependências (se ainda não tiver)
!pip install scikit-learn pandas joblib --quiet

import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.linear_model import LogisticRegression
import joblib

# Dataset
dados = pd.DataFrame({
    "titulo": [
        # Débito técnico
        "Atualizar dependências", "Remover código morto", "Reescrever módulo legado", "Ajustar nomes de variáveis", "Migrar para Python 3.10",
        "Corrigir warnings do linter", "Refatorar serviços com muita lógica", "Reduzir complexidade ciclomática", "Organizar arquivos do backend", "Melhorar estrutura de pastas",
        "Separar lógica de negócios do controller", "Remover bibliotecas não utilizadas", "Atualizar versão do Node.js", "Padronizar formatação de código", "Melhorar tempo de build",

        # Nova feature
        "Autenticação com biometria", "Notificações por e-mail", "Filtro avançado de busca", "Integração com Google Calendar", "Exportar relatórios em PDF",
        "Dashboard interativo", "Cadastro com redes sociais", "Tema escuro", "Upload de múltiplos arquivos", "Agendamento de tarefas",
        "Suporte a multi-idioma", "Login com dois fatores", "Editor de texto avançado", "Sistema de comentários", "Módulo de avaliação de usuários",

        # Bug
        "Erro ao salvar usuário", "Falha no login com Google", "Crash ao exportar CSV", "Botão de salvar não responde", "Layout quebrado no Safari",
        "Erro 500 ao acessar perfil", "Valor duplicado no relatório", "Erro de validação ao cadastrar", "Link quebrado na página inicial", "Scroll infinito não carrega",
        "Timeout na API de produtos", "Erro ao deletar item", "Logout não está funcionando", "Imagem não carrega", "Formulário bloqueado sem motivo",

        # Melhoria
        "Melhorar desempenho de busca", "Otimizar carregamento da home", "Reduzir chamadas à API", "Melhorar experiência mobile", "Melhorar feedback visual de ações",
        "Aumentar cobertura de testes", "Melhorar tempo de resposta do backend", "Reduzir uso de memória", "Aplicar cache no frontend", "Tornar mensagens de erro mais claras",
        "Reorganizar menu lateral", "Melhorar navegação por teclado", "Adicionar animações suaves", "Melhorar contraste do tema claro", "Aplicar lazy loading de imagens",

        # Documentação
        "Documentar processo de deploy", "Criar README do projeto", "Incluir exemplos de uso na doc", "Atualizar documentação da API", "Especificar variáveis de ambiente",
        "Documentar arquitetura do sistema", "Instruções para rodar localmente", "Checklist de publicação", "Criar guia de contribuição", "Documentar fluxo de autenticação",
        "Incluir changelog", "Atualizar licença do projeto", "Adicionar FAQ", "Documentar uso do Docker", "Criar tutorial de onboarding"
    ],
    "descricao": [
        # Débito técnico
        "Atualizar bibliotecas desatualizadas para evitar riscos de segurança.",
        "Remover código que não é mais utilizado no sistema.",
        "Reescrever módulo antigo para seguir o novo padrão de arquitetura.",
        "Renomear variáveis para seguir a convenção da equipe.",
        "Migrar código legado para Python 3.10.",
        "Corrigir todos os warnings apontados pelo linter.",
        "Refatorar serviços com muitas responsabilidades para separação adequada.",
        "Reduzir complexidade em funções com muitas decisões condicionais.",
        "Organizar arquivos backend em módulos mais coesos.",
        "Melhorar estrutura de pastas conforme a nova organização definida.",
        "Separar lógica de negócios dos controllers MVC.",
        "Remover dependências não utilizadas no projeto.",
        "Atualizar o Node.js para a versão LTS atual.",
        "Aplicar padrão de formatação com prettier e isort.",
        "Reduzir o tempo de build em pelo menos 30%.",

        # Nova feature
        "Implementar login usando impressão digital.",
        "Enviar e-mails transacionais para o usuário.",
        "Criar busca com filtros por data e status.",
        "Sincronizar tarefas com o Google Calendar.",
        "Permitir exportação dos dados em formato PDF.",
        "Adicionar dashboard com gráficos interativos.",
        "Permitir cadastro com Google e Facebook.",
        "Implementar tema escuro no frontend.",
        "Permitir upload de vários arquivos de uma vez.",
        "Permitir agendar execução de tarefas pelo sistema.",
        "Traduzir sistema para múltiplos idiomas.",
        "Adicionar autenticação em dois fatores.",
        "Adicionar editor de texto com markdown.",
        "Permitir comentários em postagens.",
        "Criar sistema de notas e avaliações por usuários.",

        # Bug
        "Erro ao salvar usuário sem e-mail preenchido.",
        "Falha ao autenticar com conta do Google.",
        "Sistema trava ao exportar lista em CSV.",
        "Botão 'Salvar' não executa nenhuma ação.",
        "Layout quebra em dispositivos Safari.",
        "Erro 500 ao acessar página de perfil do usuário.",
        "Relatório apresenta valores duplicados.",
        "Erro de validação ao cadastrar usuário com dados válidos.",
        "Link da página inicial está levando a um 404.",
        "Scroll infinito para de funcionar após algumas páginas.",
        "Requisições à API de produtos estão expirando.",
        "Erro ao tentar deletar um item específico.",
        "Logout não efetua redirecionamento corretamente.",
        "Imagens dos produtos não estão carregando.",
        "Formulário de cadastro está bloqueado sem razão aparente.",

        # Melhoria
        "Melhorar desempenho das buscas internas.",
        "Otimizar carregamento da página inicial.",
        "Diminuir número de chamadas duplicadas à API.",
        "Aprimorar layout para dispositivos móveis.",
        "Mostrar melhor feedback visual após ações.",
        "Aumentar cobertura de testes automatizados.",
        "Reduzir tempo de resposta do backend.",
        "Diminuir uso de memória em background jobs.",
        "Aplicar caching nas requisições mais frequentes.",
        "Deixar mensagens de erro mais explicativas.",
        "Reorganizar menu para melhor usabilidade.",
        "Permitir navegação por teclado em formulários.",
        "Adicionar pequenas animações em transições.",
        "Melhorar contraste no tema claro.",
        "Aplicar carregamento preguiçoso de imagens.",

        # Documentação
        "Passo a passo para fazer deploy em produção.",
        "Criar arquivo README com visão geral do projeto.",
        "Adicionar exemplos de chamadas à API.",
        "Atualizar a documentação com novos endpoints.",
        "Especificar variáveis necessárias no .env.",
        "Documentar a arquitetura de microsserviços.",
        "Incluir instruções para rodar localmente.",
        "Criar checklist para publicar nova versão.",
        "Guia de contribuição para novos devs.",
        "Documentar o fluxo de autenticação do sistema.",
        "Criar changelog com mudanças recentes.",
        "Atualizar tipo de licença do projeto.",
        "Adicionar perguntas frequentes (FAQ).",
        "Documentar uso do Docker e containers.",
        "Criar tutorial de onboarding técnico."
    ]
})
categorias = ["debito_tecnico", "nova_feature", "bug", "melhoria", "documentacao"]
dados["categoria"] = [cat for cat in categorias for _ in range(15)]

# Combinar título e descrição
dados["texto_completo"] = dados["titulo"] + " - " + dados["descricao"]

# Separar treino/teste
X_train, X_test, y_train, y_test = train_test_split(
    dados["texto_completo"], dados["categoria"], test_size=0.2, random_state=42, stratify=dados["categoria"]
)

# Pipeline
modelo = Pipeline([
    ("vetorizador", TfidfVectorizer()),
    ("classificador", MultinomialNB())
])

# Treinar
modelo.fit(X_train, y_train)

# Avaliar
y_pred = modelo.predict(X_test)
print("\nRelatório de classificação:\n")
print(classification_report(y_test, y_pred, zero_division=0))

# Testar com novos exemplos
novas_tarefas = pd.DataFrame({
    "titulo": [
        "Cobertura de testes",
        "Erro ao logar com Google",
        "Integração com pagamentos",
        "Atualizar README",
        "Remover código duplicado"
    ],
    "descricao": [
        "Melhorar a cobertura dos testes unitários no módulo de autenticação",
        "Corrigir falha ao autenticar usando conta Google",
        "Implementar integração com API de pagamentos",
        "Adicionar instruções de uso ao README",
        "Remover código repetido na camada de serviços"
    ]
})
novas_tarefas["texto_completo"] = novas_tarefas["titulo"] + " - " + novas_tarefas["descricao"]

previsoes = modelo.predict(novas_tarefas["texto_completo"])
for i, pred in enumerate(previsoes):
    print(f"\nTarefa: {novas_tarefas['titulo'][i]}\n-> Categoria prevista: {pred}")

# Salvar modelo
joblib.dump(modelo, "task_classifier.joblib")
