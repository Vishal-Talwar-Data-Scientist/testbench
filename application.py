from dash import Dash, html, dcc
import dash
import dash_bootstrap_components as dbc
external_stylesheets1=['https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css']


app = Dash(__name__, use_pages=True,suppress_callback_exceptions=False,external_stylesheets=external_stylesheets1,assets_folder="static",assets_url_path="static")
application=app.server

app.layout = html.Div([

	dash.page_container
])

if __name__ == '__main__':
	application.run(debug=True,port='8080')