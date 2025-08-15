import streamlit as st

st.set_page_config(page_title='Portifólio', layout='wide')

st.title('Olá, eu sou o Yuri e este é meu portifólio:')
st.write('Me chamo Yuri Pereira Gonçalves, tenho 16 anos, moro em Lavras MG e atualmente estou em desenvolvimento na área de Análise de Dados e IA.')
st.divider()
st.title('💡 Meus projetos')
st.markdown('')


st.markdown("""
        <style>
        .card-link {
            text-decoration: none !important;
            color: inherit !important;
            outline: none;
        }
        .card-link:hover, .card-link:focus {
            text-decoration: none !important;
            color: inherit !important;
        }
        .card {
            background-color: white;
            padding: 20px;
            border-radius: 15px;
            box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
            height: 200px;
            text-align: left;
            position: relative;
            transition: transform 0.2s;
            display: block;
        }
        .card:hover {
            transform: scale(1.02);
            box-shadow: 2px 2px 15px rgba(0,0,0,0.2);
            cursor: pointer;
        }
        .card-title {
            font-size: 22px;
            font-weight: bold;
            color: #333333;
        }
        .card-desc {
            font-size: 18px;
            color: black;
            margin-bottom: 15px;
        }
        </style>
    """, unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <a href="https://projetos-dashboardmusical.streamlit.app/" target="_blank" class="card-link">
        <div class="card">
            <div class="card-title">📊 Dashboard App Musical</div>
            <div class="card-desc">App com Streamlit e IA para tirar suas dúvidas sobre informações do App musical.</div>
        </div>
    </a>
    """, unsafe_allow_html=True)


with st.sidebar:
    st.header('''Yuri Pereira Gonçalves''')
    
    st.markdown("""
    💼 Análise de Dados                 
    📍 Lavras, MG               
    📧 yuri.pereirag02@email.com             
    [![LinkedIn](https://img.shields.io/badge/-LinkedIn-blue)](https://www.linkedin.com/in/yuri-pereira-analise-dados/)
    [![GitHub](https://img.shields.io/badge/-GitHub-black)](https://github.com/yuripereira02)

    ---
    ### Hard Skills
    
    - <img src="https://upload.wikimedia.org/wikipedia/commons/7/73/Microsoft_Excel_2013-2019_logo.svg" width="20" style="vertical-align:middle;"> Excel
    - 📊 Business Intelligence
    - <img src="https://cdn.simpleicons.org/python" width="20" style="vertical-align:middle;"> Python 
    - <img src="https://cdn.simpleicons.org/postgresql" width="20" style="vertical-align:middle;"> PostgreSQL
    - <img src="https://cdn.simpleicons.org/metabase" width="20" style="vertical-align:middle;"> Metabase
    - 🤖 Machine Learning
    - 🖥️ IA Generativa""",
    unsafe_allow_html=True)