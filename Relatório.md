# Relatório 01 - Laboratório de Experimentação de Software

**Guilherme Luiz Carvalho Pinto**

**Pedro Vítor Felix da Costa**

---

_Curso de Engenharia de Software, Unidade Praça da Liberdade_

_Instituto de Informática e Ciências Exatas – Pontifícia Universidade de Minas Gerais (PUC MINAS), Belo Horizonte – MG – Brasil_

---
<br>

# 1. Introdução

Os repositórios populares do GitHub possuem os mais diversos conteúdos e comportamentos. Para entedê-los é necessário analisar a atividade deles para compreender o que faz com que tantas pessoas interajam com esses repositórios, sendo assim necessário avaliar fatores que caracterizam a atividades desses projetos. Esse relatório visa analisar características dos 1000 repositórios com mais estrelas do GitHub.

# 2. Hipóteses

**RQ 01. Sistemas populares são maduros/antigos?**

Considerando que um sistema antigo tenha 5 anos ou mais, pode se considerar que um sistema popular é antigo, pois até o repositório alcançar notoriedade e atingir uma quantidade razoável de forks e favoritos ele deve ser divulgado e é necessário que o código se torne relevante para comunidade.

**RQ 02. Sistemas populares recebem muita contribuição externa?**

O fato dos repositórios populares terem grande visibilidade faz com que ele tenha muitas contribuições externas se comparado a repositórios não populares, desconsiderando os repositórios de cursos e conteúdo de aprendizado. A colaboração pode não ser tão relevante se comparada a colaboração dos criadores do repositório, mas a quantidade é muito maior se comparados a sistemas com baixa popularidade.

**RQ 03. Sistemas populares lançam releases com frequência?**
	
Considerando que os sistemas populares utilizam o SCRUM como metodologia de desenvolvimento e essa metodologia prega a entrega contínua de produto, pode se dizer que esses sistemas lançam releases frequentemente.

**RQ 04. Sistemas populares são atualizados com frequência?**
	
O fato de ser atualizado com frequência é uma junção dos fatores citados acima. Além de receber muitas colaborações externas, os repositórios por usarem o SCRUM realizam entregas frequentes, gerando atualização frequente do sistema.

**RQ 05. Sistemas populares são escritos nas linguagens mais populares?**
	
Sendo as linguagens populares de maior interesse dos desenvolvedores, os sistemas populares têm maior probabilidade de adquirir notoriedade se desenvolvidos nessas linguagens, então pode se dizer que sim.

**RQ 06. Sistemas populares possuem um alto percentual de issues fechadas?**
	
Como mencionado anteriormente, sistemas populares em sua maioria possuem cinco anos ou mais e provavelmente possuem versões estáveis atualmente, possuindo poucas melhorias ou adição de funcionalidade se comparado ao que já foi feito anteriormente. Sendo assim, sistemas populares possuem alto percentual de issues fechadas.

# 3. Metodologia
A fim de buscar informações sobre os repositórios, utilizou-se a API fornecida pelo GitHub. Para isso, foi construído um script em pyhton - ver queryGraphQL.py - realizando do consulta dos seguintes parâmetros:

- Total de pull requests;
- Total de releases;
- Linguagem principal do repositório;
- Total de issues;
- Total de issues fechadas;
- Data de criação do repositório;
- Data da última atualização do repositório.

O script realiza consultas na API do GitHub, utilizando a paginação, com o intuito de recuperar os 1000 registros. A paginação é necessária devido a limitação do tamanho de retorno.

Utilizando os dados retornados, são calculadas algumas métricas necessárias para investigar as hipotéses descritas na seção 2. As métricas calculadas são:

- Idade do repositório em anos: subtração da data de execução do script e a data de criação do repositório;
- Idade do repositório em meses: cálculo similar ao da idade do repositório, porém exibindo o valor em meses;
- Média de releses por mês: quantidade total de releases dividida pela idade em meses;
- Quantidade de dias da última atualização: subtração da data de execução pela data da última atualização.

Ao final da execução do script, é salvo um csv com os dados do projeto e são plotados gráficos para análise dos dados.

# 4. Resultados

# 6. Discussão





