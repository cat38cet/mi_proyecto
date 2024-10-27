import pandas as pd
import numpy as np

# Simular la carga de un dataset de ventas
data = {
    'VentaID': np.arange(1, 10001),
    'ProductoID': np.random.choice([101, 102, 103, 104], 10000),
    'ClienteID': np.random.choice([1001, 1002, 1003, 1004], 10000),
    'Fecha': pd.date_range(start='2021-01-01', periods=10000, freq='H'),
    'Cantidad': np.random.randint(1, 5, size=10000),
    'Precio': np.random.uniform(10, 50, size=10000)
}
df = pd.DataFrame(data)

# Calcular el total de ventas
df['Total'] = df['Cantidad'] * df['Precio']


import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

# Inicializar la aplicación Dash
app = dash.Dash(__name__)

# Layout del dashboard
app.layout = html.Div([
    html.H1("Dashboard de Ventas Interactivo"),
    
    # Dropdown para seleccionar producto
    html.Label("Seleccionar Producto:"),
    dcc.Dropdown(
        id='producto-dropdown',
        options=[{'label': str(prod), 'value': prod} for prod in df['ProductoID'].unique()],
        value=df['ProductoID'].unique()[0]
    ),
    
    # Gráfico de ventas por cliente
    dcc.Graph(id='grafico-ventas-cliente'),
    
    # Gráfico de ventas por tiempo
    dcc.Graph(id='grafico-ventas-tiempo'),
])

# Callback para actualizar el gráfico de ventas por cliente
@app.callback(
    Output('grafico-ventas-cliente', 'figure'),
    Input('producto-dropdown', 'value')
)
def update_grafico_cliente(producto_seleccionado):
    df_filtrado = df[df['ProductoID'] == producto_seleccionado]
    ventas_por_cliente = df_filtrado.groupby('ClienteID')['Total'].sum().reset_index()
    fig = px.bar(ventas_por_cliente, x='ClienteID', y='Total', title=f'Ventas por Cliente para Producto {producto_seleccionado}')
    return fig

# Callback para actualizar el gráfico de ventas a lo largo del tiempo
@app.callback(
    Output('grafico-ventas-tiempo', 'figure'),
    Input('producto-dropdown', 'value')
)
def update_grafico_tiempo(producto_seleccionado):
    df_filtrado = df[df['ProductoID'] == producto_seleccionado]
    ventas_tiempo = df_filtrado.groupby('Fecha')['Total'].sum().reset_index()
    fig = px.line(ventas_tiempo, x='Fecha', y='Total', title=f'Tendencia de Ventas en el Tiempo para Producto {producto_seleccionado}')
    return fig

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run_server(debug=True)

