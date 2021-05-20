import dash
import dash_daq as daq
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.offline as pyo
import plotly.graph_objs as go
import matplotlib.pyplot as plt
import pandas as pd
import base64

external_stylesheets = [
    # Bootstrap
    "https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css"]

app = dash.Dash()

df1 = pd.read_csv('df1.csv')
dfi1 = pd.read_csv('dfi1.csv')
dfys = pd.read_csv('dfys.csv')
corri1 = pd.read_csv('corri1.csv')
a = [1.0, 0.47, 0.43, 0.36], [0.47, 1.0, 0.91, 0.8], [0.43, 0.91, 1.0, 0.93], [0.36, 0.8, 0.93, 1.0]
pdfi1 = pd.read_csv('pdfi1.csv')  #PCA DF

dfi25 = pd.read_csv('dfi25.csv')
corri25 = pd.read_csv('corri25.csv')
pdfi25 = pd.read_csv('pdfi25.csv')
ats = pd.read_csv('ats.csv')
std = pd.read_csv('std.csv')

evr1 = pd.read_csv('evr1.csv')  #Total Variance explained
evr25 = pd.read_csv('evr25.csv')
sto1 = pd.read_csv('sto1.csv')
sto5 = pd.read_csv('sto5.csv')
sto10 = pd.read_csv('sto10.csv')
sto30 = pd.read_csv('sto30.csv')
# image_dfi1cf = 'dfi1-DGS1-CF.JPG'
image_dfi1cf = base64.b64encode(open('dfi1-DGS1-CF.JPG', 'rb').read())
image_dfi1fit = base64.b64encode(open('dfi1-DGS1-Fit.JPG', 'rb').read())
image_dfi5cf = base64.b64encode(open('dfi1-DGS5-CF.JPG', 'rb').read())
image_dfi5fit = base64.b64encode(open('dfi1-DGS5-Fit.JPG', 'rb').read())

#global variables
# graphdDict = {"1 Day increment":"1 Day increment", "25 Day increment":"25 Day increment"}
# indexDict = {"1 Day increment":0, "25 Day increment":1}
graphdDict = {"DGS1":"DGS1", "DGS5":"DGS5", "DGS10":"DGS10", "DGS30":"DGS30", "ALL":"ALL"}
indexDict = {"DGS1":0, "DGS5":1, "DGS10":2, "DGS30":3, "ALL":4}
names = list(graphdDict.keys())

