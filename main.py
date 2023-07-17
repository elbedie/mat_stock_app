"""
Stock History App

Este aplicativo permite visualizar o histórico de ações de uma determinada empresa.
"""

import streamlit as st
import yfinance as yf
import plotly.graph_objects as go


# Titulo do app
st.title('Stock History App')

st.sidebar.title('Selecione o stock')
ticker_symbol = st.sidebar.text_input('stock', 'AAPL', max_chars=10)

# baixando dados do yahoo
data = yf.download(ticker_symbol, start = '2020-01-01', end = '2023-06-26')

# exibir os dados
st.subheader('Histórico')
st.dataframe(data)

# Exibir o arquivo
fig = go.Figure()
fig.add_trace(go.Scatter(x = data.index, y = data['Close'], name ='Fechamento'))
fig.update_layout(title = f"{ticker_symbol}", xaxis_title = 'Data', yaxis_title = 'Preço')

# Exibir o gráfico
st.plotly_chart(fig)

#Exibir o gráfico de volume
fig_volume = go.Figure()
fig_volume.add_trace(go.Scatter(x = data.index, y = data['Volume'], name = 'Volume'))
fig_volume.update_layout(title = f"{ticker_symbol}", xaxis_title='Data', yaxis_title='Volume')
st.plotly_chart(fig_volume)