import streamlit as st

if 'calculo' not in st.session_state:
    st.session_state['calculo'] = False
if 'exemplo1' not in st.session_state:
    st.session_state['exemplo1'] = False


# Funções para alternar a exibição dos exemplos
def calculo():
    st.session_state['calculo'] = not st.session_state['calculo']

def exemplo1():
    st.session_state['exemplo1'] = not st.session_state['exemplo1']



# CSS para estilizar os botões
st.markdown("""
    <style>
    .stButton > button {
        background-color: #00494f;
        color: white;
        border-radius: 10px;
        height: 50px;
        width: 200px;
        font-size: 18px;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# CSS para mudar a cor da fonte
st.markdown("""
    <style>
    /* Define a cor da fonte para todo o corpo */
    body {
        color: #00494f;
    }
    h1, h2, h3, h4, h5, h6 {
        color: #00494f;
    }
    </style>
    """, unsafe_allow_html=True)


# Título principal
st.title("O que é a média aritmética?")

# Introdução com conceito da média
st.write("""
Imagine que você é um analista que precisa entender as rendas de um grupo de clientes. Cada cliente tem uma renda mensal diferente e, com tantas variações, como você poderia resumir essas informações de forma clara? A resposta está na **média**. 

A média é uma ferramenta valiosa que permite condensar todos esses números em um único valor, representando o comportamento geral do grupo e facilitando a compreensão dos dados. Em termos simples, a média é uma forma de encontrar um número que represente o centro dos seus dados. Ela ajuda a resumir valores, em um único número, capturando o **padrão central** do grupo.
""")


# Botão para mostrar/ocultar o botao 1 
if st.button("Como calcular a Média?"):
    calculo()

# Exibição condicional do Exemplo 1
if st.session_state['calculo']:
   st.write("""Para calcular a média, basta somar todos os valores e dividir pelo número de itens.
   """)
   st.latex(r'''
    \text{Média} = \frac{\text{Soma dos Valores}}{\text{Número de Valores}}
    ''')

# Botão para mostrar/ocultar o botao 2
if st.button("Vizualizar Exemplo"):
    exemplo1()

# Exibição condicional do Exemplo 2
if st.session_state['exemplo1']:
    st.write("""
    
    Vamos considerar as rendas mensais de 10 pessoas:

    - R$ 2.500
    - R$ 3.000
    - R$ 4.500
    - R$ 1.800 
    - R$ 3.200
    - R$ 5.000
    - R$ 2.200
    - R$ 4.000
    - R$ 3.600
    - R$ 3.800

    Para calcular a média, somamos todas as rendas e dividimos pelo número de pessoas.
    """)

     # Dados de renda
    rendas = [2500, 3000, 4500, 1800, 3200, 5000, 2200, 4000, 3600, 3800]
    soma_rendas = sum(rendas)
    numero_pessoas = len(rendas)

    # Cálculo da média
    media = soma_rendas / numero_pessoas

    # Cálculo no LaTeX
    st.latex(r'''
    \text{Média} = \frac{2500 + 3000 + 4500 + 1800 + 3200 + 5000 + 2200 + 4000 + 3600 + 3800}{10} = \frac{33600}{10} = 3360
    ''')

    # Exibindo a média
    st.write(f"A média da renda mensal deste grupo é **R$ {media:.2f},** oferecendo uma visão geral da renda do grupo.")

st.subheader("A Importância da Média")
st.write("""
A média é uma medida simples, mas poderosa para simplificar a análise de dados, mas não deve ser a única métrica considerada. Ao utilizar a média, podemos:

- **Identificar padrões**: Ela revela o valor típico de um grupo, permitindo-nos entender o comportamento geral.
- **Comparar segmentos**: Facilita a análise de diferentes grupos ou períodos, ajudando a identificar diferenças significativas.
- **Investigar variações**: Quando um valor se destaca, seja por estar muito acima ou abaixo da média, isso sinaliza a necessidade de uma análise mais aprofundada.

Em resumo, a média é um ponto de partida fundamental na análise de dados, mas deve sempre ser acompanhada por outras métricas para construir um quadro mais claro e informativo.
    """)