app.layout = html.Div([
	html.H1(("Analysis and Simulation of Interest Rates"), style={'backgroundColor': 'grey', 'font-size': '100px'}
		),
	html.Div([
		html.H2(('Key Points on Treasury Yields:-'), style={'backgroundColor': 'matt', 'font-size': '40px'}
		),
		html.Br([]),
		dcc.Markdown('''
			1. The Treasury yield is the interest rate that the U.S. government pays to borrow money for different lengths of time.
			2. Each of the Treasury securities (T-bonds, T-bills, and T-notes) has a different yield; longer-term Treasury securities usually have a higher yield than shorter-term Treasury securities.
			3. Treasury yields reflect how investors feel about the economy; the higher the yields on long-term instruments, the more optimistic their outlook.
			'''),
		html.P(
			'Treasury Yield = [C + ((FV - PP) / T)] ÷ [(FV + PP)/2]'
			),
		html.P(
			'where C= coupon rate, FV = face value, PP = purchase price'			
			),
		html.P(
			'T = time to maturity'
			)
		], style={'padding-left':'2%', 'padding-bottom':'0px', 'font-size': '25px'}
		),
	html.Div([
		html.H2(('Intro:-'), style={'backgroundColor': 'matt', 'font-size': '40px'}
		),
		html.P(
			'To analyze the Interest Rate, I chose the following bonds and selected the 1-year time period:-'
			),
		html.Br([]),
		dcc.Markdown('''
			1. 1-Year Treasury Constant Maturity Rate (DGS1)
			2. 5-Year Treasury Constant Maturity Rate (DGS5)
			3. 10-Year Treasury Constant Maturity Rate (DGS10)
			4. 30-Year Treasury Constant Maturity Rate (DGS30)
			''')
		], style={'padding-left':'2%', 'padding-bottom':'0px', 'font-size': '25px'}
		),
	html.Div([
		html.H2(
			'Yield% Graph'
			)], style={'font-size': '30px', 'padding-left':'2%', 'padding-bottom':'0px', 'font-size': '40px'}
		),
	dcc.Graph(
        id='df1',
    ),
    html.Div([
		html.H2(
			'Increment Graph'
			)], style={'font-size': '30px', 'padding-left':'2%', 'padding-bottom':'0px', 'padding-top':'0px', 'font-size': '40px'}
		),
    html.Div(
		dcc.Dropdown(id="increment_graph",
			options=[{'label': i, 'value': i} for i in names],
			value=names[0],
			# multi=True,
			placeholder='Select the detector'),
			style={'width':'70%', 'display':'inline-block', 'padding-left':'2%'}
		),
    html.Div([
		dcc.Graph(
        id='dfi1',
        # figure=Detector1
    			),
		dcc.Graph(
        id='dfi25',
        # figure=Detector1
    			)], style={'width': '100%', 'float': 'right', 'display': 'inline-block', 'padding-left':'2%'}
    	),
    html.Div([
		html.H2(
			'Box Plots'
			)], style={'font-size': '30px', 'padding-left':'2%', 'padding-bottom':'0px', 'padding-top':'0px', 'font-size': '40px'}
		),
    html.Div(
		dcc.Dropdown(id="increment_boxplot_graph",
			options=[{'label': i, 'value': i} for i in names],
			value=names[0],
			# multi=True,
			placeholder='Select the detector'),
			style={'width':'70%', 'display':'inline-block', 'padding-left':'2%'}
		),    
    html.Div([
		dcc.Graph(
        id='boxi1',
        # figure=Detector1
    			),
		dcc.Graph(
        id='boxi25',
        # figure=Detector1
    			)], style={'width': '100%', 'float': 'right', 'display': 'inline-block', 'padding-left':'2%'}
    	),
    # html.Img(id="dfi1-DGS1-CF", src='data:image/png;base64,{}'.format(encoded_image.decode()))
  #   html.Div([
		# html.P(
		# 	'Distribution fit for 1-year bond'
		# 	)], style={'font-size': '30px', 'padding-left':'2%', 'padding-bottom':'0px', 'padding-top':'0px'}
		# ),
    # html.Div([
    # 	html.Img(id="dfi1-DGS1-CF",
    # 	),
    # 	html.Img(id="dfi1-DGS1-Fit",
    # 	)], style={'width': '90%', 'float': 'right', 'display': 'inline-block', 'padding-left':'2%'}
    # 	),

  #   html.Div([
		# html.P(
		# 	'Distribution fit for 5-year bond'
		# 	)], style={'font-size': '30px', 'padding-left':'2%', 'padding-bottom':'0px', 'padding-top':'0px'}
		# ),
  #   html.Div([
  #   	html.Img(id="dfi1-DGS5-CF",
  #   	),
  #   	html.Img(id="dfi1-DGS5-Fit",
  #   	)], style={'width': '90%', 'float': 'right', 'display': 'inline-block', 'padding-left':'2%'}
  #   	),
  #   html.Br([]),
    html.Div([
		html.H2(
			'Average Term Structure'
			)], style={'font-size': '30px', 'padding-left':'2%', 'padding-bottom':'0px', 'padding-top':'0px', 'font-size': '40px'}
		),
  #   html.Div(
		# dcc.Dropdown(id="average_term_structure",
		# 	options=[
		# 		        {'label': 'Mean', 'value': 'Mean'},
		# 		        {'label': 'Standard Deviatione', 'value': 'Standard Deviatione'},
		# 		        {'label': 'Both', 'value': 'Both'}
		# 		    ],
		# 	value='Both',
		# 	# multi=True,
		# 	placeholder='Select the detector'),
		# 	style={'width':'70%', 'display':'inline-block', 'padding-left':'2%'}
		# ),
    dcc.Graph(
        id='ats',
        # figure = go.Figure(data=[go.Scatter(x=ats["index"], y=ats["Mean"], name="Mean",
        #             line_shape='linear'), go.Scatter(x=ats["index"], y=ats["Std."], name="Standard Deviation",
        #             line_shape='linear')])
        figure = {'data':[go.Scatter(x=ats["index"], y=ats["Mean"], name="Mean", line_shape='linear'),
        						 go.Scatter(x=ats["index"], y=ats["Std."], name="Standard Deviation", line_shape='linear')],
				           'layout':{'title':'Average Term Structure',
					                'xaxis':{
					                    'title':'Timeperiod'
					                },
					                'yaxis':{
					                     'title':'Yield,%'}
                 }}
        ),
    html.Div([
		html.H2(
			'Relation Between Standard Deviation'
			)], style={'font-size': '30px', 'padding-left':'2%', 'padding-bottom':'0px', 'padding-top':'0px', 'font-size': '40px'}
		),
    dcc.Graph(
        id='std',
        # figure = go.Figure(data=[go.Scatter(x=std["index"], y=std["Std_1inc"], name="Standard Deviation-1 Day Increment",
        #             line_shape='linear'), go.Scatter(x=std["index"], y=std["Std_25inc"], name="Standard Deviation-25 Day Increment",
        #             line_shape='linear')])
        figure = {'data':[go.Scatter(x=std["index"], y=std["Std_1inc"], name="Standard Deviation-1 Day Increment", line_shape='linear'),
                          go.Scatter(x=std["index"], y=std["Std_25inc"], name="Standard Deviation-25 Day Increment", line_shape='linear')],
				           'layout':{'title':'Standard Deviation Plot',
					                'xaxis':{
					                    'title':'Timeperiod'
					                },
					                'yaxis':{
					                     'title':'Yield,%'}
                 }}
    ),
  #   html.Div([
		# html.P(
		# 	'Correlation Matrix'
		# 	)], style={'font-size': '30px', 'padding-left':'2%', 'padding-bottom':'0px', 'padding-top':'0px'}
		# ),
  #   html.Div([
		# dcc.Graph(
  #       id='corri1',
  #       # figure=Detector1
  #   			),
		# dcc.Graph(
  #       id='corri25',
  #       figure = {'data':[px.imshow(a,
  #               labels=dict(x="Day of Week", y="Time of Day", color="Productivity"),
  #               x=['Monday', 'Tuesday', 'Wednesday', 'Thursday'],
  #               y=['Monday', 'Tuesday', 'Wednesday', 'Thursday']
  #              )],
		# 		           'layout':{'title':'Standard Deviation Plot',
		# 			                'xaxis':{
		# 			                    'title':'Timeperiod'
		# 			                },
		# 			                'yaxis':{
		# 			                     'title':'Yield,%'}
  #                }}
  #   			)], style={'width': '100%', 'float': 'right', 'display': 'inline-block', 'padding-left':'2%'}
  #   	),
  #   html.Div([
		# html.P(
		# 	'Principal Component Analys'
		# 	)], style={'font-size': '30px', 'padding-left':'2%', 'padding-bottom':'0px', 'padding-top':'0px'}
		# ),
  #   html.Div([
		# dcc.Graph(
  #       id='pcai1',
  #       figure = {'data':[px.scatter_3d(pdfi1, x='PCA1', y='PCA2', z='PCA1', color=range(252))],
		# 		           'layout':{'title':'Standard Deviation Plot',
		# 			                'xaxis':{
		# 			                    'title':'Timeperiod'
		# 			                },
		# 			                'yaxis':{
		# 			                     'title':'Yield,%'}
  #                }}
  #   			),
		# dcc.Graph(
  #       id='evr1',
  #       figure = {'data':[go.Scatter(x=evr1["index"], y=evr1["EVR"], name="Standard Deviation-1 Day Increment", line_shape='linear')],
		# 		           'layout':{'title':'Standard Deviation Plot',
		# 			                'xaxis':{
		# 			                    'title':'Timeperiod'
		# 			                },
		# 			                'yaxis':{
		# 			                     'title':'Yield,%'}
  #                }}
  #   			)], style={'width': '100%', 'float': 'right', 'display': 'inline-block', 'padding-left':'2%'}
  #   	),

])	

