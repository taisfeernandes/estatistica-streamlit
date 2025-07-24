import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Inicializando o estado da sessão para controlar a exibição dos exemplos
if 'show_example1' not in st.session_state:
    st.session_state['show_example1'] = False
if 'show_example2' not in st.session_state:
    st.session_state['show_example2'] = False

# Funções para alternar a exibição dos exemplos
def toggle_example1():
    st.session_state['show_example1'] = not st.session_state['show_example1']

def toggle_example2():
    st.session_state['show_example2'] = not st.session_state['show_example2']

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

# Título da aplicação
st.title("Distribuição Normal")

# Explicação breve sobre a distribuição normal
st.write("""
    Quando observamos fenômenos naturais ou sociais, frequentemente percebemos um padrão que se repete,
    que consiste num gráfico em forma de sino. Um exemplo disso seria a altura dos indivíduos de uma 
    certa população, cujo gráfico teria uma curva parecida com a curva abaixo:
""")

# Exibir a imagem de uma distribuição normal
st.image("Estatisticas_Inferenciais/gaussiana_altura.png", caption="Exemplo de Distribuição Normal da Altura de uma População", use_column_width=True)

# Continuação da explicação sobre a distribuição normal
st.write("""
    Essa distribuição pode ser vista como uma distribuição normal, e dela podemos concluir que:

    * A maior parte dos indivíduos possui altura próxima da média (ao redor de 1,70 metros).
    * Poucos indivíduos possuem altura menor que 1,40 metros, ou seja, muito menores que a média.
    * Poucos indivíduos possuem altura maior que 2 metros, ou seja, muito maiores que a média.
    * A distribuição é simétrica, e o eixo de simetria se apresenta na altura média da população.

    Chamamos essa distribuição de **Distribuição Normal**.
""")

# Função para criar o gráfico de distribuição com linha de média
def plot_distribution(data, title, xlabel, media):
    plt.figure(figsize=(8, 5))
    sns.histplot(data, bins=30, kde=True, color='blue', stat='density')
    plt.axvline(media, color='red', linestyle='dashed', linewidth=2, label=f'Média: {media}')
    plt.legend()
    plt.title(title, fontsize=14)
    plt.xlabel(xlabel, fontsize=12)
    plt.ylabel('Densidade', fontsize=12)
    st.pyplot(plt)

# Botão para alternar o exemplo 1 (Notas)
st.button("Mostrar  Exemplo 1: Notas em uma prova", on_click=toggle_example1)

if st.session_state['show_example1']:
    # Exemplo 1: Notas em uma prova
    media_nota = 75  # média das notas
    desvio_padrao_nota = 10  # desvio padrão das notas
    turma = 1000  # número de estudantes aumentados
    notas = np.random.normal(media_nota, desvio_padrao_nota, turma)
    
    st.subheader("Exemplo 1: Notas de Exames de uma Turma Fictícia")
    plot_distribution(notas, "Distribuição Normal das Notas", "Nota (%)", media_nota)
    
    st.write("""
        Aqui, as notas de uma turma fictícia seguem uma distribuição normal. A maioria dos estudantes 
        tem notas próximas da média (75%), enquanto poucos tiram notas muito baixas ou muito altas.
    """)

# Botão para alternar o exemplo 2 (Pesos de frutas)
st.button("Mostrar Exemplo 2: Frutas em uma colheita", on_click=toggle_example2)

if st.session_state['show_example2']:
    # Exemplo 2: Peso das maçãs em uma colheita
    media_peso = 150  # média do peso das maçãs (gramas)
    desvio_padrao_peso = 20  # desvio padrão do peso
    colheita = 2000  # número de frutas aumentado para melhorar a simetria
    pesos = np.random.normal(media_peso, desvio_padrao_peso, colheita)
    
    st.subheader("Exemplo 2: Peso de Frutas numa Colheita Fictícia")
    plot_distribution(pesos, "Distribuição Normal do Peso das Frutas", "Peso (gramas)", media_peso)
    
    st.write("""
        Neste exemplo, o peso das frutas colhidas também segue uma distribuição normal. 
        A maioria das frutas pesa em torno de 150 gramas, enquanto poucas são muito leves ou muito pesadas.
    """)
