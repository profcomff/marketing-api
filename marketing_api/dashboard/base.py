from dash import Dash, dcc, html
import plotly.express as px
from marketing_api.methods.dash_db import graph_dau, graph_wau, graph_mau
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker
from marketing_api.settings import get_settings


engine = create_engine(get_settings().DB_DSN)
session = sessionmaker(engine)

dash_app = Dash(__name__, requests_pathname_prefix="/dashboard/")

with session() as db_session:
    dau = graph_dau(db_session)
    wau = graph_wau(db_session)
    mau = graph_mau(db_session)


dash_app.layout = html.Div(children=[
    html.H1(
        children='Profcomff app dashboard',
    ),
    dau,
    wau,
    mau,
])
