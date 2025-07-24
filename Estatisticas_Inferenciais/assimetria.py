import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm, skewnorm

# Título e explicação sobre simetria
st.title("O que é assimetria?")
st.write("""
    Antes de explicar o que é assimetria, convém explicar o que é simetria.

    Quando observamos uma borboleta, podemos perceber que ao dividirmos ela ao meio, temos duas partes
    iguais. Essa linha que divide a borboleta em duas partes iguais é chamada de **eixo de simetria**.
""")

# Mostrar a imagem da borboleta com simetria
st.image("simetria_borboleta.webp", caption="Exemplo de simetria numa borboleta")

st.write("""
    Uma imagem assimétrica, portanto, é uma imagem em que não conseguimos visualizar a propriedade 
    de simetria. Assim como a borboleta acima é um exemplo de simetria na natureza, temos como exemplo
    de assimetria o caranguejo-fiddler, cujas garras possuem tamanhos distintos, evocando uma nítida
    assimetria.
""")
st.image("caranguejo-fiddler.jpg", caption="Exemplo de assimetria num caranguejo")

# Inicializando o estado da sessão para controlar a exibição dos gráficos
if 'show_symmetric' not in st.session_state:
    st.session_state['show_symmetric'] = False
if 'show_positive_skew' not in st.session_state:
    st.session_state['show_positive_skew'] = False
if 'show_negative_skew' not in st.session_state:
    st.session_state['show_negative_skew'] = False

# Funções para alternar a exibição dos gráficos
def toggle_symmetric():
    st.session_state['show_symmetric'] = not st.session_state['show_symmetric']
def toggle_positive_skew():
    st.session_state['show_positive_skew'] = not st.session_state['show_positive_skew']
def toggle_negative_skew():
    st.session_state['show_negative_skew'] = not st.session_state['show_negative_skew']

# CSS para estilizar os botões
st.markdown("""
    <style>
    .stButton > button {
        background-color: #00494f;
        color: white;
        border-radius: 10px;
        height: 50px;
        width: 250px;
        font-size: 16px;
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

# Função auxiliar para adicionar linhas de média, mediana e moda no gráfico
def add_lines(ax, mean, median, mode):
    ax.axvline(mean, color='purple', linestyle='--', label='Média')
    ax.axvline(median, color='orange', linestyle='-', label='Mediana')
    ax.axvline(mode, color='green', linestyle=':', label='Moda')
    ax.legend()

# Definindo o x utilizado para plotar os gráficos 
x = np.linspace(-5, 5, 100)

# Título e introdução
st.title("Simetria e Assimetria em Gráficos de Distribuição")

# Seção 1: Gráficos simétricos
st.subheader("1. Gráfico Simétrico")
st.write("""
    Uma distribuição simétrica é aquela em que a parte esquerda do gráfico é uma imagem espelhada da parte direita.
    O exemplo mais clássico é a distribuição normal, também conhecida como curva de sino. Numa distribuição simétrica,
    a média, mediana e moda estão todas no mesmo ponto.
""")
if st.button("Mostrar Gráfico Simétrico"):
    toggle_symmetric()

# Exibir ou ocultar gráfico simétrico
if st.session_state['show_symmetric']:
    # Gerar dados para distribuição normal (simétrica)
    x = np.linspace(-5, 5, 100)
    normal_dist = norm.pdf(x)
    mean_normal = median_normal = mode_normal = 0

    # Criar gráfico para a distribuição simétrica
    fig1, ax1 = plt.subplots(figsize=(8, 5))
    ax1.plot(x, normal_dist, label='Distribuição Normal (Simétrica)', color='blue')
    ax1.set_title("Distribuição Simétrica")
    add_lines(ax1, mean_normal, median_normal, mode_normal)

    st.pyplot(fig1)

# Seção 2: Assimetria Positiva
st.subheader("2. Assimetria Positiva")
st.write("""
    Numa distribuição com **assimetria positiva**, a cauda está alongada para a direita (valores mais elevados). Isso
    significa que os dados são concentrados na parte inferior, com alguns valores muito altos que puxam a média para cima.
    Exemplo: rendimentos em muitas economias, onde a maioria das pessoas ganha salários mais baixos, mas existem
    alguns poucos com rendimentos muito altos.
""")
if st.button("Mostrar Gráfico de Assimetria Positiva"):
    toggle_positive_skew()

# Exibir ou ocultar gráfico de assimetria positiva
if st.session_state['show_positive_skew']:
    # Gerar dados para distribuição assimétrica positiva
    a_positive = 10
    skewed_positive = skewnorm.pdf(x, a=a_positive)
    mean_positive = skewnorm.mean(a=a_positive)
    median_positive = skewnorm.median(a=a_positive)
    mode_positive = x[np.argmax(skewed_positive)]

    # Criar gráfico para assimetria positiva
    fig2, ax2 = plt.subplots(figsize=(8, 5))
    ax2.plot(x, skewed_positive, label='Distribuição Assimétrica Positiva', color='red')
    ax2.set_title("Distribuição com Assimetria Positiva")
    add_lines(ax2, mean_positive, median_positive, mode_positive)

    st.pyplot(fig2)

# Seção 3: Assimetria Negativa
st.subheader("3. Assimetria Negativa")
st.write("""
    Na **assimetria negativa**, a cauda da distribuição está à esquerda, ou seja, os dados são concentrados na parte superior,
    com alguns valores muito baixos que puxam a média para baixo. Um exemplo seria a distribuição de notas em alguns testes,
    onde a maioria das pessoas pode ter notas altas, mas algumas poucas têm notas baixas.
""")
if st.button("Mostrar Gráfico de Assimetria Negativa"):
    toggle_negative_skew()

# Exibir ou ocultar gráfico de assimetria negativa
if st.session_state['show_negative_skew']:
    # Gerar dados para distribuição assimétrica negativa
    a_negative = -10
    skewed_negative = skewnorm.pdf(x, a=a_negative)
    mean_negative = skewnorm.mean(a=a_negative)
    median_negative = skewnorm.median(a=a_negative)
    mode_negative = x[np.argmax(skewed_negative)]

    # Criar gráfico para assimetria negativa
    fig3, ax3 = plt.subplots(figsize=(8, 5))
    ax3.plot(x, skewed_negative, label='Distribuição Assimétrica Negativa', color='green')
    ax3.set_title("Distribuição com Assimetria Negativa")
    add_lines(ax3, mean_negative, median_negative, mode_negative)

    st.pyplot(fig3)
