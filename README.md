# Olimpiadas Python
Projeto proposto utilizando Django e Python, onde tenho que realizar a leitura de arquivos excel, tratar os dados e armazenar no banco de dados.

## Informções de uso
**Inicializar o servidor:** django-admin manage.py runserver  
**Executar os testes:** python manage.py test core  
**Usuário e senha:** admin

## Rotas
**Url admin:** 127.0.0.1:8000/admin  
**Url Home-page:** 127.0.0.1:8000 | 127.0.0.1:8000/ | 127.0.0.1:8000/home/  
**Url Upload dos arquivos:** 127.0.0.1:8000/upload/  


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
- [ ] Tela de visualização de região
- [ ] Tela de visualização de atleta
- [ ] Filtros de busca atleta
- [ ] Cadastrar atleta
- [ ] Apagar atleta
- [ ] Atualizar atleta
- [ ] Filtros de busca região
- [ ] Cadastrar região
- [ ] Apagar região
- [ ] Atualizar região
- [ ] Analise de tempo upload arquivo

## Analise de tempo  
Analises relacionadas ao upload e tratamento dos arquivos excel  
**Atletas:** 271116 linhas e 15 colunas  
**Paises:** 230 linhas e 3 colunas  
**Tempo de execucao:** Ainda não analisado  

## Modelo do banco de dados  

![image](https://user-images.githubusercontent.com/56879793/97120482-05ccb600-16f6-11eb-810b-73458f28e210.png)
