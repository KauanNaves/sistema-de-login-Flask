# Sistema Simples de Autenticação de Usuários

Sistema de controle de acesso desenvolvido em Python, usando o framework Flask, para estudo de autenticação de usuários, persistência de dados e gerenciamento de sessões.


## Como Executar Localmente (Local Setup)

### Pré-requisitos (*Pre-requisites*)
* Python 3.14.4 instalado.

### Instalação e Execução (*Installation & Run*)
1. Clone o repositório:
    'git clone <https://github.com/KauanNaves/sistema-de-login-Flask.git>'

2. Acesse o diretório do projeto:
    'cd sistema-de-login-Flask'

3. Crie e ative o ambiente virtual (*Virtual Environment*)
    * Windows: 'python -m venv venv' e 'venv\Scripts\activate'
    * Linux/macOS: 'python3 -m venv venv' e 'source venv/bin/activate'

4. Instale as dependências:
    'pip install -r requirements.txt'

5. Inicie o servidor da aplicação e clique na url gerada:
    'flask run'


## Funcionalidades (*Features*)
* **User Authentication:** Cadastro e validação de credenciais de usuários.
* **Session Management:** Controle de estado do usuário autenticado via sessões HTTP.
* **Access Control** Restrição de rota protegida apenas para usuários logados.
* **Data Persistence:** Armazenamento local de usuários utilizando banco de dados relacional.


## Tecnologias Utilizadas (*Tech Stack*)
* Python
* SQLite
* Flask
* Werkzeug


## Aprendizados e Desafios Técnicos (*Learnings & Technical Challenges*)
* **Gerenciamento de Estado (*State Management*):** Compreensão prática da implementação de sessões para contornar a natureza *stateless* do protocolo HTTP.
* **Integração com Banco de Dados (*Database Integration*):** Estruturação de queries SQL (operações CRUD) e conexão do banco de dados relacional (*Relational Database*) SQLite com a lógica da aplicação Python.
* **Segurança de Credenciais (*Password Security*):** Aplicação de funções de *hash* criptográfico unidirecional (*One-way Cryptographic Hashing*) utilizando a biblioteca `werkzeug.security` (`generate_password_hash` e `check_password_hash`) para garantir que as senhas não sejam armazenadas em texto plano (*plain text*).
* **Interceptação de Requisições (*Request Hooks*):** Utilização do decorador (*Decorator*) `@app.before_request` em conjunto com o objeto global `g` do Flask para carregar o contexto do usuário autenticado de forma global antes da renderização das rotas (*Routing*).
* **Controle de Acesso (*Authorization*):** Criação e aplicação do decorador customizado `@login_required` para modularizar e reutilizar a lógica de proteção das páginas restritas do sistema.
