# Processo seletivo Sersorville
**Autor**: Andre Prasel

**Objetivo**: contar um pouco sobre minha trajetória pessoal, familiar
e profissional.

**Resumo**: site feito com o framework Django, carregando templates HTML e arquivos
estáticos CSS e JavaScript.

---

## Como usar o site
Como o site usa o framework Django para o seu funcionamento, é importante
que o ele esteja instalado. Para isso recomendo os seguintes passos:

1. Iniciar um ambiente virtual python: isso evita que as dependências
sejam instaladas de forma global na máquina. Assim, navegue até a pasta do projeto
pelo terminal e digite o comando:

```python
python -m venv venv  # OU
python3 -m venv venv 
```

2. Instalar o framework Django: para instalar o Django no ambiente virtual 
criado primeiramente é necessário ativá-lo:

```python
# Caminhe até venv/Scripts e execute o arquivo compatível com seu sistema operacional
venv/Scripts/Activate.ps1  # estou usando Windows

# Após isso, instale o framework
pip install django
```

3. Iniciar o site: após instalar o Django já é possível iniciar o servidor local.
Use o comando:

```python
# Certifique-se de estar na pasta raiz do projeto e que o ambiente virtual esteja ativado
python manage.py runserver
```

O site irá abrir por padrão na porta 8000 do servidor local. No terminal é póssivel
clicar no link do servidor ou use seu navegador de preferencência 
e acesse: http://127.0.0.1:8000/

---
## Sobre a construção do site

Iniciei o projeto primeiro pensando em sua organização. Para isso, duas etapas foram feitas:
organizar as ideias e organizar a estrutura do projeto. Para a organização de ideias 
e controle das etapas concluídas usei um aplicativo de notas chamado Notion.

![Notion do Projeto](https://raw.githubusercontent.com/andreprs/processo-seletivo/main/images/notion_do_projeto.png)

Usando o comando `django-admin startproject minha_jornada .` iniciei
a base do site. Em seguida, usando `python .\manage.py startapp blog` criei o app 
responsável por todas as páginas do site (home, trajetória pessoal e profissional).
Ao criar o app também foi necessário fazer todas as etapas para "cadastrar" esse app na base do projeto.
Por fim, para terminar a base na qual o site seria construído, 
criei as pastas onde ficariam os arquivos estáticos (arquivos acessados 
pelas tags do Django). 

Terminando isso, a estrutura de pastas do projeto ficou da seguinte forma:

![Estrutura do Projeto](https://raw.githubusercontent.com/andreprs/processo-seletivo/main/images/estrutura_do_projeto.png)


**Ferramentas utilizadas**: além de usado o framework Django, para escrever os códigos usei o editor de códigos
da microsoft, o Visual Studio Code, juntamente do git para fazer o versionamento dos códigos. 

## Percepções sobre o processo de construção

Quero destacar aqui algumas percepções que tive durante a construção do site. Considero isso uma parte importante para a construção de algo e também
para o aprendizado. Identificar os pontos fortes e fracos pode não ser muito fácil, 
mas pode ser tornar um grande aliado. Dessa forma, aponto os seguintes pontos:

* Certo domínio na construção e manipulação da base do projeto, ou seja, 
na organização dos arquivos e saber o que alterar da base 
criada pelo comando Django;

* Dificuldade em construir um site totalmente responsivo (adaptável de acordo com 
tamanho da tela ou dispositivo). Assim foquei em construir um site totalmente focado para a versão 
desktop;

* Facilidade com o versionamento dos arquivos com o git, ajudando em alterações que fui fazendo
durante a construção.
