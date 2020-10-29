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
**Url visualizar regiões:** 127.0.0.1:8000/region/view/  
**Url Criar nova regiao:** 127.0.0.1:8000/region/create/  
**Url Update de regiões:** 127.0.0.1:8000/region/update/<int:id>'  
    
#### Rest  
**Url executar upload:** 127.0.0.1:8000/upload/submit  
**Url executar filtragem atletas:** 127.0.0.1:8000/athlete/filter/submit  
**Url executar deletar atleta:** 127.0.0.1:8000/athlete/delete/<int:id>  
**Url executar criação do atleta:** 127.0.0.1:8000/athlete/create/submit    
**Url executar atualizaçao atletas:** 127.0.0.1:8000/athlete/update/submit  
**Url executar cadatro de participação:** 127.0.0.1:8000/athlete/participation/submit  
**Url executar deletar participação:**  127.0.0.1:8000/athlete/<int:athlete>/participation/delete/<int:id>  
**Url executar filtragem regiões:** 127.0.0.1:8000/region/filter/submit  
**Url executar a exclusão regiões:** 127.0.0.1:8000/region/delete/<int:id>  
**Url executar a criação regiões:** 127.0.0.1:8000/region/create/submit  
**Url executar a atualizacão regiões:** 127.0.0.1:8000/region/update/submit     

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
- [X] Tela de visualização de região
- [X] Cadastrar região
- [X] Apagar região
- [X] Atualizar região
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
  
## Telas do sistema

#### Home page  
![image](https://user-images.githubusercontent.com/56879793/97598406-b0d6bb80-19e5-11eb-8f71-2987b1decf04.png)  

#### Upload de arquivos  
![image](https://user-images.githubusercontent.com/56879793/97598789-1460e900-19e6-11eb-85c4-3701daab4ebe.png)  

#### Criar/Atualizar Atleta  
![image](https://user-images.githubusercontent.com/56879793/97599044-59851b00-19e6-11eb-84b0-870efe216fe2.png)  

#### Filtagem de atletas  
![image](https://user-images.githubusercontent.com/56879793/97599482-d2847280-19e6-11eb-9024-bc238ec0fd9f.png)  

#### Listagem de atletas (imagem sem passar por filtragem)  
![image](https://user-images.githubusercontent.com/56879793/97599733-0fe90000-19e7-11eb-8275-13c0b2c65bbf.png)

#### Visualizar atleta   
![image](https://user-images.githubusercontent.com/56879793/97599998-5a6a7c80-19e7-11eb-8b5f-d702f14b8bb2.png)  

#### Registrar participação de atleta em evento   
![image](https://user-images.githubusercontent.com/56879793/97600141-8423a380-19e7-11eb-82b6-db83fabb4496.png)  

#### Cadastrar/atualizar país/região   
![image](https://user-images.githubusercontent.com/56879793/97600330-b33a1500-19e7-11eb-9ef0-9c48f769164c.png)  

#### Filtro de países  
![image](https://user-images.githubusercontent.com/56879793/97600493-e1b7f000-19e7-11eb-917d-11b8a34dcfa7.png)  

#### Lista de países  
![image](https://user-images.githubusercontent.com/56879793/97600727-204daa80-19e8-11eb-9eed-0565637de873.png)  

#### Visualização de país  
![image](https://user-images.githubusercontent.com/56879793/97600868-48d5a480-19e8-11eb-8eb1-4f3b376728c8.png)  


