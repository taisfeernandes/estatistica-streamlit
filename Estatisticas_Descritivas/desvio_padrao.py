import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Inicializando o estado da sessão para controlar a exibição dos exemplos
if 'show_example_1' not in st.session_state:
    st.session_state['show_example_1'] = False
if 'show_example_2' not in st.session_state:
    st.session_state['show_example_2'] = False

# Função para alternar a exibição dos exemplos
def toggle_example_1():
    st.session_state['show_example_1'] = not st.session_state['show_example_1']
def toggle_example_2():
    st.session_state['show_example_2'] = not st.session_state['show_example_2']

# CSS para estilizar os botões
st.markdown("""
    <style>
    .stButton > button {
        background-color: #00494f;
        color: white;
        border-radius: 10px;
        height: 80px;
        width: 200px;
        font-size: 18px;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

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

st.title("O que é desvio padrão?")
st.write("""
O desvio padrão nos ajuda a entender o grau de variação ou dispersão de um conjunto de números em relação à média,
nos mostrando se os dados são mais uniformes ou mais variados. Seu cálculo se dá simplesmente por meio da raiz 
quadrada da variância, o que torna mais intuitiva a visualização.
""")

# Botões para mostrar/ocultar os exemplos
if st.button("Mostrar exemplo 1: Idade dos colaboradores"):
    toggle_example_1()

if st.button("Mostrar exemplo 2: Idade dos alunos"):
    toggle_example_2()

# Exemplo 1
if st.session_state['show_example_1']:
    st.write("""
    ### Exemplo 1: Idade dos Profissionais (Grande desvio padrão)
    Considere as seguintes idades de um grupo de colaboradores:
    """)
    st.latex(r'''18, 22, 25, 30, 35, 40, 45, 50, 52, 55, 58, 60, 61, 24, 38''')

    st.write("""
    O primeiro passo é calcular a média dessas idades:
    """)
    media_idades = 40.87  

    st.latex(r'''
    \bar{{x}} = \frac{{18 + 22 + 25 + 30 + 35 + 40 + 45 + 50 + 52 + 55 + 58 + 60 + 61 + 24 + 38}}{{15}} = 40.87
    ''')

    st.write("""
    Agora, vamos calcular a variância. Primeiro, subtraímos a média de cada valor, elevamos ao quadrado e somamos:
    """)

    st.latex(r'''
    \text{{Variância}} = \frac{{(18 - 40.87)^2 + (22 - 40.87)^2 + (25 - 40.87)^2 + \cdots + (38 - 40.87)^2}}{15}
    ''')
    variancia_idades = 456.47  

    st.latex(r'''
    \text{{Variância}} = \frac{{6847.07}}{15} = 456.47
    ''')

    st.write("""
    Agora, para calcular o desvio padrão, basta tirar a raiz quadrada da variância:
    """)

    desvio_padrao = np.sqrt(variancia_idades) 

    st.latex(r'''
    \text{{Desvio Padrão}} = \sqrt{{456.47}} = 21.37
    ''')
    st.write("""
    Como pudemos ver, é mais intuitivo analisarmos um desvio padrão de 21.37 do que uma variância de 456.47,
    já que os valores das idades estão mais próximos do desvio padrão do que da variância. 
    """)

# Exemplo 2
if st.session_state['show_example_2']:
    st.write("""
    ### Exemplo 2: Idade dos Alunos (Pequeno desvio padrão)
    Considere a seguinte distribuição de idades em uma sala de aula com 15 alunos:
    """)
    st.latex(r'''16, 16, 16, 16, 16, 16, 16, 16, 17, 17, 17, 17, 17, 18, 18''')

    st.write("""
    O primeiro passo é calcular a média dessas idades:
    """)

    # Lista com as idades dos alunos
    idades_alunos = [16, 16, 16, 16, 16, 16, 16, 16, 17, 17, 17, 17, 17, 18, 18]
    media_alunos = sum(idades_alunos) / len(idades_alunos)

    st.latex(r'''
    \bar{{x}} = \frac{{16 + 16 + 16 + 16 + 16 + 16 + 16 + 16 + 17 + 17 + 17 + 17 + 17 + 18 + 18}}{{15}} = {:.2f}
    '''.format(media_alunos))

    st.write("""
    Agora, vamos calcular a variância. Primeiro, subtraímos a média de cada valor, elevamos ao quadrado e somamos:
    """)

    variancia_alunos = sum((x - media_alunos) ** 2 for x in idades_alunos) / len(idades_alunos)

    st.latex(r'''
    \text{{Variância}} = \frac{{(16 - 16.60)^2 + (16 - 16.60)^2 + \cdots + (18 - 16.60)^2}}{15}
    ''')
    st.write(f"Variância dos alunos: {variancia_alunos:.2f}")
    st.write("""
    Agora, para calcular o desvio padrão, basta tirar a raiz quadrada da variância:
    """)

    desvio_padrao_alunos = np.sqrt(variancia_alunos)

    st.latex(r'''
    \text{{Desvio Padrão}} = \sqrt{{\text{{Variância}}}} = {:.2f}
    '''.format(desvio_padrao_alunos))

    st.write(f"Desvio padrão dos alunos: {desvio_padrao_alunos:.2f}")
    st.write("""
    O desvio padrão do segundo exemplo é muito menor que o do primeiro, o que significa que os valores das
    idades dessa sala de aula no geral se aproximam da média dessas idades muito mais do que as idades do
    grupo de colaboradores se aproximam da média das idades desse grupo.          
    """)