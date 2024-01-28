# Blog Django - Um blog simples e fácil de usar

O Blog Django é um aplicativo web desenvolvido em Python com o framework Django, que permite criar posts e páginas pelo painel admin, sem precisar programar. Você pode usar o Blog Django para compartilhar seus conhecimentos, ideias, opiniões e muito mais.

## Funcionalidades Principais

- **Criação de Posts:** Você pode criar posts com título, conteúdo, imagem, categoria e tags, usando o painel admin do Django.
- **Criação de Páginas:** Você pode criar páginas estáticas com título e conteúdo, usando o painel admin do Django.
- **Listagem de Posts:** Você pode ver todos os posts publicados em uma página, com paginação, ordenação e filtro por categoria e tag.
- **Detalhe de Post:** Você pode ver o conteúdo completo de um post, com a imagem, a data, a categoria, as tags e os comentários.
- **Comentários:** Você pode deixar um comentário em um post, informando seu nome, email e mensagem. Os comentários são moderados pelo admin do blog.
- **Busca:** Você pode buscar posts pelo título ou pelo conteúdo, usando uma caixa de pesquisa no cabeçalho do blog.

## Como Testar

**Pré-requisitos:**

- [Git](https://git-scm.com/) instalado no seu computador.
- [Docker](https://www.docker.com/) instalado no seu computador.
- [PostgreSQL](https://www.postgresql.org/) instalado no seu computador.

**Instalação:**

Clone o repositório:

```bash
git clone https://github.com/seu-usuario/blog-django.git
```

Navegue até o diretório do projeto:

```bash
cd blog-django
```

Crie um arquivo .env com as variáveis de ambiente necessárias para o projeto, como o nome do banco de dados, o usuário, a senha, o host e a porta. Você pode usar o arquivo .env.example como referência.

Execute o comando docker-compose para criar e iniciar os contêineres do projeto:

```bash
docker-compose up -d
```

Acesse o painel admin do Django no seu navegador: http://localhost:8000/admin

Use o usuário e a senha que você definiu nas variáveis de ambiente para fazer login.

Crie os posts e as páginas que você quiser pelo painel admin.

Acesse o blog no seu navegador: http://localhost:8000/

Você pode acessar o site diretamente por esse link, se quiseres ver ele online http://34.125.225.100/


## Licença

Este projeto está licenciado sob a licença MIT - consulte o arquivo LICENSE para obter detalhes.

Desenvolvido Andre Morais | [GitHub](https://github.com/Andrersm)

