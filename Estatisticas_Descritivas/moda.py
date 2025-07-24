import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statistics import multimode


# Inicializando o estado da sessão para controlar a exibição dos exemplos
if 'show_example1' not in st.session_state:
    st.session_state['show_example1'] = False
if 'show_example2' not in st.session_state:
    st.session_state['show_example2'] = False
if 'show_example3' not in st.session_state:
    st.session_state['show_example3'] = False

# Funções para alternar a exibição dos exemplos
def toggle_example1():
    st.session_state['show_example1'] = not st.session_state['show_example1']

def toggle_example2():
    st.session_state['show_example2'] = not st.session_state['show_example2']

def toggle_example3():
    st.session_state['show_example3'] = not st.session_state['show_example3']

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

# Título e explicação sobre a moda
st.title("O que é moda?")
st.write("""
Quando temos uma amostra, contamos com diversas formas de visualizar como os elementos se comportam. 
A moda é um conceito da estatística que corresponde ao **elemento mais frequente em uma amostra**, sendo
especialmente útil para casos em que estamos observando variáveis que não representam números.
""")

# Botão para mostrar/ocultar o Exemplo 1
if st.button("Exemplo 1: Qual sua cor favorita?"):
    toggle_example1()

# Exibição condicional do Exemplo 1
if st.session_state['show_example1']:
    st.write("""
    **Exemplo 1**: Qual sua cor favorita?
                
    Perguntamos a todos os dez colaboradores de um certo time qual a cor favorita de cada um. 
    Obtemos a seguinte lista:
                
            {Verde, Rosa, Vermelho, Azul, Verde, Amarelo, Azul, Verde, Rosa, Preto}
             
    A moda, nesse caso, corresponde à cor "Verde", escolhida por três pessoas. A amostra é **unimodal**.
    """)

    # Lista das cores favoritas
    cores_favoritas = ['Verde', 'Rosa', 'Vermelho', 'Azul', 'Verde', 'Amarelo', 'Azul', 'Verde', 'Rosa', 'Preto']

    # Contagem das cores favoritas
    contagem_cores = pd.Series(cores_favoritas).value_counts()

    # Criando o gráfico de barras
    fig, ax = plt.subplots()
    ax.bar(contagem_cores.index, contagem_cores.values, color=['#00494f', '#00494f', '#00494f', '#00494f', '#00494f'])

    # Anotando os valores diretamente nas barras
    for i, v in enumerate(contagem_cores.values):
        ax.text(i, v + 0.1, str(v), ha='center', va='bottom', fontsize=12)

    # Título e rótulos dos eixos
    ax.set_title('Distribuição das Cores Favoritas', fontsize=14)
    ax.set_xlabel('Cor', fontsize=12)
    ax.set_ylabel('Frequência', fontsize=12)

    # Exibindo o gráfico no Streamlit
    st.pyplot(fig)

# Botão para mostrar/ocultar o Exemplo 2
if st.button("Exemplo 2: Qual sua idade?"):
    toggle_example2()

# Exibição condicional do Exemplo 2
if st.session_state['show_example2']:
    st.write("""
    **Exemplo 2**: Qual sua idade?
            
    Perguntamos a um grupo de colaboradores suas idades, obtendo a seguinte lista:
                
                {23, 25, 45, 52, 29, 28, 45, 53, 36, 28}

    As idades mais frequentes são 28 e 45 anos. Como existem dois valores mais frequentes, a amostra é **bimodal**.
    """)

    # Idades dos colaboradores
    idades = [23, 25, 45, 52, 29, 28, 45, 53, 36, 28]

    # Contagem das idades
    contagem_idades = pd.Series(idades).value_counts()

    # Criando o gráfico de barras
    fig, ax = plt.subplots()
    ax.bar(contagem_idades.index, contagem_idades.values, color='#00494f')



    # Título e rótulos dos eixos
    ax.set_title('Distribuição das Idades', fontsize=14)
    ax.set_xlabel('Idade', fontsize=12)
    ax.set_ylabel('Frequência', fontsize=12)

    # Exibindo o gráfico no Streamlit
    st.pyplot(fig)

# Botão para mostrar/ocultar o Exemplo 3
if st.button("Exemplo 3: Quantos irmãos você tem?"):
    toggle_example3()

# Exibição condicional do Exemplo 3
if st.session_state['show_example3']:
    st.write("""
    **Exemplo 3**: Quantos irmãos você tem?
            
    Perguntamos a um grupo de colaboradores quantos irmãos eles têm, obtendo a seguinte lista:
                
                {1, 0, 2, 2, 1, 0, 0, 1, 4, 2}

    A moda, nesse caso, corresponde aos valores que aparecem três vezes cada, ou seja, os valores 0, 1 e 2.
    Dizemos que essa é uma amostra **multimodal**.
    """)

    # Lista de irmãos
    irmaos = [1, 0, 2, 2, 1, 0, 0, 1, 4, 2]

    # Contagem dos irmãos
    contagem_irmaos = pd.Series(irmaos).value_counts()

    # Criando o gráfico de barras
    fig, ax = plt.subplots()
    ax.bar(contagem_irmaos.index, contagem_irmaos.values, color='#00494f')

    # Título e rótulos dos eixos
    ax.set_title('Distribuição do Número de Irmãos', fontsize=14)
    ax.set_xlabel('Número de Irmãos', fontsize=12)
    ax.set_ylabel('Frequência', fontsize=12)

    # Exibindo o gráfico no Streamlit
    st.pyplot(fig)