# Yield Graph
@app.callback(
	Output('df1', 'figure'),
	[Input('increment_graph', 'value')]
)

def update_graph(value):
	global graphdDict
	global indexDict
	global names

	if value == "1 Day increment":
		# fig = px.line(df1, x="DATE", y="DGS1", color='DGS1')
		fig = go.Figure()
		fig.add_trace(go.Scatter(x=df1["DATE"], y=df1["DGS1"], name="DGS1",
                    line_shape='linear'))
		fig.add_trace(go.Scatter(x=df1["DATE"], y=df1["DGS5"], name="DGS5",
                    line_shape='linear'))
		fig.add_trace(go.Scatter(x=df1["DATE"], y=df1["DGS10"], name="DGS10",
                    line_shape='linear'))
		fig.add_trace(go.Scatter(x=df1["DATE"], y=df1["DGS30"], name="DGS30",
                    line_shape='linear'))
		fig.update_layout(
		    title="Yield Graph",
		    xaxis_title="Timeperiod",
		    yaxis_title="Yield,%",
		    legend_title="Tenors",
		    font=dict(
		        family="Courier New, monospace",
		        size=18,
		        color="RebeccaPurple"
		    )
		)
	else:
		fig = go.Figure()
		fig.add_trace(go.Scatter(x=df1["DATE"], y=df1["DGS1"], name="DGS1",
                    line_shape='linear'))
		fig.add_trace(go.Scatter(x=df1["DATE"], y=df1["DGS5"], name="DGS5",
                    line_shape='linear'))
		fig.add_trace(go.Scatter(x=df1["DATE"], y=df1["DGS10"], name="DGS10",
                    line_shape='linear'))
		fig.add_trace(go.Scatter(x=df1["DATE"], y=df1["DGS30"], name="DGS30",
                    line_shape='linear'))
		fig.update_layout(
		    title="Yield% Graph",
		    xaxis_title="Timeperiod",
		    yaxis_title="Yield,%",
		    legend_title="Tenors",
		    font=dict(
		        family="Courier New, monospace",
		        size=18,
		        color="RebeccaPurple"
		    )
		)

	return fig

