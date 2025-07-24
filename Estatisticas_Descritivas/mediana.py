import streamlit as st

# Funções para alternar a exibição dos exemplos
def toggle_example1():
    st.session_state['show_example1'] = not st.session_state['show_example1']
    
# Inicializando o estado da sessão para controlar a exibição dos exemplos
if 'show_example1' not in st.session_state:
    st.session_state['show_example1'] = False

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

st.title("O que é a Mediana?")

# Texto sobre a mediana
st.write("""
Considere que você está na posição de analista de dados encarregado de analisar as notas de desempenho de uma equipe ao longo do tempo.
As notas variam bastante, e você precisa encontrar uma forma eficiente de resumir essas informações. 
Nesse caso, uma solução simples e direta seria utilizar a mediana.
""")

# Botão para mostrar/ocultar o Exemplo 1
if st.button("Exemplo"):
    toggle_example1()

if st.session_state['show_example1']:
    st.write("""
    Considere as seguintes notas de desempenho:
    """)
    st.latex(r'''45, 50, 52, \textbf{55}, 60, 95, 98''')

    st.write("""
    Nesse caso, ao ordenar os dados, a mediana é o valor que ocupa o ponto central.  
    Como o conjunto tem 7 valores, o valor central é 55, o que representa a mediana.  
    Observe que, embora existam valores extremos como 45 e 98, esses outliers não influenciam a mediana, tornando-a uma escolha robusta para medir o centro dos dados.
    """)

st.write("""
Observe que a mediana é uma medida de tendência central que divide o conjunto de dados em duas partes iguais.
Para calcular a mediana, é necessário ordenar os dados e encontrar o valor central.
Se o conjunto de dados tiver um número par de elementos, a mediana é a média dos dois valores centrais.

###  Quando usar a mediana?

**Dados Ordinais:** Quando se trabalha com dados ordinais (dados que têm uma ordem, mas não necessariamente distâncias iguais entre os valores), a mediana pode ser uma melhor medida de tendência central do que a média.

**Distribuições Assimétricas:** Em distribuições assimétricas, onde os dados não são distribuídos uniformemente, a mediana pode ser uma representação mais precisa do centro do dataset do que a média.

**Identificação de assimetria:** Comparando a mediana com a média, pode-se ter uma ideia sobre a simetria da distribuição. Se a mediana for menor que a média, a distribuição pode ser assimétrica à direita, se for maior, a distribuição pode ser assimétrica à esquerda.
""")