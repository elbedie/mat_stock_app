"""
Stock History App

Este aplicativo permite visualizar o histórico de ações de duas empresas diferentes.
"""

import streamlit as st
import yfinance as yf
import plotly.graph_objects as go


# Titulo do app
st.title('Stock History App')

st.sidebar.title('Selecione os stocks')
ticker_symbol1 = st.sidebar.text_input('stock 1', 'AAPL', max_chars=10)
ticker_symbol2 = st.sidebar.text_input('stock 2', 'GOOGL', max_chars=10)

# baixando dados do yahoo
data1 = yf.download(ticker_symbol1, start='2020-01-01', end='2023-06-26')
data2 = yf.download(ticker_symbol2, start='2020-01-01', end='2023-06-26')

# exibir os dados
st.subheader('Histórico')
st.dataframe(data1)
st.dataframe(data2)

# Exibir o gráfico de fechamento
fig = go.Figure()
fig.add_trace(go.Scatter(x=data1.index, y=data1['Close'], name=ticker_symbol1 + ' Fechamento'))
fig.add_trace(go.Scatter(x=data2.index, y=data2['Close'], name=ticker_symbol2 + ' Fechamento'))
fig.update_layout(title='Histórico de Fechamento', xaxis_title='Data', yaxis_title='Preço')

# Exibir o gráfico de volume
fig_volume = go.Figure()
fig_volume.add_trace(go.Scatter(x=data1.index, y=data1['Volume'], name=ticker_symbol1 + ' Volume'))
fig_volume.add_trace(go.Scatter(x=data2.index, y=data2['Volume'], name=ticker_symbol2 + ' Volume'))
fig_volume.update_layout(title='Histórico de Volume', xaxis_title='Data', yaxis_title='Volume')

# Exibir os gráficos
st.plotly_chart(fig)
st.plotly_chart(fig_volume)