# Increment Graph, dfi1
@app.callback(
	Output('dfi1', 'figure'),
	[Input('increment_graph', 'value')]
)

def update_graph(value):
	global graphdDict
	global indexDict
	global names

	if value == "DGS1":
		fig = go.Figure()
		fig.add_trace(go.Scatter(x=dfi1["DATE"], y=dfi1["DGS1"], name="DGS1",
                    line_shape='linear'))
		fig.update_layout(
		    title="1 Day Yield% increment Graph",
		    xaxis_title="Timeperiod",
		    yaxis_title="Yield,%",
		    legend_title="Tenors",
		    font=dict(
		        family="Courier New, monospace",
		        size=18,
		        color="RebeccaPurple"
		    )
		)
	elif value == "DGS5":
		fig = go.Figure()
		fig.add_trace(go.Scatter(x=dfi1["DATE"], y=dfi1["DGS5"], name="DGS5",
                    line_shape='linear'))
		fig.update_layout(
		    title="1 Day Yield% increment Graph",
		    xaxis_title="Timeperiod",
		    yaxis_title="Yield,%",
		    legend_title="Tenors",
		    font=dict(
		        family="Courier New, monospace",
		        size=18,
		        color="RebeccaPurple"
		    )
		)
	elif value == "DGS10":
		fig = go.Figure()
		fig.add_trace(go.Scatter(x=dfi1["DATE"], y=dfi1["DGS10"], name="DGS10",
                    line_shape='linear'))
		fig.update_layout(
		    title="1 Day Yield% increment Graph",
		    xaxis_title="Timeperiod",
		    yaxis_title="Yield,%",
		    legend_title="Tenors",
		    font=dict(
		        family="Courier New, monospace",
		        size=18,
		        color="RebeccaPurple"
		    )
		)
	elif value == "DGS30":
		fig = go.Figure()
		fig.add_trace(go.Scatter(x=dfi1["DATE"], y=dfi1["DGS30"], name="DGS30",
                    line_shape='linear'))
		fig.update_layout(
		    title="1 Day Yield% increment Graph",
		    xaxis_title="Timeperiod",
		    yaxis_title="Yield,%",
		    legend_title="Tenors",
		    font=dict(
		        family="Courier New, monospace",
		        size=18,
		        color="RebeccaPurple"
		    )
		)
	elif value == "ALL":
		fig = go.Figure()
		fig.add_trace(go.Scatter(x=dfi1["DATE"], y=dfi1["DGS1"], name="DGS1",
                    line_shape='linear'))
		fig.add_trace(go.Scatter(x=dfi1["DATE"], y=dfi1["DGS5"], name="DGS5",
                    line_shape='linear'))
		fig.add_trace(go.Scatter(x=dfi1["DATE"], y=dfi1["DGS10"], name="DGS10",
                    line_shape='linear'))
		fig.add_trace(go.Scatter(x=dfi1["DATE"], y=dfi1["DGS10"], name="DGS10",
                    line_shape='linear'))
		fig.update_layout(
		    title="1 Day Yield% increment Graph",
		    xaxis_title="Timeperiod",
		    yaxis_title="Yield,%",
		    legend_title="Tenors",
		    font=dict(
		        family="Courier New, monospace",
		        size=18,
		        color="RebeccaPurple"
		    )
		)
	return fig

