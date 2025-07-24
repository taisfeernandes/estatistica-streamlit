import streamlit as st

# Título do chat
st.title("🤖 Sigma AI")

# Informação destacada
st.info("Sigma AI é uma poderosa ferramenta da inteligência Artificial que utiliza conceitos de estatística e matemática para responder suas perguntas e gerar insights. Explore o potêncial da AI clicando no link abaixo.")

# Link para abrir em uma nova aba
st.markdown('<a href="https://chatgpt.com/g/g-ZAUv4kLrx-sigma-ai" target="_blank" style="text-decoration:none;"><button>🌐 Acessar Sigma AI</button></a>', unsafe_allow_html=True)

# Espaços
st.write("\n") 
st.write("\n")
st.write("\n")

# Rodapé
st.markdown("""---
**Desenvolvido por Sigma AI**  
Experimente nossa solução avançada de IA para melhorar sua produtividade!""")
