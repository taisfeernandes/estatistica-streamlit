import streamlit as st

# Funções para alternar a exibição dos exemplos
def toggle_example_variancia_1():
    st.session_state['show_example_variancia_1'] = not st.session_state['show_example_variancia_1']
    
# Inicializando o estado da sessão para controlar a exibição dos exemplos
if 'show_example_variancia_1' not in st.session_state:
    st.session_state['show_example_variancia_1'] = False

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

st.title("O que é a Variância?")

st.write("""
Suponha que você precise avaliar o desempenho dos funcionários de uma empresa. Cada colaborador tem uma produtividade diferente, e para entender o quão dispersos esses desempenhos estão em relação à média, usamos a variância.

A variância é uma medida importante que indica o quão longe, em média, os desempenhos individuais estão da média geral da equipe. Em outras palavras, ela mostra o quanto os valores se afastam do centro.
""")
st.latex(r'''\text{Variância} = \frac{\sum_{i=1}^{n} (x_i - \bar{x})^2}{n}''')
st.write("""
Quando a variância é alta, significa que os desempenhos estão bastante espalhados, ou seja, há muita variação entre os funcionários.  
Se a variância for baixa, os desempenhos estão mais próximos uns dos outros, indicando maior uniformidade.

Com a variância, é possível entender melhor a dispersão dos dados, o que ajuda a identificar se os resultados da equipe são consistentes ou muito variados.
""")

if st.button("Exemplo prático"):
    toggle_example_variancia_1()

if st.session_state['show_example_variancia_1']:
    st.write("""
    Considere as seguintes notas de desempenho de uma equipe:
    Considere as seguintes avaliações de desempenho (em uma escala de 0 a 100) de 6 funcionários de uma empresa:
    """)
    st.latex(r'''70, 75, 80, 85, 90, 95''')
    st.write("""
    O primeiro passo é calcular a média dessas notas:
    """)
    st.latex(r'''\bar{x} = \frac{70 + 75 + 80 + 85 + 90 + 95}{6} = 82.5''')
    st.write("""
    Agora, vamos calcular a variância:
    """)
    st.latex(r'''\text{Variância} = \frac{(70-82.5)^2 + (75-82.5)^2 + (80-82.5)^2 + (85-82.5)^2 + (90-82.5)^2 + (95-82.5)^2}{6}''')
    st.latex(r'''\text{Variância} = \frac{12.5^2 + 7.5^2 + 2.5^2 + 2.5^2 + 7.5^2 + 12.5^2}{6}''')
    st.latex(r'''\text{Variância} = \frac{156.25 + 56.25 + 6.25 + 6.25 + 56.25 + 156.25}{6} = \frac{437.5}{6} = 72.92''')
    st.write("""
    A variância aqui é aproximadamente 72.92, o que indica que as avaliações estão razoavelmente espalhadas em torno da média.

    Neste exemplo, como a variância é moderada, ela revela uma certa variação entre as avaliações, com alguns funcionários se saindo melhor ou pior do que a média de 82.5.
    """)