# Increment Graph, dfi25
@app.callback(
	Output('dfi25', 'figure'),
	[Input('increment_graph', 'value')]
)

def update_graph(value):
	global graphdDict
	global indexDict
	global names

	if value == "DGS1":
		fig = go.Figure()
		fig.add_trace(go.Scatter(x=dfi25["DATE"], y=dfi25["DGS1"], name="DGS1",
                    line_shape='linear'))
		fig.update_layout(
		    title="25 Day Yield% increment Graph",
		    xaxis_title="Timeperiod",
		    yaxis_title="Yield,%",
		    legend_title="Tenors",
		    font=dict(
		        family="Courier New, monospace",
		        size=18,
		        color="RebeccaPurple"
		    )
		)
	elif value == "DGS5":
		fig = go.Figure()
		fig.add_trace(go.Scatter(x=dfi25["DATE"], y=dfi25["DGS5"], name="DGS5",
                    line_shape='linear'))
		fig.update_layout(
		    title="25 Day Yield% increment Graph",
		    xaxis_title="Timeperiod",
		    yaxis_title="Yield,%",
		    legend_title="Tenors",
		    font=dict(
		        family="Courier New, monospace",
		        size=18,
		        color="RebeccaPurple"
		    )
		)
	elif value == "DGS10":
		fig = go.Figure()
		fig.add_trace(go.Scatter(x=dfi25["DATE"], y=dfi25["DGS10"], name="DGS10",
                    line_shape='linear'))
		fig.update_layout(
		    title="25 Day Yield% increment Graph",
		    xaxis_title="Timeperiod",
		    yaxis_title="Yield,%",
		    legend_title="Tenors",
		    font=dict(
		        family="Courier New, monospace",
		        size=18,
		        color="RebeccaPurple"
		    )
		)
	elif value == "DGS30":
		fig = go.Figure()
		fig.add_trace(go.Scatter(x=dfi25["DATE"], y=dfi25["DGS30"], name="DGS30",
                    line_shape='linear'))
		fig.update_layout(
		    title="25 Day Yield% increment Graph",
		    xaxis_title="Timeperiod",
		    yaxis_title="Yield,%",
		    legend_title="Tenors",
		    font=dict(
		        family="Courier New, monospace",
		        size=18,
		        color="RebeccaPurple"
		    )
		)
	elif value == "ALL":
		fig = go.Figure()
		fig.add_trace(go.Scatter(x=dfi25["DATE"], y=dfi25["DGS1"], name="DGS1",
                    line_shape='linear'))
		fig.add_trace(go.Scatter(x=dfi25["DATE"], y=dfi25["DGS5"], name="DGS5",
                    line_shape='linear'))
		fig.add_trace(go.Scatter(x=dfi25["DATE"], y=dfi25["DGS10"], name="DGS10",
                    line_shape='linear'))
		fig.add_trace(go.Scatter(x=dfi25["DATE"], y=dfi25["DGS10"], name="DGS10",
                    line_shape='linear'))
		fig.update_layout(
		    title="25 Day Yield% increment Graph",
		    xaxis_title="Timeperiod",
		    yaxis_title="Yield,%",
		    legend_title="Tenors",
		    font=dict(
		        family="Courier New, monospace",
		        size=18,
		        color="RebeccaPurple"
		    )
		)
	return fig

# Increment Box Plt Graph, dfi1
@app.callback(
	Output('boxi1', 'figure'),
	[Input('increment_boxplot_graph', 'value')]
)

