# Olimpiadas Python
Projeto proposto utilizando Django e Python, onde tenho que realizar a leitura de arquivos excel, tratar os dados e armazenar no banco de dados.

## Informções de uso
**Inicializar o servidor:** django-admin manage.py runserver  
**Executar os testes:** python manage.py test core  
**Usuário e senha:** admin

## Rotas  
#### Paginas  

**Url admin:** 127.0.0.1:8000/admin  
**Url Home-page:** 127.0.0.1:8000 | 127.0.0.1:8000/ | 127.0.0.1:8000/home  
**Url Upload dos arquivos:** 127.0.0.1:8000/upload   
**Url listar atletas:** 127.0.0.1:8000/athlete/list  
**Url filtrar atletas:** 127.0.0.1:8000/athlete/filter  
**Url visualizar atletas:** 127.0.0.1:8000/athlete/view  
**Url criar atletas:** 127.0.0.1:8000/athlete/create  
**Url atualizar atletas:** 127.0.0.1:8000/athlete/update/<int:id>  
**Url adicionar participação de atletas:** 127.0.0.1:8000/athlete/participation/<int:id>  
**Url listar regiões:** 127.0.0.1:8000/region/list/  
**Url filtrar regiões:** 127.0.0.1:8000/region/filter/     

#### Rest  
**Url executar upload:** 127.0.0.1:8000/upload/submit  
**Url executar filtragem atletas:** 127.0.0.1:8000/athlete/filter/submit  
**Url executar deletar atleta:** 127.0.0.1:8000/athlete/delete/<int:id>  
**Url executar criação do atleta:** 127.0.0.1:8000/athlete/create/submit    
**Url executar atualizaçao atletas:** 127.0.0.1:8000/athlete/update/submit  
**Url executar cadatro de participação:** 127.0.0.1:8000/athlete/participation/submit  
**Url executar deletar participação:**  127.0.0.1:8000/athlete/<int:athlete>/participation/delete/<int:id>  
**Url executar filtragem regiões:** 127.0.0.1:8000/region/filter/submit   

## Tarefas
- [X] Home page
- [X] Tela de upload
- [X] Mensagem de erro upload 
- [X] Salvar regiões
- [X] Salvar esportes
- [X] Salvar eventos
- [X] Salvar cidades que ocorrem os jogos
- [X] Salvar as temporadas
- [X] Salvar os jogos
- [X] Salvar os eventos dos jogos
- [X] Salvar atleta
- [X] Salvar os atletas participantes
- [X] Readme.md
- [X] Testes templates/rotas
- [X] Otimizaçoes
- [X] Testes upload
- [ ] Testes TDD itens abaixo
- [X] listar atletas
- [X] Filtros de busca atleta
- [X] Tela de visualização de atleta
- [X] Cadastrar atleta
- [X] Apagar atleta
- [X] Atualizar atleta
- [X] Filtros de busca região
- [X] listar região
- [ ] Tela de visualização de região
- [ ] Cadastrar região
- [ ] Apagar região
- [ ] Atualizar região
- [ ] Analise de tempo upload arquivo
- [ ] Voltar melhorando (Upload esta despatronizado)
- [ ] Adicionar paginação no atleta

## Analise de tempo  
Analises relacionadas ao upload e tratamento dos arquivos excel  
**Atletas:** 271116 linhas e 15 colunas  
**Paises:** 230 linhas e 3 colunas  
**Tempo de execucao:** Ainda não analisado  

## Modelo do banco de dados  

![image](https://user-images.githubusercontent.com/56879793/97129878-b6e74680-171e-11eb-992d-798cbc177b9a.png)
