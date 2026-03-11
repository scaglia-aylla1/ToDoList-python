# 🚀 TodoList API

![Build Status](https://github.com/scaglia-aylla1/100days-python-web/actions/workflows/tests.yml/badge.svg)

## 📌 Sobre o Projeto

### API REST para gerenciamento de tarefas desenvolvida com Flask.
### O projeto implementa boas práticas de desenvolvimento backend, incluindo arquitetura em camadas, testes automatizados e integração contínua.

## 🛠️ Stack Tecnológica

* Python

* Flask

* Flask-Smorest(documentação)

* SQLAlchemy

* PostgreSQL

* Flask-Migrate

* Marshmallow

* Pytest

* SQLite

* Docker

* Versionamento com Git
Github Actions

## 📂 Estrutura do Projeto
```
    todolist-api 
    │ 
    ├── app 
    │    │ 
    │    ├── routes.py  
    │    ├── extensions.py 
    │    │ 
    │    ├── models 
    │    │    │ 
    │    │    └── task.py 
    │    ├── schemas 
    │    │    └── task_schema.py 
    │    │  
    │    └── services │
    │        └── task_service.py 
    │     
    ├── tests 
    │    └── test_tasks.py 
    │ 
    ├── migrations 
    ├── pytest.ini 
    ├── requirements.txt 
    └── run.py
```

## O projeto segue uma arquitetura em camadas:
* **Routes** → definição dos endpoints da API

* **Services** → lógica de negócio

* **Schemas** → validação e serialização de dados

* **Models** → entidades do banco de dados

* **Tests** → testes automatizados da API

## Funcionalidades

* Criar tarefas

* Listar tarefas

* Filtrar tarefas por status

* Marcar tarefa como concluída

* Deletar tarefa

* Verificar saúde da API

## 📡 Endpoints da API
```
  Método	   Endpoint	          Descrição
  POST	       /tasks/ 	          Criar uma nova tarefa
  GET	       /tasks/	          Listar todas as tarefas
  PATCH	       /tasks/{id}	      Marcar tarefa como concluída
  DELETE	   /tasks/{id}	      Deletar tarefa
  GET	       /tasks/health	  Verificar status da API

```

## 📥 Exemplo de requisição
### Criar tarefa
#### POST /tasks/
```
Body:

    {
    "title": "Estudar Flask"
    }

    Resposta:

    {
    "id": 1,
    "title": "Estudar Flask",
    "completed": false
    }
```
## 📄 Documentação da API

### A documentação interativa está disponível via Swagger UI:

### **/docs/swagger**

### Ela é gerada automaticamente utilizando Flask-Smorest e OpenAPI.

## 🧪 Testes automatizados

### Os testes foram implementados utilizando Pytest.

###  Testes localmente:

#### pytest

### A suíte de testes valida:

* criação de tarefas

* listagem de tarefas

* atualização de status

* remoção de tarefas

* endpoint de health check

## ⚙️ Integração contínua

### O projeto utiliza GitHub Actions para executar automaticamente os testes a cada push ou pull request.

### A pipeline realiza:

* instalação das dependências

* execução dos testes

* validação do build

## Executando o Projeto

### 1️⃣ Clonar repositório
### git clone https://github.com/scaglia-aylla1/100days-python-web.git
### 2️⃣ Entrar no diretório
  ####  todolist-api
### 3️⃣ Criar ambiente virtual
  #### python -m venv venv
### 4️⃣ Ativar ambiente

### Windows:

#### .\venv\Scripts\activate

### Linux/Mac:

#### source venv/bin/activate
### 5️⃣ Instalar dependências
#### pip install -r requirements.txt
### 6️⃣ Rodar migrações
#### flask db upgrade
### 7️⃣ Executar API
#### flask run

## 🧠 Competências demonstradas no projeto

Este projeto foi desenvolvido com foco em boas práticas de engenharia de software e desenvolvimento backend.

### 🔹 Desenvolvimento de APIs REST

* Criação de endpoints HTTP utilizando **Flask**
* Implementação de operações CRUD para gerenciamento de tarefas
* Uso correto de métodos HTTP (`GET`, `POST`, `PATCH`, `DELETE`)
* Estruturação de respostas JSON padronizadas

### 🔹 Arquitetura de Software

* Organização do projeto em **arquitetura em camadas**
* Separação clara de responsabilidades entre:

  * **Routes** (camada de API)
  * **Services** (lógica de negócio)
  * **Schemas** (validação e serialização)
  * **Models** (entidades de dados)

### 🔹 Persistência de Dados

* Modelagem de entidades com **SQLAlchemy**
* Uso de **ORM** para manipulação de dados
* Gerenciamento de versionamento do banco com **Flask-Migrate**

### 🔹 Validação de Dados

* Validação de entrada com **Marshmallow**
* Criação de schemas para serialização e desserialização de objetos
* Garantia de integridade dos dados enviados à API

### 🔹 Testes Automatizados

* Desenvolvimento de testes automatizados utilizando **Pytest**
* Testes de endpoints utilizando **Flask Test Client**
* Uso de banco de dados **SQLite em memória** para execução de testes isolados

### 🔹 Integração Contínua (CI)

* Configuração de pipeline com **GitHub Actions**
* Execução automática da suíte de testes a cada push ou pull request
* Garantia de estabilidade do projeto através de validação automática

### 🔹 Boas práticas de desenvolvimento

* Versionamento de código com **Git**
* Documentação automática da API com **OpenAPI / Swagger**
* Organização de código seguindo padrões utilizados em aplicações backend profissionais


## 📌 Melhorias futuras

* Autenticação de usuários

* Deploy em cloud


## 🧠 Propósito Profissional

### Este projeto faz parte da minha preparação para atuar como desenvolvedora web Python, aplicando práticas reais utilizadas no mercado de tecnologia.

## 📌 Status Atual

 ### 🚧 Em andamento 

## 👩‍💻 Autora

### Projeto desenvolvido por **Aylla Scaglia** durante estudos de desenvolvimento backend com Python.