def update_graph(value):
	global graphdDict
	global indexDict
	global names

	if value == "DGS1":
		fig = go.Figure(data=[go.Box(x=dfi1["DGS1"], name="DGS1")])
		fig.update_layout(
		    title="1 Day Yield% increment Box Plot Graph",
		    xaxis_title="Yield,%",
		    yaxis_title="Tenors",
		    legend_title="Tenors",
		    font=dict(
		        family="Courier New, monospace",
		        size=18,
		        color="RebeccaPurple"
		    )
		)
	elif value == "DGS5":
		fig = go.Figure(data=[go.Box(x=dfi1["DGS5"], name="DGS5")])
		fig.update_layout(
		    title="1 Day Yield% increment Box Plot Graph",
		    xaxis_title="Yield,%",
		    yaxis_title="Tenors",
		    legend_title="Tenors",
		    font=dict(
		        family="Courier New, monospace",
		        size=18,
		        color="RebeccaPurple"
		    )
		)
	elif value == "DGS10":
		fig = go.Figure(data=[go.Box(x=dfi1["DGS10"], name="DGS10")])
		fig.update_layout(
		    title="1 Day Yield% increment Box Plot Graph",
		    xaxis_title="Yield,%",
		    yaxis_title="Tenors",
		    legend_title="Tenors",
		    font=dict(
		        family="Courier New, monospace",
		        size=18,
		        color="RebeccaPurple"
		    )
		)
	elif value == "DGS30":
		fig = go.Figure(data=[go.Box(x=dfi1["DGS30"], name="DGS30")])
		fig.update_layout(
		    title="1 Day Yield% increment Box Plot Graph",
		    xaxis_title="Yield,%",
		    yaxis_title="Tenors",
		    legend_title="Tenors",
		    font=dict(
		        family="Courier New, monospace",
		        size=18,
		        color="RebeccaPurple"
		    )
		)
	elif value == "ALL":
		fig = go.Figure(data=[go.Box(x=dfi1["DGS1"], name="DGS1"), go.Box(x=dfi1["DGS5"], name="DGS5"),
		       go.Box(x=dfi1["DGS10"], name="DGS10"), go.Box(x=dfi1["DGS30"], name="DGS30")])
		fig.update_layout(
		    title="1 Day Yield% increment Box Plot Graph",
		    xaxis_title="Yield,%",
		    yaxis_title="Tenors",
		    legend_title="Tenors",
		    font=dict(
		        family="Courier New, monospace",
		        size=18,
		        color="RebeccaPurple"
		    )
		)
	return fig

# Increment Box Plt Graph, dfi25
@app.callback(
	Output('boxi25', 'figure'),
	[Input('increment_boxplot_graph', 'value')]
)

def update_graph(value):
	global graphdDict
	global indexDict
	global names

	if value == "DGS1":
		fig = go.Figure(data=[go.Box(x=dfi25["DGS1"], name="DGS1")])
		fig.update_layout(
		    title="25 Day Yield% increment Box Plot Graph",
		    xaxis_title="Yield,%",
		    yaxis_title="Tenors",
		    legend_title="Tenors",
		    font=dict(
		        family="Courier New, monospace",
		        size=18,
		        color="RebeccaPurple"
		    )
		)
	elif value == "DGS5":
		fig = go.Figure(data=[go.Box(x=dfi25["DGS5"], name="DGS5")])
		fig.update_layout(
		    title="25 Day Yield% increment Box Plot Graph",
		    xaxis_title="Yield,%",
		    yaxis_title="Tenors",
		    legend_title="Tenors",
		    font=dict(
		        family="Courier New, monospace",
		        size=18,
		        color="RebeccaPurple"
		    )
		)
	elif value == "DGS10":
		fig = go.Figure(data=[go.Box(x=dfi25["DGS10"], name="DGS10")])
		fig.update_layout(
		    title="25 Day Yield% increment Box Plot Graph",
		    xaxis_title="Yield,%",
		    yaxis_title="Tenors",
		    legend_title="Tenors",
		    font=dict(
		        family="Courier New, monospace",
		        size=18,
		        color="RebeccaPurple"
		    )
		)
	elif value == "DGS30":
		fig = go.Figure(data=[go.Box(x=dfi25["DGS30"], name="DGS30")])
		fig.update_layout(
		    title="25 Day Yield% increment Box Plot Graph",
		    xaxis_title="Yield,%",
		    yaxis_title="Tenors",
		    legend_title="Tenors",
		    font=dict(
		        family="Courier New, monospace",
		        size=18,
		        color="RebeccaPurple"
		    )
		)
	elif value == "ALL":
		fig = go.Figure(data=[go.Box(x=dfi25["DGS1"], name="DGS1"), go.Box(x=dfi25["DGS5"], name="DGS5"),
		       go.Box(x=dfi25["DGS10"], name="DGS10"), go.Box(x=dfi25["DGS30"], name="DGS30")])
		fig.update_layout(
		    title="25 Day Yield% increment Box Plot Graph",
		    xaxis_title="Yield,%",
		    yaxis_title="Tenors",
		    legend_title="Tenors",
		    font=dict(
		        family="Courier New, monospace",
		        size=18,
		        color="RebeccaPurple"
		    )
		)
	return fig

