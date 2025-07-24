## Projeto de Estatística - Análise Descritiva e Inferencial
Este repositório contém um projeto de análise estatística desenvolvido em Python. O objetivo é fornecer uma ferramenta educacional que aborda tanto estatísticas descritivas quanto inferenciais, com uma aplicação prática e visual para facilitar a compreensão dos conceitos.

## Sumário
- Introdução
- Objetivos
- Estrutura do Projeto
- Configuração do Ambiente
- Descrição dos Módulos e Scripts
- Execução e Uso
- Contribuição
- Licença


## Introdução
Este projeto foi desenvolvido para servir como um guia prático para aqueles que desejam entender os fundamentos de estatística por meio de exemplos práticos em Python. A aplicação fornece uma interface interativa que inclui cálculos de medidas descritivas e inferenciais, um quiz para reforçar o aprendizado, e um chatbot de inteligência artificial para tirar dúvidas.

## Objetivos
Educação Estatística: Facilitar o aprendizado de estatística descritiva e inferencial com exemplos práticos.
Interatividade: Proporcionar uma experiência interativa através de um quiz e um chatbot de IA.
Ferramenta de Consultoria: Servir como uma referência para conceitos estatísticos comuns usados em análise de dados.

## Descrição dos Principais Arquivos e Módulos
- chat_ia.py: 
Um chatbot de inteligência artificial para responder perguntas básicas de estatística. Ideal para consultas rápidas ou dúvidas sobre os conceitos.

- index.py: 
O ponto de entrada do projeto, responsável por carregar a interface principal e integrar as funcionalidades de estatística descritiva e inferencial.

- mvp.py: 
Interface do projeto, desenvolvida para mostrar os resultados dos cálculos de forma visual e interativa.

- quiz.py: 
Script que apresenta um quiz sobre conceitos estatísticos para reforçar o aprendizado do usuário.

- respostas.db: 
Banco de dados SQLite que armazena as respostas dos usuários no quiz, permitindo monitorar o progresso.

- requirements.txt: 
Arquivo que lista todas as bibliotecas necessárias para rodar o projeto. É essencial para configurar o ambiente de maneira rápida.


## Pastas de Análise Estatística
Estatisticas_Descritivas: Scripts que abrangem os cálculos das medidas descritivas fundamentais, como média, mediana, moda, variância, e desvio padrão. Esses scripts facilitam a análise de dados e a compreensão das distribuições.

Estatisticas_Inferenciais: Contém scripts que realizam cálculos mais avançados, como assimetria, curtose, correlação e covariância, essenciais para análises de tendências e relações entre variáveis.

## Configuração do Ambiente
Pré-Requisitos
Certifique-se de ter o Python 3.7+ instalado. As bibliotecas necessárias estão listadas no arquivo requirements.txt, incluindo:

- numpy
- scipy
- pandas
- matplotlib
- streamlit


## Instalação
#### 1 - Clone este repositório:
`git clone https://github.com/seu-usuario/projeto-estatistica.git
cd projeto-estatistica
`
#### 2- Instale as dependências:
`pip install -r requirements.txt
`

## Descrição dos Módulos e Scripts
#### Estatísticas Descritivas
- media.py: Calcula a média de uma lista de valores.
- mediana.py: Calcula a mediana para um conjunto de dados.
- moda.py: Calcula a moda, ou valor mais frequente, em uma lista de valores.
- variancia.py: Calcula a variância, uma medida da dispersão dos dados.
- desvio_padrao.py: Calcula o desvio padrão, que indica a quantidade de variação dos dados em relação à média.
- distribuicao_normal.py: Visualiza uma distribuição normal.
- distribuicao_t.py: Gera uma distribuição t, útil para amostras pequenas.
- Estatísticas Inferenciais
- assimetria.py: Mede a assimetria de uma distribuição.
- curtose.py: Mede a curtose, ou achatamento, de uma distribuição.
- correlacao.py: Calcula a correlação entre duas variáveis, indicando a relação entre elas.
- covariancia.py: Calcula a covariância, que mostra a direção da relação linear entre variáveis.


## Execução e Uso
Executando a Interface Principal
Para iniciar a interface do projeto e explorar os cálculos estatísticos:
`python index.py
`

## Executando o Quiz de Estatística
O quiz interativo é uma ótima maneira de testar seus conhecimentos em estatística:
`python quiz.py`

## Interação com o Chatbot
Para utilizar o chatbot de IA e tirar dúvidas rápidas sobre estatística:

`python chat_ia.py`

## Scripts de Análise Estatística
Para cada conceito estatístico, você pode executar os scripts individualmente. Por exemplo, para calcular a média:

`python Estatisticas_Descritivas/media.py`

Contribuição
Contribuições para melhorar este projeto são bem-vindas! Por favor, siga estas diretrizes:

## Realize um fork do repositório.
- Crie uma branch para sua funcionalidade (git checkout -b feature/nova-funcionalidade).
- Commit suas mudanças (git commit -m 'Adiciona nova funcionalidade').
- Envie para o repositório remoto (git push origin feature/nova-funcionalidade).
- Abra um Pull Request para revisão.