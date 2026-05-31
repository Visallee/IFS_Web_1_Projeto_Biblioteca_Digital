# Biblioteca Digital - IFS Campus Lagarto

Aplicação web desenvolvida como requisito de avaliação para a disciplina de Programação Web I do curso de Bacharelado em Sistemas de Informação (BSI). O sistema consiste em uma biblioteca digital para gerenciar um acervo de livros, permitindo o cadastro de obras, categorização, controle de empréstimos e visualização de histórico por usuário.

**Professor:** Jean Louis Silva Santos

## 👥 Integrantes do Grupo
* Rauan Phelipe Nascimento de Jesus
* Victor Silva do Valle
* William Silva Santos

## 🚀 Como executar o projeto localmente

Siga o passo a passo abaixo para rodar a aplicação na sua máquina:

1. Clone este repositório:
   ```bash
   git clone [https://github.com/Visallee/IFS_Web_1_Projeto_Biblioteca_Digital.git](https://github.com/Visallee/IFS_Web_1_Projeto_Biblioteca_Digital.git)
   ```
2. Acesse a pasta do projeto:
   ```bash
   cd IFS_Web_1_Projeto_Biblioteca_Digital
   ```
3. Crie e ative o ambiente virtual:
   ```bash
   python -m venv .venv
   # No Windows:
   .venv\Scripts\activate
   # No Linux/Mac:
   source .venv/bin/activate
   ```
4. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
5. Aplique as migrações do banco de dados (os dados iniciais já serão carregados automaticamente):
   ```bash
   python manage.py migrate
   ```
6. Inicie o servidor local:
   ```bash
   python manage.py runserver
   ```
7. Acesse no navegador: `http://127.0.0.1:8000/`

## 📋 Requisitos Funcionais Implementados

* **RF01 - Autenticação:** Cadastro, login e logout utilizando o sistema nativo do Django.
* **RF02 - Perfil:** Tela para visualização e edição dos dados do usuário autenticado.
* **RF03 - Modelo Central:** Entidade `Livro` com mais de 5 campos (título, autor, isbn, ano_publicacao, editora, quantidade_disponivel).
* **RF04 - CRUD Completo:** Listagem, criação, edição e exclusão de Livros restritos a usuários logados.
* **RF05 - Relacionamentos:** Relacionamento entre `Livro` e `Categoria` (ForeignKey/ManyToMany) e `Livro` e `Usuario` (através de Empréstimos).
* **RF06 - Formulários:** Utilização de ModelForms com validações customizadas.
* **RF07 - Busca/Filtro:** Barra de pesquisa funcional na listagem de livros via parâmetro GET.
* **RF08 - Controle de Acesso:** Views protegidas pelo `@login_required` e validação para garantir que apenas quem criou um registro possa excluí-lo (quando aplicável).
* **RF09 - Templates:** Uso de herança com `base.html`, feedback com Django Messages e layout responsivo.
* **RF10 - Migrations:** Banco de dados SQLite funcional. Os dados iniciais de testes (categorias e livros) são carregados automaticamente de forma inteligente utilizando Data Migrations.

## 📸 Capturas de Tela

## TELA INICIAL
<img width="1440" height="900" alt="tela_inicial" src="https://github.com/user-attachments/assets/e2c60bd1-5c3b-48d9-bfeb-2c70389c751a" />
*Página inicial com a listagem do acervo.*

## TELA CADASTRO
<img width="1440" height="900" alt="tela_cadastro" src="https://github.com/user-attachments/assets/82621242-2ca0-4167-afdb-5f260f4059c1" />
*Formulário de cadastro de novo livro e validações.*
