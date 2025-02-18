import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Carregar os dados
@st.cache
def load_data():
    # Substitua 'seu_arquivo.csv' pelo caminho real do arquivo CSV
    return pd.read_csv('dataset/train.csv')

# Carregar o arquivo
df = load_data()

# Título do dashboard
st.title('Dashboard Titanic')

# Exibir as primeiras linhas do DataFrame
st.subheader('Primeiras linhas do dataset')
st.write(df.head())

# Exibir informações gerais sobre o dataset
st.subheader('Informações do dataset')
st.write(df.describe())

# Gráfico de distribuição de sobreviventes
st.subheader('Distribuição de sobreviventes')
sns.countplot(data=df, x='Survived')
st.pyplot()

# Gráfico de sobreviventes por classe de passageiro (Pclass)
st.subheader('Sobreviventes por Classe de Passageiro')
sns.countplot(data=df, x='Pclass', hue='Survived')
st.pyplot()

# Gráfico de sobreviventes por sexo
st.subheader('Sobreviventes por Sexo')
sns.countplot(data=df, x='Sex', hue='Survived')
st.pyplot()

# Gráfico de idade
st.subheader('Distribuição de Idades')
sns.histplot(df['Age'].dropna(), kde=True)
st.pyplot()

# Filtro interativo
st.sidebar.subheader('Filtros')
sexo_filtro = st.sidebar.selectbox('Escolha o sexo:', ['All', 'male', 'female'])
classe_filtro = st.sidebar.selectbox('Escolha a classe de passageiro (Pclass):', [1, 2, 3, 'All'])

# Aplicando filtros
if sexo_filtro != 'All':
    df = df[df['Sex'] == sexo_filtro]
if classe_filtro != 'All':
    df = df[df['Pclass'] == classe_filtro]

# Exibindo os dados filtrados
st.subheader('Dados Filtrados')
st.write(df)
