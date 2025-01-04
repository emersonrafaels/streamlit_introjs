import streamlit as st
import streamlit.components.v1 as components

# HTML, CSS e JS para Intro.js com opções personalizadas
intro_js_code = """
<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/intro.js/minified/introjs.min.css">
    <script src="https://cdn.jsdelivr.net/npm/intro.js/minified/intro.min.js"></script>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        .container {
            width: 100%;
            max-width: 1200px;
            margin: 0 auto;
        }
        .section {
            margin-bottom: 20px;
            padding: 20px;
            border: 1px solid #ddd;
            background-color: #f9f9f9;
        }
        input[type="text"], input[type="number"], input[type="range"], select {
            padding: 10px;
            margin: 10px 0;
            width: 100%;
            max-width: 300px;
        }
        .btn {
            padding: 10px 20px;
            font-size: 16px;
            background-color: #4CAF50;
            color: white;
            border: none;
            cursor: pointer;
        }
        .btn:hover {
            background-color: #45a049;
        }
        .stSidebar {
            border: 2px solid #ddd;
            background-color: #f4f4f4;
        }
    </style>
</head>
<body>
    <div class="container">
        <h2>Interatividade com Streamlit & Intro.js</h2>

        <!-- Botão de Início do Tutorial -->
        <button onclick="startIntro()" class="btn">Iniciar Tutorial</button>

        <!-- Seções com tutoriais -->
        <div class="section" id="section1" data-intro="Aqui está o menu de navegação na barra lateral. Você pode usá-lo para navegar entre as páginas!" data-step="1">
            <h3>Seção 1: Menu de Navegação</h3>
            <p>Esta seção explica o menu de navegação na barra lateral. O menu permite alternar entre diferentes páginas do aplicativo.</p>
        </div>

        <div class="section" id="section2" data-intro="Aqui estão os Inputs do Streamlit! Tente interagir com eles para ver como funcionam." data-step="2">
            <h3>Seção 2: Inputs Interativos</h3>
            <p>Você pode interagir com os inputs abaixo para modificar as configurações.</p>
            <p><strong>Nome:</strong> <input type="text" id="name_input" placeholder="Digite seu nome" data-step="3"></p>
            <p><strong>Idade:</strong> <input type="number" id="age_input" placeholder="Digite sua idade" data-step="4"></p>
            <p><strong>Avaliação:</strong> <input type="range" min="1" max="5" id="rating_input" data-step="5"></p>
        </div>

        <div class="section" id="section3" data-intro="Aqui você pode visualizar os resultados dos seus inputs!" data-step="6">
            <h3>Seção 3: Exibição de Resultados</h3>
            <p>Aqui você verá os resultados das interações realizadas nas seções anteriores.</p>
        </div>

        <div class="section" id="section4" data-intro="Clique para mostrar os resultados!" data-step="7">
            <button id="show_results" class="btn">Mostrar Resumo</button>
        </div>
    </div>

    <script>
        // Definir a função startIntro antes de usá-la no botão
        function startIntro() {
            introJs().setOptions({
                showProgress: true,
                nextLabel: 'Próximo',
                prevLabel: 'Anterior',
                doneLabel: 'Concluir',
                showStepNumbers: true,
                stepNumbersOfLabel: 'de',
                steps: [
                    {
                        title: 'Menu de Navegação',
                        intro: 'Aqui está o menu de navegação na barra lateral. Você pode usá-lo para navegar entre as páginas do aplicativo.',
                        element: document.querySelector('#section1')  // Apontando para o elemento da seção do menu
                    },
                    {
                        title: 'Inputs Interativos',
                        intro: 'Aqui estão os Inputs do Streamlit! Tente interagir com eles para ver como funcionam.',
                        element: document.querySelector('#section2')  // Apontando para a seção de inputs
                    },
                    {
                        title: 'Input de Nome',
                        intro: 'Digite seu nome aqui para interagir com o aplicativo.',
                        element: document.querySelector('#name_input')
                    },
                    {
                        title: 'Input de Idade',
                        intro: 'Escolha sua idade para ver a interatividade.',
                        element: document.querySelector('#age_input')
                    },
                    {
                        title: 'Avaliação',
                        intro: 'Avalie o produto ou serviço com este controle deslizante.',
                        element: document.querySelector('#rating_input')
                    },
                    {
                        title: 'Exibição de Resultados',
                        intro: 'Aqui você verá os resultados das suas interações.',
                        element: document.querySelector('#section3')
                    },
                    {
                        title: 'Mostrar Resumo',
                        intro: 'Clique aqui para ver o resumo das informações inseridas.',
                        element: document.querySelector('#show_results')
                    },
                    {
                        intro: '<img src="https://i.giphy.com/media/ujUdrdpX7Ok5W/giphy.webp" onerror="this.onerror=null;this.src="https://i.giphy.com/ujUdrdpX7Ok5W.gif" alt="">'
                    }
                ]
            }).start();
        }

        document.getElementById('show_results').addEventListener('click', function() {
            alert("Nome: " + document.getElementById('name_input').value + 
                  "Idade: " + document.getElementById('age_input').value + 
                  "valiação: " + document.getElementById('rating_input').value);
        });
    </script>
</body>
</html>
"""

# Streamlit App
st.set_page_config(page_title="Tutorial Interativo", layout="wide")

# Barra lateral com Menu
menu = st.sidebar.selectbox("Escolha uma opção", ["Início", "Sobre", "Tutorial", "Contatos"])

if menu == "Início":
    st.title("Bem-vindo ao App Streamlit + Intro.js!")
    st.write(
        "Este aplicativo demonstra como integrar o **Intro.js** com o Streamlit. Navegue pelo tutorial para aprender mais.")

elif menu == "Sobre":
    st.title("Sobre o App")
    st.write(
        "Este é um aplicativo de exemplo utilizando o framework Streamlit, combinando a simplicidade da criação de apps com a interatividade do **Intro.js**.")

elif menu == "Tutorial":
    st.title("Tutorial Interativo")
    st.write("Clique no botão abaixo para iniciar o tutorial que explica como usar este aplicativo com o **Intro.js**.")
    st.components.v1.html(intro_js_code, height=800, scrolling=True)

elif menu == "Contatos":
    st.title("Entre em Contato")
    st.write("Caso tenha dúvidas ou sugestões, entre em contato conosco!")
    email = st.text_input("Seu e-mail", "")
    mensagem = st.text_area("Sua mensagem", "")
    if st.button("Enviar"):
        st.success("Mensagem enviada com sucesso!")

# Exibição de Inputs Interativos no Streamlit
st.sidebar.header("Configurações Interativas")

# Exemplo de Input Text
name = st.sidebar.text_input("Digite seu nome", "Seu nome aqui")

# Exemplo de Slider
age = st.sidebar.slider("Selecione sua idade", 18, 100, 25)

# Exemplo de Caixa de Seleção
rating = st.sidebar.selectbox("Qual sua avaliação?", [1, 2, 3, 4, 5])

# Exibindo os valores inseridos
st.sidebar.write(f"Nome: {name}")
st.sidebar.write(f"Idade: {age}")
st.sidebar.write(f"Avaliação: {rating}")

# Inserir botões de ação no Streamlit
if st.sidebar.button("Mostrar Resumo"):
    st.write(f"Nome: {name}")
    st.write(f"Idade: {age}")
    st.write(f"Avaliação: {rating}")
