import base64
import datetime
import io


from DemandSensing.PredictiveModels.LinearModels.Regression import Linear_Regression_gradient_descent
from DemandSensing.DataPrep.FeatureExtraction.featext import FeatureExtration as fx
from DemandSensing.ModelEvaluation.evaluation import Evaluation_param as ep
from DemandSensing.DataIngestion.readCSV import read_file as rf

import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
import dash_table

import pandas as pd
from pandas import DataFrame as df


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[

    html.H1(
        children='Demand Sensing',
        style={
            'textAlign':'center'
        }
    ),

    html.H4(
        'Demand Sensing Tool',
        style={
            'textAlign':'center'
        }
            
        #}
    ),

     html.H5(
        'Select The Training Algorithm',
     ),
    
    dcc.Dropdown(
        id='my-dropdown-algo',
        options=[
        {'label': 'Linear Regression', 'value': 'LR'},
        {'label': 'Suppport Vector Machines', 'value': 'SVM'},
        {'label': 'Neural Networks', 'value': 'NN'}
    ],
        value='LR',
        style={
            'width': '40%',
            'textAlign': 'center',
            'margin': '10px'
        },
    ),

     html.H5(
        'Select the normalisation technique',
     ),
    
    dcc.Dropdown(
        id='my-dropdown-norm',
        options=[
        {'label': 'Standard Normalisation ', 'value': 'SN'},
        {'label': 'Min Max Norm', 'value': 'MMN'},
        {'label': 'None', 'value': 'N'}
    ],
        #value='MMN',
        style={
            'width': '40%',
            'textAlign': 'center',
            'margin': '10px'
        },
    ),
    
    
     html.H5(
         'Upload the CSV File ',
     ),

    dcc.Upload(
        id='upload-data',
        children=html.Div([
            'Drag and Drop or ',
            html.A('Select File')
        ]),
        style={
            'width': '15%',
            'height': '30px',
            'lineHeight': '30px',
            'borderWidth': '2px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px'
        },
        # Allow multiple files to be uploaded
        multiple=True
    ),

    html.Button('RUN', id='button',
    style={
            'width': '40%',
            'textAlign': 'center',
            'margin': '10px'
        },
    ),
    
    html.H5(id='output-data-upload')
])





@app.callback(Output('output-data-upload', 'children'),
              [Input('button','n_clicks')],
              [State('upload-data', 'contents'),
               State('upload-data', 'filename'),
               State('my-dropdown-algo', 'value'),
               State('my-dropdown-norm', 'value'),]
              )

def fiii(clicks,content,filename,algo,norm):


    if clicks != None and filename != None:
        try:
            stock_market=pd.read_csv(str(filename[0]))
        except:
            return html.H5("The File is not a CSV Need a CSV file to be uplpaded")

        train_data= df(stock_market,columns=[ 'Interest_Rate' ,'Unemployment_Rate' ,'Stock_Index_Price' ])
        
        X = train_data[['Interest_Rate','Unemployment_Rate']]
        #X = train_data[['Interest_Rate']]
        Y = train_data['Stock_Index_Price'] 
        if algo=='LR':
            reg_obj=Linear_Regression_gradient_descent(X,Y,learning_rate=0.03,epochs=1000,logs=True)
            ret=reg_obj.run_grad()
            eval_param=ep(reg_obj)
            if ret==1:
                return html.Div([
                    html.H5("The Regression was Successful"),
                    html.Div("The parameters for the model is "+str(reg_obj.incpt)+" "+str(reg_obj.cord)),
                    html.Div("The Evaluation parameters are "),
                    html.Div("R Squared value is "+str(eval_param.R_squared())),
                    html.Div("Standard Error value is "+str(eval_param.calculate_stder()))
                ])
            
            
        else:
            return html.H5("Other Methods Not Yet implemented")
        
        '''
        print "the button is clicked "
        return html.Div("the button has been clicked "+str(clicks)+" times and the value for the algo is "+str(algo)+" and normalisation is "+str(norm)+ " and the file name selected is "+str(filename[0]))
    elif clicks != None and filename == None:
        print "file not uploaded "
        return html.H5("File Not selected")
        '''
    '''
    print "the button has been clicked ",str(clicks)," times"
    return html.Div("the button has been clicked "+str(clicks)+" times and the value for the algo is "+str(algo)+" and normalisation is "+str(norm))
    if content is not None:
        print "inside the function call"
        print "the contents are", content
        print "the filename are", filename
        print "the last modified are", clicks
    
        return html.Div(
            html.H5(
                'The file uploaded is '+filename[0]
            )
            )
    '''


'''
def parse_contents(contents, filename, date):
    content_type, content_string = contents.split(',')

    decoded = base64.b64decode(content_string)
    try:
        if 'csv' in filename:
            # Assume that the user uploaded a CSV file
            df = pd.read_csv(
                io.StringIO(decoded.decode('utf-8')))
        elif 'xls' in filename:
            # Assume that the user uploaded an excel file
            df = pd.read_excel(io.BytesIO(decoded))
            
    except Exception as e:
        print(e)
        return html.Div([
            'There was an error processing this file.'
        ])

    return html.Div([
        html.H5(filename),
        html.H6(datetime.datetime.fromtimestamp(date)),

        dash_table.DataTable(
            data=df.to_dict('rows'),
            columns=[{'name': i, 'id': i} for i in df.columns]
        ),

        html.Hr(),  # horizontal line

        # For debugging, display the raw contents provided by the web browser
        html.Div('Raw Content'),
        html.Pre(contents[0:200] + '...', style={
            'whiteSpace': 'pre-wrap',
            'wordBreak': 'break-all'
        })
    ])


@app.callback(Output('output-data-upload', 'children'),
              [Input('upload-data', 'contents')],
              [State('upload-data', 'filename'),
               State('upload-data', 'last_modified')])



def update_output(list_of_contents, list_of_names, list_of_dates):
    if list_of_contents is not None:
        children = [
            parse_contents(c, n, d) for c, n, d in
            zip(list_of_contents, list_of_names, list_of_dates)]
        return children
'''


if __name__ == '__main__':
    app.run_server(debug=True)
