import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Verifica se os exemplos já estão na sessão
if 'coeficiente_pearson' not in st.session_state:
    st.session_state['coeficiente_pearson'] = False
if 'coeficiente_spearman' not in st.session_state:
    st.session_state['coeficiente_spearman'] = False
if 'coeficiente_kendall' not in st.session_state:
    st.session_state['coeficiente_kendall'] = False

# Funções para alternar a exibição dos exemplos
def pearson():
    st.session_state['coeficiente_pearson'] = not st.session_state['coeficiente_pearson']

def sperman():
    st.session_state['coeficiente_spearman'] = not st.session_state['coeficiente_spearman']

def kendall():
    st.session_state['coeficiente_kendall'] = not st.session_state['coeficiente_kendall']

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
    body {
        color: #00494f;
    }
    h1, h2, h3, h4, h5, h6 {
        color: #00494f;
    }
    </style>
    """, unsafe_allow_html=True)

# Criando um dataset 
np.random.seed(42)
df = pd.DataFrame({
    "Tempo_Uso (meses)": np.random.randint(6, 36, 100),
    "Atraso_Pagamento (dias)": np.random.randint(0, 20, 100),
    "Número_Reclamações": np.random.randint(0, 5, 100),
    "Satisfação_Cliente (1 a 5)": np.random.randint(1, 6, 100),
    "Cancelamento (0=Não, 1=Sim)": np.random.randint(0, 2, 100)
})

# Função para criar heatmap
def plot_heatmap(corr, title):
    fig = px.imshow(corr, text_auto=True, color_continuous_scale='Blues', 
                    title=title, aspect="auto", width=600, height=600)
    fig.update_traces(textfont_size=12)
    st.plotly_chart(fig)

# Título da Aplicação
st.title("Correlação")

# Introdução ao conceito de correlação
st.write("""
Entender os motivos que levam alguns clientes a cancelar um serviço é um desafio comum. Por exemplo, será que atrasos no pagamento ou quanto tempo a pessoa usa o serviço têm alguma relação com o cancelamento?

A **correlação** é uma maneira de ver se duas coisas estão ligadas. Pense nela como um indicador que nos diz se, quando algo muda, a outra coisa também tende a mudar.

A correlação varia de **1 a -1**:
- **1**: Correlação positiva perfeita (ambas aumentam juntas).
- **-1**: Correlação negativa perfeita (uma aumenta enquanto a outra diminui).
- **0**: Sem correlação significativa.
""")

st.image("Estatisticas_Inferenciais/forcadedirecao.png")

# Coeficientes de correlação 
st.subheader("Tipos de Coeficientes de Correlação")

# Botão para mostrar/ocultar o Exemplo 1
if st.button("Coeficiente de Pearson"):
    pearson()

# Exibição condicional do Exemplo 1
if st.session_state['coeficiente_pearson']:
    st.subheader("Coeficiente de Pearson")
    st.write("""
    - **Descrição:** Mede a força e direção de uma relação linear entre duas variáveis numéricas. Ideal para dados que seguem uma distribuição normal e apresentam uma relação linear.
    - **Exemplo de Uso:** Imagine que queremos verificar se o tempo de uso do serviço está relacionado ao cancelamento. Podemos aplicar o coeficiente de Pearson para investigar essa possível relação linear entre as duas variáveis.
    """)

    
    pearson_corr = df.corr(method='pearson')
    plot_heatmap(pearson_corr, "Matriz de Correlação de Pearson")
    
    st.write("""
    **Interpretação**:
    - Se o coeficiente entre o "Tempo de Uso" e "Cancelamento" for próximo de **-1**, indica que quanto mais tempo o cliente usa o serviço, menor a chance de ele cancelar.
    - Se o coeficiente entre "Atraso de Pagamento" e "Cancelamento" for próximo de **1**, pode sugerir que clientes que atrasam mais os pagamentos tendem a cancelar mais.
    """)

# Botão para mostrar/ocultar o Exemplo 2
if st.button("Coeficiente de Spearman"):
    sperman()

# Exibição condicional do Exemplo 2
if st.session_state['coeficiente_spearman']:
    st.subheader("Coeficiente de Spearman")
    st.write("""
    - **Descrição:** Mede a relação monotônica (não necessariamente linear) entre duas variáveis. É útil quando os dados não seguem uma distribuição normal.
    - **Exemplo de Uso:** Suponha que queremos verificar se o atraso no pagamento está relacionado ao cancelamento, mas os dados podem não seguir uma distribuição normal. Nesse caso, o coeficiente de Spearman é uma boa opção, pois mede a correlação monotônica.
    """)

    spearman_corr = df.corr(method='spearman')
    plot_heatmap(spearman_corr, "Matriz de Correlação de Spearman")
    
    st.write("""
    **Interpretação**:
    - Se o coeficiente de Spearman entre "Satisfação do Cliente" e "Cancelamento" for negativo, isso significa que clientes menos satisfeitos tendem a cancelar mais.
    - Se houver uma correlação alta entre "Número de Reclamações" e "Cancelamento", indica que muitos clientes que reclamam acabam cancelando o serviço.
    """)

# Botão para mostrar/ocultar o Exemplo 3
if st.button("Coeficiente de Kendall"):
    kendall()

# Exibição condicional do Exemplo 3
if st.session_state['coeficiente_kendall']:
    st.subheader("Coeficiente de Kendall")
    st.write("""
    - **Descrição:** Avalia a concordância entre as ordens de classificação de duas variáveis. É mais robusto para dados com pequenos conjuntos ou com muitas classificações.
    - **Exemplo de Uso:** Podemos usar o coeficiente de Kendall para entender se a satisfação do cliente, que é uma variável ordinal, está correlacionada com o cancelamento do serviço.
    """)


    kendall_corr = df.corr(method='kendall')
    plot_heatmap(kendall_corr, "Matriz de Correlação de Kendall")
    
    st.write("""
    **Interpretação**:
    - Se o coeficiente de Kendall para "Satisfação do Cliente" e "Cancelamento" for negativo, significa que os clientes com maior satisfação têm menos probabilidade de cancelar.
    - O coeficiente entre "Número de Reclamações" e "Cancelamento" pode indicar se os clientes que fazem mais reclamações são mais propensos a encerrar o serviço.
    """)

# Conclusão
st.write("""
### Considerações Finais
A correlação nos ajuda a identificar padrões e tendências importantes entre os fatores que podem levar ao cancelamento de serviços. Ao entender essas relações, as empresas podem tomar decisões mais estratégicas, focando nos fatores que têm maior impacto sobre o comportamento dos clientes e, assim, melhorar a retenção e satisfação.
""")