# # Cullen and Fray Pic for 1-year bond
# @app.callback(
# 	Output('dfi1-DGS1-CF', 'src'),
# 	[Input('detector', 'value')]
# )

# def update_graph(value):
# 	global graphdDict
# 	global indexDict
# 	global names

# 	if value == "1 Day increment":
# 		src='data:image/png;base64,{}'.format(image_dfi1cf.decode())
# 	else:
# 		src='data:image/png;base64,{}'.format(image_dfi1cf.decode())
# 	return src

# # Distribution Fit Pic for 1-year bond
# @app.callback(
# 	Output('dfi1-DGS1-Fit', 'src'),
# 	[Input('detector', 'value')]
# )

# def update_graph(value):
# 	global graphdDict
# 	global indexDict
# 	global names

# 	if value == "1 Day increment":
# 		src='data:image/png;base64,{}'.format(image_dfi1fit.decode())
# 	else:
# 		src='data:image/png;base64,{}'.format(image_dfi1fit.decode())
# 	return src

# # Cullen and Fray Pic for 5-year bond
# @app.callback(
# 	Output('dfi1-DGS5-CF', 'src'),
# 	[Input('detector', 'value')]
# )

# def update_graph(value):
# 	global graphdDict
# 	global indexDict
# 	global names

# 	if value == "1 Day increment":
# 		src='data:image/png;base64,{}'.format(image_dfi5cf.decode())
# 	else:
# 		src='data:image/png;base64,{}'.format(image_dfi5cf.decode())
# 	return src

# # Distribution Fit Pic for 5-year bond
# @app.callback(
# 	Output('dfi1-DGS5-Fit', 'src'),
# 	[Input('detector', 'value')]
# )

# def update_graph(value):
# 	global graphdDict
# 	global indexDict
# 	global names

# 	if value == "1 Day increment":
# 		src='data:image/png;base64,{}'.format(image_dfi5fit.decode())
# 	else:
# 		src='data:image/png;base64,{}'.format(image_dfi5fit.decode())
# 	return src

#Average Term Structure
# @app.callback(
# 	Output('ats', 'figure'),
# 	[Input('average_term_structure', 'value')]
# )
# def update_graph(value):
# 	global graphdDict
# 	global indexDict
# 	global names
#     fig = go.Figure()
# 	if value == "Mean":
# 		fig = go.Figure()
# 		fig.add_trace(go.Scatter(x=ats["index"], y=ats["Mean"], name="Mean",
#                     line_shape='linear'))
# 	elif value == "Standard Deviation":
# 		fig = go.Figure()
# 		fig.add_trace(go.Scatter(x=ats["index"], y=ats["Std."], name="Standard Deviation",
#                     line_shape='linear'))
# 	elif value == "Both":
# 		fig = go.Figure()
# 		fig.add_trace(go.Scatter(x=ats["index"], y=ats["Mean"], name="Mean",
#                     line_shape='linear'))
# 		fig.add_trace(go.Scatter(x=ats["index"], y=ats["Std."], name="Standard Deviation",
#                     line_shape='linear'))
# 	return fig

#Relation Between Standard Deviation
# @app.callback(
# 	Output('std', 'figure'),
# 	[Input('detector', 'value')]
# )
# def update_graph(value):
# 	global graphdDict
# 	global indexDict
# 	global names

# 	if value == "1 Day increment":
# 		fig = go.Figure()
# 		fig.add_trace(go.Scatter(x=std["index"], y=std["Std_1inc"], name="Standard Deviation-1 Day Increment",
#                     line_shape='linear'))
# 		fig.add_trace(go.Scatter(x=std["index"], y=std["Std_25inc"], name="Standard Deviation-25 Day Increment",
#                     line_shape='linear'))
# 		# fig.show()
# 	else:
# 		fig = go.Figure()
# 		fig.add_trace(go.Scatter(x=std["index"], y=std["Std_1inc"], name="Standard Deviation-1 Day Increment",
#                     line_shape='linear'))
# 		fig.add_trace(go.Scatter(x=std["index"], y=std["Std_25inc"], name="Standard Deviation-25 Day Increment",
#                     line_shape='linear'))	

# 	return fig

if __name__ == '__main__':
    app.run_server(debug=True, port=5003, host='10.128.0.2')
