import dash
import dash_core_components as dcc
import dash_html_components as html
import pickle
import pandas as pd
infile = open("files/senti_prediction_NB.pickle",'rb')
data = pickle.load(infile)
infile.close()
#print('im')
x=data[data==2]

#print(x)
y=data[data==1]
z=data[data==0]

app = dash.Dash()

app.layout = html.Div(children=[
    html.H1(children='Welcome to Prodevans Technology'),
    dcc.Graph(id='example',
        figure={
            'data': [
                {'x': [0,1,2],'y ':[y],'type': 'bar', 'name': 'Negative sentiment'},
                {'x': [0,1,2],'y ':[z],'type': 'bar', 'name': 'Positive sentiment'},
                
                {'x': [0,1,2],'y ':[x],'type': 'bar', 'name': 'Neutral sentiment'},
            ],
            'layout': {
                'title': 'Sentiment Analysis for drugs/medicines'
            }
        }
            )
])

if __name__ == "__main__":
    app.run_server(debug=True,host='0.0.0.0')
