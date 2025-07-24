import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# Inicializando o estado da sessão para controlar a exibição
if 'grafico' not in st.session_state:
    st.session_state['grafico'] = False
if 'formula' not in st.session_state:
    st.session_state['formula'] = False
if 'exemplo' not in st.session_state:
    st.session_state['exemplo'] = False

# Funções para alternar a exibição da fórmula, gráfico e exemplo
def formula():
    st.session_state['formula'] = not st.session_state['formula']

def grafico():
    st.session_state['grafico'] = not st.session_state['grafico']

def exemplo():
    st.session_state['exemplo'] = not st.session_state['exemplo']

# CSS para estilizar os botões
st.markdown("""<style>
.stButton > button {
    background-color: #00494f;
    color: white;
    border-radius: 10px;
    height: 50px;
    width: 200px;
    font-size: 18px;
    font-weight: bold;
}
</style>""", unsafe_allow_html=True)

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



# Título da Página
st.title("Distribuição t-Student")

# Introdução simplificada
st.markdown("""
Imagine que você quer entender algo sobre um grupo pequeno de pessoas, mas tem dados de apenas 12 delas. Quando temos poucos dados, é difícil ter certeza sobre a média desses valores. É aqui que entra a **distribuição t-Student**.

Ela nos ajuda a fazer estimativas melhores e a entender melhor a média, mesmo quando temos poucos dados. Usando essa ferramenta, podemos calcular uma faixa de valores (intervalo de confiança) onde a média real provavelmente está.
""")

# Botão da fórmula do intervalo de confiança
if st.button("Fórmula do Intervalo de Confiança"):
    formula()

# Exibição condicional da fórmula de forma simples
if st.session_state['formula']:
    st.latex(r"""
    IC = \bar{x} \pm t_{\left(\frac{\alpha}{2}, n-1\right)} \cdot \left(\frac{s}{\sqrt{n}}\right)
    """)
    st.markdown("**Onde:**")
    st.latex(r"\bar{x} = \text{média amostral}")
    st.latex(r"t = \text{valor t-Student}")
    st.latex(r"s = \text{desvio padrão}")
    st.latex(r"n = \text{número de dados (tamanho da amostra)}")

# Botão para mostrar/ocultar o Exemplo
if st.button("Exemplo"):
    exemplo()

# Exibição condicional do Exemplo 
if st.session_state['exemplo']:
    st.subheader("Exemplo")
    st.markdown("""
    Vamos supor que você trabalhe em uma empresa de telecomunicações e queira avaliar a satisfação de 12 clientes com o atendimento ao cliente. As notas de satisfação variam de 1 a 5, e os dados coletados foram:

    As notas coletadas foram:
    1. **4**  
    2. **3**  
    3. **5**  
    4. **4**  
    5. **2**  
    6. **3**  
    7. **5**  
    8. **4**  
    9. **3**  
    10. **4**  
    11. **2**  
    12. **4**
    


    **Passos para calcular o intervalo de confiança:**
    1. **Média da amostra**:  
    A média dessas notas é 3,58.
    
    2. **Desvio padrão da amostra**:  
    O desvio padrão (uma medida de variação) é aproximadamente 0,996.

    3. **Nível de confiança**:  
    Usando um nível de confiança de 95%, o valor t-Student é 2,201 para 11 graus de liberdade.

    4. **Intervalo de confiança**:  
    Após calcular, a média da satisfação está entre **2,95** e **4,22**, com 95% de confiança.
    """)

# Botão para mostrar/ocultar o gráfico
if st.button("Visualizar Distribuição t -Student"):
    grafico()

# Exibição condicional do gráfico com explicações simplificadas
if st.session_state['grafico']:
    x = np.linspace(-4, 4, 1000)
    normal = stats.norm.pdf(x, 0, 1)  # Distribuição normal
    t_dist = stats.t.pdf(x, df=11)  # Distribuição t com 11 graus de liberdade (n-1)

    fig, ax = plt.subplots()
    ax.plot(x, normal, label='Distribuição Normal', linestyle='--')
    ax.plot(x, t_dist, label='Distribuição t-Student', color='red')
    ax.fill_between(x, 0, t_dist, alpha=0.2, color='red')

    ax.legend()
    ax.set_title("Comparação: Distribuição Normal vs t-Student")
    st.pyplot(fig)

    st.markdown("""
    A curva t-Student é mais larga e tem caudas mais longas que a curva normal, o que significa mais incerteza com amostras pequenas. Conforme o número de dados aumenta, a t-Student vai se aproximando da distribuição normal.
    """)

# Resumo simplificado
st.subheader("Resumindo")
st.markdown("""
Quando você trabalha com poucos dados, a **distribuição t-Student** ajuda a entender melhor a média e a fazer estimativas mais seguras. Ela cria um intervalo de confiança que mostra a faixa de valores onde a média real provavelmente está. Conforme você coleta mais dados, a incerteza diminui, e os resultados ficam mais confiáveis.
""")
