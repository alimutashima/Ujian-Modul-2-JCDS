import plotly
import plotly.graph_objects  as go
import plotly.express as px
from data import data_clean
import json

def dist1():
    df = data_clean()
    df_group= df['horsepower'].value_counts()
    
    fig = go.Figure([go.Bar(x=df['mpg'], y=df_group)])
    fig.show()

    fig_json = json.dumps(fig , cls=plotly.utils.PlotlyJSONEncoder)
    return fig_json
    # fig.show()

def dist1():
    df= data_clean()
    
    fig = go.Figure([go.Bar(x=df['horsepower'], y=df_group)])
    fig.show()
    
    fig_json = json.dumps(fig , cls=plotly.utils.PlotlyJSONEncoder)
    return fig_json
