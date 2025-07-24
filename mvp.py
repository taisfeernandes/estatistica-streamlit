import streamlit as st
import base64

@st.cache_data()
def get_base64_of_bin_file(png_file):
    with open(png_file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

def build_markup_for_logo(
    png_file,
    background_position="50% 5%",
    margin_top="", 
    image_width="60%",
    image_height="",
):
    binary_string = get_base64_of_bin_file(png_file)
    return """
            <style>
                [data-testid="stSidebar"] {
                    background-image: url("data:image/png;base64,%s");
                    background-repeat: no-repeat;
                    background-position: %s;
                    margin-top: %s;
                    background-size: %s %s;
                }
            </style>
            """ % (
        binary_string,
        background_position,
        margin_top,
        image_width,
        image_height,
    )


def add_logo(png_file):
    logo_markup = build_markup_for_logo(png_file)
    st.markdown(
        logo_markup,
        unsafe_allow_html=True,
    )

add_logo("Logo_GH.png")


index = st.Page("index.py", title="Introdução", icon=":material/home:", default=True)

#Estatísticas Descritivas
##Medidas de Tendência Central
media = st.Page("Estatisticas_Descritivas/media.py", title="O que é média aritmética?", icon=":material/arrow_right:")
mediana = st.Page("Estatisticas_Descritivas/mediana.py", title="O que é mediana?", icon=":material/arrow_right:")
moda = st.Page("Estatisticas_Descritivas/moda.py", title="O que é moda?", icon=":material/arrow_right:")

##Medidas de Dispersão
desvio_padrao = st.Page("Estatisticas_Descritivas/desvio_padrao.py", title="O que é Desvio Padrão?", icon=":material/arrow_right:")
variancia = st.Page("Estatisticas_Descritivas/variancia.py", title="O que é Variância?", icon=":material/arrow_right:")

##Distribuições
distribuicao_normal = st.Page("Estatisticas_Descritivas/distribuicao_normal.py", title="Distribuição Normal", icon=":material/arrow_right:")
distribuicao_t = st.Page("Estatisticas_Descritivas/distribuicao_t.py", title="Distribuição t-Student", icon=":material/arrow_right:")

#Estatísticas Infereciais
##Correlação e Covariância
correlacao = st.Page("Estatisticas_Inferenciais/correlacao.py", title="Correlação", icon=":material/arrow_right:")
covariancia = st.Page("Estatisticas_Inferenciais/covariancia.py", title="Covariância", icon=":material/arrow_right:")

##Medidas de Forma
assimetria = st.Page("Estatisticas_Inferenciais/assimetria.py", title="Assimetria", icon=":material/arrow_right:")
curtose = st.Page("Estatisticas_Inferenciais/curtose.py", title="Curtose", icon=":material/arrow_right:")

#Chat IA
chat = st.Page("chat_ia.py", title="Chat IA", icon=":material/arrow_right:")

#Quiz
quiz = st.Page("quiz.py", title="Quiz", icon=":material/arrow_right:")

pg = st.navigation(
    {
        "home": [index],
        "Medidas de Tendência Central": [media, mediana, moda],
        "Medidas de Dispersão": [desvio_padrao, variancia],
        "Medidas de Forma": [assimetria, curtose],
        "Correlacao e Covariância": [correlacao, covariancia],
        "Distribuições": [distribuicao_normal, distribuicao_t],
        "Chat IA": [chat],
        "Quiz": [quiz]
    }
)

pg.run()