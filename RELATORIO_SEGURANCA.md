# Relatório de Auditoria de Segurança

**Disciplina:** Programação Web I
**Projeto:** Biblioteca Digital

## Itens Verificados e Corrigidos

* **RS01 (Configuração de Produção):** O arquivo `settings.py` foi atualizado. O `DEBUG` passou a ser controlado por variável de ambiente (`DJANGO_DEBUG`), com padrão seguro `False`. Isolamos a `SECRET_KEY` para ser lida por variável de ambiente (`os.environ.get`) e configuramos `ALLOWED_HOSTS`. `SESSION_COOKIE_SECURE` e `SECURE_SSL_REDIRECT` foram acoplados ao `DEBUG` (`not DEBUG`), de modo que ficam ativos automaticamente sempre que o projeto não estiver em modo de desenvolvimento. **Ressalva de operação:** como o `runserver` não serve HTTPS, é necessário exportar `DJANGO_DEBUG=True` para rodar localmente (documentado no README); optamos por manter o padrão `False` (seguro) em vez de inverter essa lógica, para evitar que alguém esqueça de desativar o modo debug em produção. Adicionamos também `SESSION_COOKIE_HTTPONLY = True` e mantivemos `X_FRAME_OPTIONS = 'DENY'` para evitar Clickjacking.
* **RS02 (Autorização IDOR):** Identificamos o risco nas views de edição e exclusão de Livros. A correção foi substituir buscas genéricas por `get_object_or_404(Livro, pk=pk, cadastrado_por=request.user)`, garantindo que o usuário só interaja com os livros que ele mesmo cadastrou.
* **RS03 (Política de Senhas):** O `AUTH_PASSWORD_VALIDATORS` foi atualizado com o `MinimumLengthValidator` (10 caracteres mínimos) e o `CommonPasswordValidator` para bloquear senhas fracas da lista do framework.
* **RS04 (CSRF):** Realizada auditoria nos templates (como `form_livro.html`, `confirmar_exclusao.html`, `login.html`). Todos os formulários `POST` possuem o token `{% csrf_token %}` e nenhuma view utiliza `@csrf_exempt`.
* **RS05 (XSS):** Auditoria nos templates confirmou que a proteção nativa de autoescape do Django está ativa. Não existem ocorrências das tags `|safe` ou do método `mark_safe()` em variáveis alimentadas pelos usuários.
* **RS06 (Logging):** O dicionário `LOGGING` foi configurado no `settings.py`. Adicionamos um evento de nível `INFO` na view `excluir_livro` para auditar sempre que um livro for deletado do acervo.
* **Atualização de Dependências:** Como parte da auditoria, verificamos as versões das bibliotecas em `requirements.txt` e atualizamos o Django de 6.0.5 para 6.0.7 (última versão estável disponível), que corrige três falhas de segurança de severidade baixa, incluindo uma relacionada a cache de respostas contendo cookies de sessão. `asgiref` e `tzdata` também foram atualizados para suas versões mais recentes.

## Risco Remanescente Identificado
Não implementamos proteção contra ataques de força bruta no login (como o uso da biblioteca `django-axes`), por limitação de tempo do escopo da atividade.

---
**Integrantes do Grupo:**
* Rauan Phelipe Nascimento de Jesus
* Victor Silva do Valle
* William Silva Santos