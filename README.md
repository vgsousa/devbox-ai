# 🤖 DevBox de IA — Stack com Terraform e Ansible

Este projeto provisiona uma **DevBox de Inteligência Artificial** na **Azure**, usando **Terraform** para criar a infraestrutura e **Ansible** para configurar o ambiente com ferramentas como **JupyterLab**, **Python**, bibliotecas de IA e machine learning.

Feito com foco em tornar Infra + IA acessível para devs.

---

## 📦 Visão Geral

- ☁️ **Terraform**: Cria uma máquina virtual Ubuntu na Azure.
- ⚙️ **Ansible**: Instala JupyterLab, Python, bibliotecas de IA (scikit-learn, pandas, etc) e configura acesso.
- 🧠 **JupyterLab**: Ambiente pronto para executar modelos locais e prototipar ideias com IA.

---

## 📁 Estrutura do projeto

```bash
.
├── ai/
│   ├── sentiment.py
│   └── task_classifier.py
│   └── use_model.py
├── ansible/
│   ├── roles/
│   │   └── devbox/
│   │       ├── tasks/
│   │       │   └── main.yml
│   │       └── templates/
│   │           └── jupyter.service.j2
│   │── inventory.ini
│   └── playbook.yml
├── terraform/
│   ├── main.tf
│   ├── variables.tf
│   ├── outputs.tf
│   └── provider.tf
├── keys/
│   ├── azure-key
│   └── azure-key.pub
├── .env
├── docker-compose.yml
├── Dockerfile
└── README.md
```

## 🚀 Configurando
### 1. Pré-requisitos

- Docker instalado
- Chave SSH gerada (em `./keys`)
- Azure Service Principal criado com permissão de contributor

### 2. Configurar variáveis de ambiente

Preencha o arquivo `.env` com suas credenciais da Azure e chave SSH pública:

```dotenv
ARM_CLIENT_ID=""
ARM_TENANT_ID=""
ARM_SUBSCRIPTION_ID=""
ARM_CLIENT_SECRET=""

TF_VAR_azure_key_pub="$(cat ./keys/azure-key.pub)"
```

### 3. Subir o container com Terraform + Ansible

```bash
docker-compose run --rm tf-ansible
```

### 4. Provisionar a VM com Terraform

```bash
cd terraform
terraform init
terraform apply
```
No final, o Terraform vai te mostrar o IP público da VM criada.

### 5. Configurar a VM com Ansible

Atualize o arquivo ansible/inventory.ini com o IP da VM:
```bash
[devbox]
<ID_INSTANCE_TERRAFORM> ansible_user=devbox ansible_ssh_private_key_file=/.ssh/azure-key
```
Depois, ainda dentro do container:
```bash
cd ansible
ansible-playbook -i inventory.ini playbook.yml
```
Isso instalará:

- Python 3, pip
- JupyterLab
- Bibliotecas como pandas, scikit-learn
- Configuração de Jupyter como serviço acessível na porta 8888

## 🌐 Acessar o JupyterLab

Abra no navegador:
```cpp
http://<IP_PUBLICO>:8888
```
O token de acesso pode ser visto com:
```bash
journalctl -u jupyter.service
```

## 🤖 IA: Classificador de Tarefas
### 🧠 ai/task_classifier.py
Script de treino de modelo que classifica tarefas de desenvolvimento:
- bug
- documentacao
- nova_feature
- debito_tecnico
Baseado no título e descrição da tarefa.

### 📦 ai/use_model.py
Exemplo de como carregar o modelo salvo com joblib e fazer previsões novas.

## 📜 Licença
MIT License — fique à vontade para adaptar e usar o projeto como quiser.
