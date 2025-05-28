# 🏫 API de Reserva de Salas

API desenvolvida para permitir a **reserva de salas** em um ambiente escolar, com integração direta à **API de Gestão Escolar**.

Esta API garante que:
- A sala exista no sistema.
- Haja um professor válido vinculado à reserva.

Essa integração promove **consistência entre dados**, **controle eficaz de recursos** e facilita a **organização do uso de espaços escolares**.

---

## 🚀 Tecnologias Utilizadas

- **Python** – Linguagem principal do projeto
- **Flask** – Framework web leve e flexível para criação de APIs
- **Flask-RESTx** – Criação de APIs RESTful com documentação automática
- **Flask-JWT-Extended** – Autenticação via tokens JWT
- **Flask-SQLAlchemy** / **SQLAlchemy** – ORM para integração com banco de dados
- **openpyxl** – Leitura e escrita de arquivos `.xlsx`
- **requests** – Requisições HTTP para integração com a API externa
- **python-dotenv** – Variáveis de ambiente a partir do `.env`
- **black**, **autopep8** – Padronização e formatação de código

---

## 📁 Estrutura do Projeto
```sh
reserva_sala_api/
├── app.py # Arquivo principal da aplicação
├── config.py # Configurações (ex: banco, JWT, .env)
├── database.py # Conexão com banco de dados
├── requirements.txt # Dependências do projeto
├── README.md
├── instance/
│ └── banco.db # Banco de dados SQLite
├── models/
│ ├── ReservaModel.py # Modelo da reserva
│ └── SalaModel.py # Modelo da sala
├── routes/
│ ├── HomeRoute.py # Rota de status da API
│ ├── ReservaRoute.py # Rotas relacionadas à reserva
│ └── SalaRoute.py # Rotas relacionadas à sala
└── services/
└── GestaoEscolarService.py # Comunicação com API de Gestão Escolar
```
---

## Como Rodar o Projeto (Via Docker)
### 🔨 Fazendo o build da imagem
```sh
docker compose build
```
Isso usará o build definido no docker-compose.yml, criará a imagem reserva-sala-api:1.0 e já prepara tudo pro up.
### 🚀 Rodando a aplicação
```sh
docker compose up
```
ou em modo "background":
```sh
docker compose up -d
```
### ⛔ Parando a aplicação:
```sh
Ctrl+C
```
ou em modo "background":
```sh
docker compose down
```
### ❌ Apagando a imagem:
**Usando docker compose:**
```sh
docker compose down --rmi all
```
`--rmi all` remove todas as imagens construídas pelo docker compose;
`-v` se quiser também remover volumes

---

## ⚙️ Como Executar Localmente

```bash
# Clone o repositório
git clone https://github.com/WallyssonSousa/reserva_sala_api.git
cd reserva_sala_api

# Criar e Ativar um Ambiente Virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate  # Windows

#  Instalar Dependências
pip install -r requirements.txt

# Configurar o Banco de Dados
flask db init
flask db migrate -m "Inicialização do banco de dados"
flask db upgrade

# Rodar o Servidor Flask - O servidor será iniciado em http://127.0.0.1:5000/
python app.py

# Como Executar os Testes
pytest
