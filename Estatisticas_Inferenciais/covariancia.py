import streamlit as st
import pandas as pd

# Funções para alternar a exibição dos exemplos
def toggle_example_cov_1():
    st.session_state['show_example_cov_1'] = not st.session_state['show_example_cov_1']
    
# Inicializando o estado da sessão para controlar a exibição dos exemplos
if 'show_example_cov_1' not in st.session_state:
    st.session_state['show_example_cov_1'] = False

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

st.title("Covariância")
# Texto sobre a covariancia
st.write("""
A covariância é uma medida estatística que mostra como duas variáveis mudam em conjunto. Quando uma variável se desvia de sua média, a covariância nos ajuda a entender se outra variável tende a se desviar de sua média de maneira semelhante ou de forma oposta.

Se a covariância entre duas variáveis for positiva, significa que, geralmente, quando uma variável aumenta, a outra também aumenta.  
Se a covariância for negativa, quando uma variável aumenta, a outra tende a diminuir.  
E, se a covariância for próxima de zero, isso indica que não há uma relação linear clara entre as variáveis.
""")


st.write("""Fórmula da Covariância:""")
st.latex(r'''\text{Covariância}(X, Y) = \frac{\sum_{i=1}^{n} (X_i - \bar{X})(Y_i - \bar{Y})}{n}''')

if st.button("Exemplo prático"):
    toggle_example_cov_1()

if st.session_state['show_example_cov_1']:
    st.write("""
    Considere que você está avaliando a produtividade de 5 funcionários (Produtividade) e as horas que eles dedicam ao trabalho semanalmente (Horas):
    """)
    st.latex(r'''\text{Produtividade} = [60, 65, 70, 80, 85]''')
    st.latex(r'''\text{Horas} = [35, 40, 45, 50, 55]''')


    st.write("""
    Para calcular a covariância entre essas duas variáveis, primeiro precisamos calcular a média de cada uma delas:
    """)
    st.latex(r'''\text{Média Produtividade} = \bar{X} = \frac{60 + 65 + 70 + 80 + 85}{5} = 72''')
    st.latex(r'''\text{Média Horas} = \bar{Y} = \frac{35 + 40 + 45 + 50 + 55}{5} = 45''')

    st.write("""
    Agora, vamos calcular a covariância:
    """)
    st.latex(r'''\text{Covariância}(X, Y) = \frac{(60-72)(35-45) + (65-72)(40-45) + (70-72)(45-45) + (80-72)(50-45) + (85-72)(55-45)}{5}''')
    st.latex(r'''\text{Covariância}(X, Y) = \frac{-12*-10 + -7*-5 + -2*0 + 8*5 + 13*10}{5}''')
    st.latex(r'''\text{Covariância}(X, Y) = \frac{120 + 35 + 0 + 40 + 130}{5} = \frac{325}{5} = 65''')

    st.write("""A covariância neste exemplo é **65**, indicando que, conforme as horas de trabalho aumentam, a produtividade tende a aumentar também. 
    Como a covariância é positiva, podemos concluir que há uma relação direta entre essas duas variáveis.
    """)