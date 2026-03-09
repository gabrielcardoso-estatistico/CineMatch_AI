# 🎬 CineMatch AI:

O **CineMatch AI** é um sistema de recomendação de filmes que utiliza Processamento de Linguagem Natural (NLP) de última geração para entender a "alma" de um filme. Diferente de recomendadores comuns que apenas buscam palavras iguais, esta IA analisa o contexto semântico de sinopses, diretores e metadados.

---

## 🚀 O Resultado Final

Aqui está uma demonstração do sistema sugerindo filmes similares ao "Avatar" com filtros personalizados de Ação e Aventura:

![Demonstração do CineMatch AI](image_e80159.jpg) 

> **Nota:** Certifique-se de que o arquivo da imagem (`image_e80159.jpg`) esteja na raiz do seu repositório para que ela apareça corretamente.

---

## 🧠 Inteligência Por Trás do Projeto

O motor de recomendação foi construído utilizando uma abordagem de **Filtragem Híbrida** e **Deep Learning**:

### 1. Engenharia de Metadados (Weighted Soup)
Para que a IA priorizasse elementos cruciais, criamos uma "Sopa de Metadados" com pesos diferenciados:
* **Diretor (Peso 5x):** O estilo autoral é o maior preditor de gosto.
* **Keywords e Título (Peso 3x):** Capturam a essência temática e franquias.
* **Gêneros (Peso 2x):** Define a categoria técnica.
* **Sinopse e Elenco (Peso 1x):** Fornece o contexto narrativo.



### 2. Deep Learning com Transformers
Utilizamos o modelo **`all-mpnet-base-v2`** da biblioteca *Sentence-Transformers*. Este modelo mapeia cada filme em um **espaço vetorial de 768 dimensões**, permitindo que o sistema entenda que "exploração espacial" e "viagem intergalática" são conceitos quase idênticos matematicamente.

### 3. Similaridade do Cosseno
A recomendação é feita calculando a distância angular entre os vetores de alta fidelidade. Scores acima de **80%** indicam uma compatibilidade semântica extremamente alta entre as obras.



---

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3.10+
* **IA/NLP:** Sentence-Transformers (BERT/MPNet)
* **Processamento de Dados:** Pandas, NumPy, Scikit-learn
* **Interface:** Streamlit
* **API Externa:** The Movie Database (TMDB) para posters em tempo real

---

## 📂 Como Executar

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/gabrielcardoso-estatistico/CineMatch-AI.git](https://github.com/gabrielcardoso-estatistico/CineMatch-AI.git)
    ```

2.  **Instale as dependências:**
    ```bash
    pip install streamlit pandas sentence-transformers scikit-learn requests
    ```

3.  **Adicione sua API Key:**
    No arquivo `app.py`, insira sua chave do TMDB na variável da função `fetch_poster`.

4.  **Execute o App:**
    ```bash
    streamlit run app.py
    ```

---

## 📊 Dataset
Os dados utilizados foram extraídos do dataset **TMDB 5000 Movies**, contendo informações detalhadas de orçamento, elenco, sinopses e palavras-chave de mais de 4.800 produções cinematográficas.

---

**Desenvolvido por Gabriel Cardoso 🚀** *Conectando IA e Cinema para uma experiência de descoberta inteligente.*
