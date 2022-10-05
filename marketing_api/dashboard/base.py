from dash import Dash, dcc, html
import plotly.express as px
from marketing_api.methods.dash_db import count_mau, count_wau, count_dau
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker
from marketing_api.settings import get_settings


engine = create_engine(get_settings().DB_DSN)
session = sessionmaker(engine)

dash_app = Dash(__name__, requests_pathname_prefix="/dashboard/")

with session() as db_session:
    dau = count_dau(db_session)
    wau = count_wau(db_session)
    mau = count_mau(db_session)


fig_dau = px.bar(x=dau.keys(), y=dau.values(), title="DAU")
fig_wau = px.bar(x=wau.keys(), y=wau.values(), title="WAU")
fig_mau = px.bar(x=mau.keys(), y=mau.values(), title="MAU")


dash_app.layout = html.Div(children=[
    html.H1(
        children='Profcomff app dashboard',
    ),
    dcc.Graph(
        id='graph_dau',
        figure=fig_dau
    ),
    dcc.Graph(
        id='graph_wau',
        figure=fig_wau
    ),
    dcc.Graph(
        id='graph_mau',
        figure=fig_mau
    ),
])
