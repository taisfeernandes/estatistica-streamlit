import streamlit as st

# Funções para alternar a exibição dos exemplos
def toggle_example_curtose_1():
    st.session_state['show_example_curtose_1'] = not st.session_state['show_example_curtose_1']
    
# Inicializando o estado da sessão para controlar a exibição dos exemplos
if 'show_example_curtose_1' not in st.session_state:
    st.session_state['show_example_curtose_1'] = False

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

st.title("O que é a Curtose?")

# Texto sobre a curtose
st.write("""
A curtose é uma medida estatística que descreve a forma da distribuição de dados, especialmente no que diz respeito à concentração de valores nas caudas da distribuição (valores extremos). 
Ela nos ajuda a entender se os dados têm caudas mais pesadas ou mais leves em comparação com uma distribuição normal.

Se a curtose for alta (leptocúrtica), isso significa que há mais valores extremos, ou seja, a distribuição tem caudas mais pesadas. 
Se a curtose for baixa (platicúrtica), a distribuição tem caudas mais leves, com os dados concentrados em torno da média. 
A curtose normal (mesocúrtica) é próxima de zero e corresponde a uma distribuição normal.
""")

st.latex(r'''\text{Curtose} = \frac{\sum_{i=1}^{n} (x_i - \bar{x})^4}{n \cdot \sigma^4}''')
st.latex(r'''\text{onde:}''')
st.latex(r'''\begin{align*} \text{n} & = \text{número de observações} \\ 
\text{x}_i & = \text{cada observação} \\ 
\bar{x} & = \text{média dos dados} \\ 
\sigma & = \text{desvio padrão} \end{align*}''')

if st.button("Exemplo prático"):
    toggle_example_curtose_1()

if st.session_state['show_example_curtose_1']:
    st.write("""
    Considere o seguinte conjunto de dados que representa o número de vendas diárias de uma empresa em um determinado período:
    """)

    st.latex(r'''\text{Vendas diárias} = [5, 7, 8, 10, 10, 12, 25]''')

    st.write("""
    Para calcular a curtose, primeiro precisamos calcular a média e o desvio padrão dos dados.
    """)
    st.latex(r'''\text{Média} = \frac{5 + 7 + 8 + 10 + 10 + 12 + 25}{7} = 10.14''')

    st.latex(r'''\text{Desvio padrão} = \sqrt{\frac{(5-10.14)^2 + (7-10.14)^2 + (8-10.14)^2 + (10-10.14)^2 + (10-10.14)^2 + (12-10.14)^2 + (25-10.14)^2}{7}} = 6.45''')

    st.write("""
    Substituindo esses valores na fórmula da curtose, obtemos:
    """)
    st.latex(r'''\text{Curtose} = \frac{(5-10.14)^4 + (7-10.14)^4 + (8-10.14)^4 + (10-10.14)^4 + (10-10.14)^4 + (12-10.14)^4 + (25-10.14)^4}{7 \cdot 6.45^4} = 2.14''')

    st.write("""
    Neste caso, a curtose é de 2.14, o que indica que a distribuição dos dados é mais leptocúrtica do que uma distribuição normal.
    """)

st.write("""
### Interpretação da Curtose
- **Curtose > 0:** Distribuição leptocúrtica, com caudas mais pesadas e mais valores extremos.
- **Curtose = 0:** Distribuição normal, com caudas semelhantes às de uma distribuição normal.
- **Curtose < 0:** Distribuição platicúrtica, com caudas mais leves e menos valores extremos.
""")
