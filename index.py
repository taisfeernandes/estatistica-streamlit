import streamlit as st

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

st.image("Logo_br_2.jpg")
st.header("Introdução")

st.write("""
O projeto proporciona uma exploração de conceitos fundamentais em estatística e análise de dados por meio de uma ferramenta de visualização interativa, o Streamlit. O foco principal foi desenvolver uma compreensão sólida sobre estatística, abrangendo desde conceitos básicos, como médias e desvio padrão, até técnicas mais avançadas, como distribuições de probabilidade.

A aplicação foi desenvolvida com base na manipulação e visualização dinâmica de dados. A ferramenta permitiu criar uma aplicação interativa, onde é possível visualizar e explorar resultados, gráficos e análises de maneira prática e intuitiva.

A estatística é essencial para a análise de dados e tomada de decisões, pois permite uma interpretação precisa e baseada em evidências. A utilização de técnicas estatísticas ajuda a descobrir padrões, tendências e relações entre as variáveis, assegurando que as decisões se baseiem em dados concretos, o que aumenta a clareza dos insights e a confiança nos resultados.
""")

st.subheader("Objetivos Principais:")
st.write("""
- **Facilitar o entendimento de conceitos estatísticos:** Oferecer uma explicação clara e acessível, ajudando a construir uma base sólida de conhecimento.

- **Proporcionar uma experiência interativa:** Permitir que os usuários explorem e visualizem dados de forma dinâmica, promovendo um aprendizado mais prático e envolvente.

- **Apresentar análises e resultados de forma intuitiva:** Utilizar gráficos e visualizações claras para tornar os resultados e análises facilmente compreensíveis, facilitando a interpretação.
""")
st.info("Para explorar as funcionalidades da aplicação, utilize o menu de navegação à esquerda.")

# Rodapé
footer="""<style>
a:link , a:visited{
color: blue;
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: white;
color: black;
text-align: center;
}
</style>
<div class="footer">
<p>Desenvolvido por Johann Daflon, Ralph Neto, Tais Fernandes, Thiago Oliveira, Ângelo Pereira, Ricardo Leopoldo, André Victor Costa</p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)