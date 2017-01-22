# -*- coding: utf-8 -*-
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask.ext.wtf import Form
from wtforms import SelectField, SubmitField
#from wtforms.validators import Required, Length
import random, json
import plotly.plotly
import plotly.graph_objs as go
#import pandas as pd


import plotly.tools as tls
tls.set_credentials_file(username='nmamadeo', api_key='9eLPzUvSLGlWKczFs2ig')

app = Flask(__name__)
#app._static_folder = '/static'
app.config['SECRET_KEY'] = 'top secret!'
bootstrap = Bootstrap(app)

countsDct = {'Alabama':	[	11.8,	11.9	],
'Alaska':	[	8.1,	16.4	],
'Arizona':	[	8.2,	12.8	],
'Arkansas':	[	12.3,	11.1	],
'California':	[	6.8,	9.7	],
'Colorado':	[	7.2,	9.2	],
'Connecticut':	[	7.1,	6.9	],
'Delaware':	[	8.5,	6.8	],
'Florida':	[	8.5,	16.2	],
'Georgia':	[	8.8,	15.7	],
'Hawaii':	[	6.5,	4.7	],
'Idaho':	[	9,	12.9	],
'Illinois':	[	7.1,	8.1	],
'Indiana':	[	9.7,	11.2	],
'Iowa':	[	7.9,	5.9	],
'Kansas':	[	8.6,	10.6	],
'Kentucky':	[	12.9,	7	],
'Louisiana':	[	11,	13.8	],
'Maine':	[	11.9,	10.3	],
'Maryland':	[	7.1,	7.5	],
'Massachusetts':	[	7.9,	3.3	],
'Michigan':	[	10.3,	7.1	],
'Minnesota':	[	7.1,	5.2	],
'Mississippi':	[	11.9,	14.8	],
'Missouri':	[	10.4,	11.4	],
'Montana':	[	9.1,	14	],
'Nebraska':	[	7.3,	9.5	],
'Nevada':	[	9,	14	],
'New Hampshire':	[	8.5,	7.5	],
'New Jersey':	[	6.6,	10	],
'New Mexico':	[	10.1,	12.8	],
'New York':	[	7.4,	8.1	],
'North Carolina':	[	9.6,	13.1	],
'North Dakota':	[	6.8,	8.9	],
'Ohio':	[	9.9,	7.6	],
'Oklahoma':	[	11.3,	16.2	],
'Oregon':	[	10.2,	8.3	],
'Pennsylvania':	[	9.5,	7.5	],
'Rhode Island':	[	8.9,	6.7	],
'South Carolina':	[	10.3,	12.9	],
'South Dakota':	[	8.4,	12	],
'Tennessee':	[	11.2,	12	],
'Texas':	[	8.1,	19.1	],
'Utah':	[	6.6,	11.5	],
'Vermont':	[	10,	4.6	],
'Virginia':	[	7.7,	10.5	],
'Washington':	[	8.9,	7.6	],
'West Virginia':	[	14.4,	7.2	],
'Wisconsin':	[	8.5,	13.4	],
'Wyoming':	[	8.2,	6.6	]}

food = {'Alabama':	[	17.6	],
'Alaska':	[	13.3	],
'Arizona':	[	14.9	],
'Arkansas':	[	19.2	],
'California':	[	12.6	],
'Colorado':	[	12.1	],
'Connecticut':	[	13.1	],
'Delaware':	[	11.9	],
'Florida':	[	12.7	],
'Georgia':	[	14.9	],
'Hawaii':	[	9.7	],
'Idaho':	[	13.8	],
'Illinois':	[	11.1	],
'Indiana':	[	14.8	],
'Iowa':	[	10.6	],
'Kansas':	[	14.6	],
'Kentucky':	[	17.6	],
'Louisiana':	[	18.4	],
'Maine':	[	15.8	],
'Maryland':	[	10.7	],
'Massachusetts':	[	9.7	],
'Michigan':	[	14.9	],
'Minnesota':	[	9.9	],
'Mississippi':	[	20.8	],
'Missouri':	[	15.2	],
'Montana':	[	12.2	],
'Nebraska':	[	14.8	],
'Nevada':	[	14.2	],
'New Hampshire':	[	10.1	],
'New Jersey':	[	11.1	],
'New Mexico':	[	14.4	],
'New York':	[	14.1	],
'North Carolina':	[	15.9	],
'North Dakota':	[	8.5	],
'Ohio':	[	16.1	],
'Oklahoma':	[	15.5	],
'Oregon':	[	16.1	],
'Pennsylvania':	[	12.4	],
'Rhode Island':	[	11.8	],
'South Carolina':	[	13.2	],
'South Dakota':	[	11.5	],
'Tennessee':	[	15.1	],
'Texas':	[	15.4	],
'Utah':	[	11.9	],
'Vermont':	[	11.4	],
'Virginia':	[	9.8	],
'Washington':	[	12.9	],
'West Virginia':	[	15	],
'Wisconsin':	[	13.2	],
'Wyoming':	[	11.3	],}

wage = {'Alabama': [	69.4,	76.2,	58.0,	55.8,	'null',	'null'],
    'Alaska': [	69.4,	73.9,	56.0,	'null',	54.3,	55.5],
    'Arizona': [	72.1,	80.5,	52.4,	68.3,	50.0,	'null'],
    'Arkansas': [	71.1,	74.4,	61.8,	62.1,	46.2,	'null'],
    'California': [	62.2,	74.8,	53.2,	64.0,	41.9,	69.8],
    'Colorado': [	69.3,	74.1,	53.8,	59.5,	48.1,	66.3],
    'Connecticut': [	70.0,	73.8,	53.4,	60.8,	44.4,	66.8],
    'Delaware': [	72.5,	76.9,	62.3,	66.5,	49.9,	66.6],
    'Florida': [	66.7,	73.0,	56.5,	58.3,	52.1,	68.9],
    'Georgia': [	68.7,	75.5,	62.2,	62.4,	41.6,	72.8],
    'Hawaii': [	63.9,	79.0,	61.6,	'null',	57.8,	61.6],
    'Idaho': [	70.2,	72.7,	56.3,	29.5,	49.9,	'null'],
    'Illinois': [	69.3,	72.7,	63.3,	63.4,	51.4,	85.5],
    'Indiana': [	71.4,	71.4,	63.0,	66.9,	45.7,	'null'],
    'Iowa': [	76.2,	76.4,	57.6,	'null',	55.2,	'null'],
    'Kansas': [	75.0,	76.2,	65.6,	62.3,	65.0,	'null'],
    'Kentucky': [	75.0,	75.3,	65.0,	69.3,	'null',	'null'],
    'Louisiana': [	63.0,	70.2,	51.4,	51.4,	'null',	'null'],
    'Maine': [	75.8,	76.5,	65.0,	'null',	'null',	'null'],
    'Maryland': [	69.5,	75.6,	63.3,	64.5,	45.9,	68.0],
    'Massachusetts': [	66.7,	71.1,	50.0,	56.2,	41.7,	64.5],
    'Michigan': [	70.0,	70.0,	70.0,	69.2,	57.8,	76.4],
    'Minnesota': [	74.7,	76.7,	60.2,	65.6,	48.0,	68.3],
    'Mississippi': [	64.5,	74.4,	51.2,	51.2,	'null',	'null'],
    'Missouri': [	72.0,	73.1,	66.3,	'null',	61.0,	'null'],
    'Montana': [	69.1,	70.3,	52.6,	42.1,	'null',	'null'],
    'Nebraska': [	74.8,	76.4,	59.6,	67.3,	54.8,	'null'],
    'Nevada': [	67.3,	76.2,	55.1,	60.7,	49.0,	71.4],
    'New Hampshire': [	74.0,	74.2,	70.8,	'null',	'null',	'null'],
    'New Jersey': [	66.4,	75.9,	52.0,	53.2,	41.7,	79.2],
    'New Mexico': [	60.4,	69.5,	53.0,	'null',	54.3,	'null'],
    'New York': [	70.4,	80.0,	60.0,	64.0,	53.3,	66.0],
    'North Carolina': [	73.4,	76.9,	62.7,	65.3,	46.6,	62.2],
    'North Dakota': [	70,	70,	65,	'null',	'null',	'null'],
    'Ohio': [	74.5,	75.8,	67.7,	67.7,	59.2,	'null'],
    'Oklahoma': [	74.9,	77.4,	64.9,	75.0,	49.9,	'null'],
    'Oregon': [	65.6,	68.4,	53.2,	'null',	47.2,	66.7],
    'Pennsylvania': [	71.7,	73.9,	64.9,	64.9,	60.5,	87.7],
    'Rhode Island': [	71.1,	75.0,	51.2,	57.7,	41.0,	55.8],
    'South Carolina': [	68.6,	71.5,	62.8,	62.0,	57.1,	'null'],
    'South Dakota': [	76,	76,	67,	'null',	'null',	'null'],
    'Tennessee': [	74.7,	74.7,	63.3,	67.8,	44.8,	'null'],
    'Texas': [	63.9,	75.8,	51.2,	59.9,	46.7,	68.2],
    'Utah': [	61.3,	65.2,	48.9,	'null',	44.4,	56.2],
    'Vermont': [	81.1,	81.2,	75.4,	'null',	'null',	'null'],
    'Virginia': [	66.7,	75.0,	56.3,	56.2,	50.6,	63],
    'Washington': [	68.9,	72.3,	57.7,	'null',	55.7,	56.3],
    'West Virginia': [	76.3,	76.3,	82.1,	'null',	'null',	'null'],
    'Wyoming': [	71.7,	74.3,	58.7,	60.8,	58.5,	'null'],
    'Wisconsin': [	57.1,	57.3,	54.1,	'null',	53.1,	'null']}


wageRace = {'Alabama': [	46893,	26722,	33825,	40489,	46962	],
    'Alaska': [	68750,	52294,	57331,	66953,	73531	],
    'Arizona': [	66960,	40619,	37796,	48745,	53638	],
    'Arkansas': [	40599,	23805,	30492,	37823,	41680	],
    'California': [	73227,	43501,	45665,	58931,	67880	],
    'Colorado': [	64622,	33354,	38299,	55430,	61044	],
    'Connecticut': [	89434,	41800,	39547,	67034,	73930	],
    'Delaware': [	85117,	42126,	35507,	56860,	62288	],
    'Florida': [	54952,	32560,	39385,	44736,	49029	],
    'Georgia': [	59585,	34496,	33797,	47590,	55680	],
    'Hawaii': [	68103,	46204,	51924,	64098,	66650	],
    'Idaho': [	42422,	28526,	32991,	44926,	46723	],
    'Illinois': [	72711,	32655,	45638,	53966,	59467	],
    'Indiana': [	50629,	27815,	36913,	45424,	47967	],
    'Iowa': [	48609,	25311,	38135,	48044,	49187	],
    'Kansas': [	57002,	29127,	37649,	47817,	50014	],
    'Kentucky': [	54491,	27506,	33440,	40072,	41471	],
    'Louisiana': [	48019,	26728,	40060,	42492,	51512	],
    'Maine': [	44154,	24829,	33264,	45734,	46403	],
    'Maryland': [	89558,	54096,	60311,	69272,	77187	],
    'Massachusetts': [	78939,	42182,	33193,	64081,	68154	],
    'Michigan': [	65091,	28487,	36413,	42255,	48651	],
    'Minnesota': [	59893,	26930,	38751,	55616,	57979	],
    'Mississippi': [	42281,	23895,	38566,	36646,	45583	],
    'Missouri': [	62413,	29143,	35416,	45229,	47974	],
    'Montana': [	38521,	47804,	30117,	42322,	43768	],
    'Nebraska': [	43448,	24174,	35464,	47357,	49761	],
    'Nevada': [	62291,	41444,	43571,	53341,	58658	],
    'New Hampshire': [	64920,	40664,	40669,	60567,	61052	],
    'New Jersey': [	97257,	45252,	48442,	68342,	76412	],
    'New Mexico': [	57546,	38366,	36282,	43028,	51405	],
    'New York': [	59159,	39704,	37781,	54659,	62290	],
    'North Carolina': [	62699,	30845,	31449,	43674,	49785	],
    'North Dakota': [	37583,	20275,	46919,	47827,	49285	],
    'Ohio': [	64317,	26039,	34461,	45395,	48593	],
    'Oklahoma': [	49502,	27057,	32085,	41664,	45618	],
    'Oregon': [	58283,	32266,	35861,	48457,	49825	],
    'Pennsylvania': [	64927,	30693,	32339,	49520,	52258	],
    'Rhode Island': [	53615,	34844,	31525,	54119,	58986	],
    'South Carolina': [	50262,	28112,	32265,	42442,	49694	],
    'South Dakota': [	45064,	32224,	30560,	45043,	47072	],
    'Tennessee': [	63365,	29201,	32022,	41725,	44979	],
    'Texas': [	63692,	35438,	35628,	48259,	59836	],
    'Utah': [	47246,	25299,	40039,	55117,	58218	],
    'Vermont': [	30989,	43389,	55019,	51618,	52026	],
    'Virginia': [	83920,	40901,	54848,	59330,	64784	],
    'Washington': [	67506,	38287,	42532,	56548,	58431	],
    'West Virginia': [	46163,	25262,	44667,	37435,	37894	],
    'Wyoming': [	57955,	25807,	36980,	49993,	52080	],
    'Wisconsin': [	44032,	31019,	38329,	52664,	55132	],}

business = {'Alabama': [	54.4173106,	36.7844171,	24.6474036,	72.8715258	],
    'Alaska': [	52.0372766,	32.5449788,	20.1199436,	75.1807973	],
    'Arizona': [	49.0558603,	36.4904006,	27.0666059,	69.0064129	],
    'Arkansas': [	53.0947279,	32.7480287,	15.5122241,	81.4924189	],
    'California': [	52.2081619,	37.2017465,	45.6497191,	51.2648484	],
    'Colorado': [	51.9873865,	35.5361815,	15.6844225,	80.8191073	],
    'Connecticut': [	57.4989363,	32.6538983,	17.1760644,	79.4672674	],
    'Delaware': [	52.2051813,	32.6404969,	19.6682013,	74.616579	],
    'Florida': [	51.6565906,	38.4640511,	44.0966447,	53.4118628	],
    'Georgia': [	51.6826117,	40.4904373,	39.9615428,	57.9539589	],
    'Hawaii': [	50.9978557,	37.5276479,	62.6471035,	32.5105104	],
    'Idaho': [	48.0339875,	30.7694931,	72.23033,	89.3147939	],
    'Illinois': [	53.7126757,	36.78359,	27.4607341,	70.0543692	],
    'Indiana': [	52.9231264,	33.9828706,	12.785899,	84.5595219	],
    'Iowa': [	52.2466338,	31.7785899,	56.757268,	91.2936427	],
    'Kansas': [	52.346122,	32.282806,	10.9264045,	85.5485576	],
    'Kentucky': [	55.5440271,	31.9747486,	82.214836,	89.3254631	],
    'Louisiana': [	51.9226824,	36.4753277,	30.4375427,	67.0243862	],
    'Maine': [	56.7765279,	30.1404313,	31.088343,	94.0904206	],
    'Maryland': [	52.0027145,	39.3115557,	38.2353328,	59.1973351	],
    'Massachusetts': [	58.7755733,	32.7829195,	14.8053859,	82.2755668	],
    'Michigan': [	53.4869864,	36.8050335,	19.0562855,	78.7971758	],
    'Minnesota': [	54.8954635,	32.2416618,	96.634484,	87.5835046	],
    'Mississippi': [	53.1224783,	37.8668445,	31.7786064,	65.8701912	],
    'Missouri': [	52.4704743,	33.0785222,	12.4154302,	846149152	],
    'Montana': [	49.7362545,	31.5329259,	49.617947,	91.3955826	],
    'Nebraska': [	51.006466,	31.6511162,	88.799371,	87.8316036	],
    'Nevada': [	50.2108683,	36.3221751,	31.6364085,	63.8081319	],
    'New Hampshire': [	58.2780048,	29.2658655,	46.422765,	92.1443656	],
    'New Jersey': [	58.6540889,	31.9338255,	29.95147,	67.3925119	],
    'New Mexico': [	46.9943117,	39.008212,	40.050739,	55.4012539	],
    'New York': [	56.7405082,	36.1231127,	35.2924457,	62.135961	],
    'North Carolina': [	54.0552244,	35.6157993,	22.7522845,	74.8378692	],
    'North Dakota': [	54.2200088,	29.7583126,	46.726234,	91.2128314	],
    'Ohio': [	56.3737962,	33.9101738,	13.5556037,	83.9475295	],
    'Oklahoma': [	53.2944818,	32.1389608,	19.8255656,	76.1017514	],
    'Oregon': [	48.8324664,	36.2549918,	12.217916,	84.0034777	],
    'Pennsylvania': [	59.3980438,	31.2473282,	13.4821462,	83.9464331	],
    'Rhode Island': [	57.7449758,	32.2098011,	15.5713108,	81.4036052	],
    'South Carolina': [	55.0534909,	35.8571328,	22.6345159,	75.1290363	],
    'South Dakota': [	52.1656787,	29.1733281,	50.43412,	91.2856335	],
    'Tennessee': [	54.9091385,	35.5514458,	19.1177085,	78.8486937	],
    'Texas': [	53.1111515,	36.7743178,	45.4181779,	51.9718273	],
    'Utah': [	52.5668307,	30.3354162,	97.14063,	87.0363815	],
    'Vermont': [	54.4265235,	30.8821396,	31.044351,	92.9629288	],
    'Virginia': [	54.0440574,	36.1746069,	28.3289931,	68.9090361	],
    'Washington': [	48.5021846,	34.6573177,	17.1381772,	78.7958753	],
    'West Virginia': [	55.1509591,	34.1372832,	50.482807,	91.5672653	],
    'Wyoming': [	48.1186025,	30.9865923,	65.30828,	88.738847	],
    'Wisconsin': [	54.5641831,	30.9157467,	93.553975,	87.7486258	]}

preg = {'Alabama':	[	55,	],
    'Alaska':	[	48,	],
    'Arizona':	[	51,	],
    'Arkansas':	[	55,	],
    'California':	[	48,	],
    'Colorado':	[	45,	],
    'Connecticut':	[	51,	],
    'Delaware':	[	57,	],
    'Florida':	[	59,	],
    'Georgia':	[	60,	],
    'Hawaii':	[	56,	],
    'Idaho':	[	39,	],
    'Illinois':	[	52,	],
    'Indiana':	[	49,	],
    'Iowa':	[	43,	],
    'Kansas':	[	45,	],
    'Kentucky':	[	47,	],
    'Louisiana':	[	60,	],
    'Maine':	[	48,	],
    'Maryland':	[	58,	],
    'Massachusetts':	[	47,	],
    'Michigan':	[	54,	],
    'Minnesota':	[	40,	],
    'Mississippi':	[	62,	],
    'Missouri':	[	51,	],
    'Montana':	[	45,	],
    'Nebraska':	[	43,	],
    'Nevada':	[	52,	],
    'New Hampshire':	[	43,	],
    'New Jersey':	[	53,	],
    'New Mexico':	[	55,	],
    'New York':	[	55,	],
    'North Carolina':	[	54,	],
    'North Dakota':	[	44,	],
    'Ohio':	[	55,	],
    'Oklahoma':	[	51,	],
    'Oregon':	[	46,	],
    'Pennsylvania':	[	53,	],
    'Rhode Island':	[	52,	],
    'South Carolina':	[	50,	],
    'South Dakota':	[	46,	],
    'Tennessee':	[	56,	],
    'Texas':	[	54,	],
    'Utah':	[	36,	],
    'Vermont':	[	46,	],
    'Virginia':	[	54,	],
    'Washington':	[	48,	],
    'West Virginia':	[	52,	],
    'Wisconsin':	[	46,	],
    'Wyoming':	[	44,	],}
poverty1 = {'Alabama':	[	19.2	],
    'Alaska':	[	10.3	],
    'Arizona':	[	17.4	],
    'Arkansas':	[	19.1	],
    'California':	[	15.3	],
    'Colorado':	[	11.5	],
    'Connecticut':	[	10.5	],
    'Delaware':	[	12.4	],
    'Florida':	[	15.7	],
    'Georgia':	[	17	],
    'Hawaii':	[	10.6	],
    'Idaho':	[	15.1	],
    'Illinois':	[	13.6	],
    'Indiana':	[	14.5	],
    'Iowa':	[	12.2	],
    'Kansas':	[	13	],
    'Kentucky':	[	18.5	],
    'Louisiana':	[	19.6	],
    'Maine':	[	13.4	],
    'Maryland':	[	9.7	],
    'Massachusetts':	[	11.5	],
    'Michigan':	[	15.8	],
    'Minnesota':	[	10.2	],
    'Mississippi':	[	22	],
    'Missouri':	[	14.8	],
    'Montana':	[	14.6	],
    'Nebraska':	[	12.6	],
    'Nevada':	[	14.7	],
    'New Hampshire':	[	8.2	],
    'New Jersey':	[	10.8	],
    'New Mexico':	[	20.4	],
    'New York':	[	15.4	],
    'North Carolina':	[	16.4	],
    'North Dakota':	[	11	],
    'Ohio':	[	14.8	],
    'Oklahoma':	[	16.1	],
    'Oregon':	[	15.4	],
    'Pennsylvania':	[	13.2	],
    'Rhode Island':	[	13.9	],
    'South Carolina':	[	16.6	],
    'South Dakota':	[	13.7	],
    'Tennessee':	[	16.7	],
    'Texas':	[	15.9	],
    'Utah':	[	11.3	],
    'Vermont':	[	10.2	],
    'Virginia':	[	11.2	],
    'Washington':	[	12.2	],
    'West Virginia':	[	17.9	],
    'Wisconsin':	[	11.1	],
    'Wyoming':	[	12.1	],}
def make_bar_chart(choice, state):
    trace1 = go.Bar(
        x=['<65 w/ a disability', 'w/o health insurance'],
        y=countsDct[choice],
        name= choice
    )
    trace2 = go.Bar(
        x=['<65 w/ a disability', 'w/o health insurance'],
        y=countsDct[state],
        name= state
    )
    graphs = [ dict (data = [trace1, trace2], layout = go.Layout( barmode = 'group',
                                                                width = 400,
                                                                height = 300,
                                                                title = 'Health Differences'), 
                     yaxis = dict(
                                titlefont=dict(
                                    color='rgb(000, 000, 000)'
                                ),
                            title='Percentages',
                        ),
                    margin=dict(
                            l=20,
                            r=20,
                            b=20,
                            t=20
                        ),)]
    graphJSON = json.dumps(graphs, cls=plotly.utils.PlotlyJSONEncoder)
    print(graphJSON)
    return graphJSON

def make_bar_preg(choice, state):
    trace1 = go.Bar(
        x=['unplanned pregnancy %',],
        y=preg[choice],
        name= choice
    )
    trace2 = go.Bar(
        x=['unplanned pregnancy %',],
        y=preg[state],
        name= state
    )
    graphs = [ dict (data = [trace1, trace2], layout = go.Layout( barmode = 'group',
                                                                width = 400,
                                                                height = 300,
                                                                title = 'Unplanned Pregnancy'),
                            yaxis = dict(
                                titlefont=dict(
                                    color='rgb(000, 000, 000)'
                                ),
                            title='Percentage of all Pregnancies',
                        ),
                    margin=dict(
                            l=20,
                            r=20,
                            b=20,
                            t=20
                        ),)]
    graphJSON = json.dumps(graphs, cls=plotly.utils.PlotlyJSONEncoder)
    print(graphJSON)
    return graphJSON

def make_bar_poverty(choice, state):
    trace1 = go.Bar(
        x=['In poverty',],
        y=poverty1[choice],
        name= choice
    )
    trace2 = go.Bar(
        x=['In poverty',],
        y=poverty1[state],
        name= state
    )
    graphs = [ dict (data = [trace1, trace2], layout = go.Layout( barmode = 'group',
                                                                width = 400,
                                                                height = 300,
                                                                title = 'Percent in Poverty'),
                            yaxis = dict(
                                titlefont=dict(
                                    color='rgb(000, 000, 000)'
                                ),
                        ),
                    margin=dict(
                            l=20,
                            r=20,
                            b=20,
                            t=20
                        ),)]
    graphJSON = json.dumps(graphs, cls=plotly.utils.PlotlyJSONEncoder)
    print(graphJSON)
    return graphJSON

def make_bar_food(choice, state):
    trace1 = go.Bar(
        x=['W/o Food Security',],
        y=food[choice],
        name= choice
    )
    trace2 = go.Bar(
        x=['W/o Food Security',],
        y=food[state],
        name= state
    )
    graphs = [ dict (data = [trace1, trace2], layout = go.Layout( barmode = 'group',
                                                                width = 400,
                                                                height = 300,
                                                                title = 'Percent without Food Security'),
                            yaxis = dict(
                                titlefont=dict(
                                    color='rgb(000, 000, 000)'
                                ),
                        ),
                    margin=dict(
                            l=20,
                            r=20,
                            b=20,
                            t=20
                        ),)]
    graphJSON = json.dumps(graphs, cls=plotly.utils.PlotlyJSONEncoder)
    print(graphJSON)
    return graphJSON

def make_bar_wage_chart(choice, state):
    
    graphs = [
            dict(
                data = [
                        dict(
                            x=['All', 'White', 'All POC', 'Black', 'Hispanic', 'Asian/NHPI'],
                            y=wage[choice],
                            mode='markers',
                            name=choice,
                            marker=dict(
                            color='rgba(33, 37, 174, 0.95)',
                            line=dict(
                            color='rgba(33, 37, 174, 1.0)',
                            width=1,
                            ),
                            symbol='circle',
                            size=16,
                            )
                           ,),
                           dict(
                            x=['All', 'White', 'All POC', 'Black', 'Hispanic', 'Asian/NHPI'],
                                                y=wage[state],
                                                mode='markers',
                                                name=state,
                                                marker=dict(
                                                    color='rgba(255, 120, 255, 0.95)',
                                                    line=dict(
                                                        color='rgba(255, 120, 255, 1.0)',
                                                        width=1,
                                                    ),
                                                    symbol='circle',
                                                    size=16,
                                                    )
                                                ),
                        
                        ],
                layout =
                    go.Layout(
                        title="Women's Wage Gap by Race",
                        titlefont=dict(
                                color='rgb(000, 000, 000)',
                                size = 15,
                            ),
                        xaxis=dict(
                            showgrid=False,
                            showline=True,
                            linecolor='rgb(102, 102, 102)',
                            titlefont=dict(
                                color='rgb(000, 000, 000)'
                            ),
                            tickfont=dict(
                                color='rgb(102, 102, 102)',
                            ),
                            autotick=False,
                            dtick=1,
                            ticks='outside',
                            tickcolor='rgb(102, 102, 102)',
                        ),
                        margin=dict(
                            l=50,
                            r=40,
                            b=50,
                            t=80
                        ),
                        yaxis = dict(
                            titlefont=dict(
                                color='rgb(000, 000, 000)'
                            ),
                            title='Cents on A Dollar Earned by White Men',
                        ),
                        legend=dict(
                            font=dict(
                                size=10,
                            ),
                            yanchor='middle',
                            xanchor='right',
                        ),
                        width=400,
                        height=400,
                        plot_bgcolor='rgb(242,243,255)',
                        hovermode='closest',
                        )
                )
        ]
    
    graphLine = json.dumps(graphs, cls=plotly.utils.PlotlyJSONEncoder)
    print(graphLine)
    return graphLine


def make_bar_wagerace_chart(choice, state):
    
    graphs = [
            dict(
                data = [
                        dict(
                            x=['Asian', 'Black', 'Hispanic', 'All', 'White'],
                            y=wageRace[choice],
                            mode='markers',
                            name=choice,
                            marker=dict(
                            color='rgba(33, 37, 174, 0.95)',
                            line=dict(
                            color='rgba(33, 37, 174, 1.0)',
                            width=1,
                            ),
                            symbol='circle',
                            size=16,
                            )
                           ,),
                           dict(
                            x=['Asian', 'Black', 'Hispanic', 'All', 'White'],
                                                y=wageRace[state],
                                                mode='markers',
                                                name=state,
                                                marker=dict(
                                                    color='rgba(255, 120, 255, 0.95)',
                                                    line=dict(
                                                        color='rgba(255, 120, 255, 1.0)',
                                                        width=1,
                                                    ),
                                                    symbol='circle',
                                                    size=16,
                                                    )
                                                ),
                        
                        ],
                layout =
                    go.Layout(
                        title="Overall Wage Gap by Race",
                        titlefont=dict(
                                color='rgb(000, 000, 000)',
                                size = 15,
                            ),
                        xaxis=dict(
                            showgrid=False,
                            showline=True,
                            linecolor='rgb(102, 102, 102)',
                            titlefont=dict(
                                color='rgb(000, 000, 000)'
                            ),
                            tickfont=dict(
                                color='rgb(102, 102, 102)',
                            ),
                            autotick=False,
                            dtick=1,
                            ticks='outside',
                            tickcolor='rgb(102, 102, 102)',
                        ),
                        margin=dict(
                            l=50,
                            r=40,
                            b=50,
                            t=80
                        ),
                        yaxis = dict(
                            titlefont=dict(
                                color='rgb(000, 000, 000)'
                            ),
                            title='Annual Salary',
                        ),
                        legend=dict(
                            font=dict(
                                size=10,
                            ),
                            yanchor='middle',
                            xanchor='right',
                        ),
                        width=400,
                        height=400,
                        plot_bgcolor='rgb(242,243,255)',
                        hovermode='closest',
                        )
                )
        ]
    
    graphLine = json.dumps(graphs, cls=plotly.utils.PlotlyJSONEncoder)
    print(graphLine)
    return graphLine





def make_barbus_chart(choice, state):
    trace1 = go.Bar(
        x=['by men', 'by women', 'by people of color', 'by non-poc'],
        y=business[choice],
        name= choice
    )
    trace2 = go.Bar(
        x=['by men', 'by women', 'by people of color', 'by non-poc'],
        y=business[state],
        name= state
    )
    graphs = [ dict (data = [trace1, trace2], layout = go.Layout( barmode = 'group',
                                                                width = 400,
                                                                height = 300,
                                                                yaxis = dict(
                                                            titlefont=dict(
                                                            color='rgb(000, 000, 000)'
                                                            ),
                                                                title='Percent of Owners',
                                                                ),
                                                                 xaxis = dict(
                                                            titlefont=dict(
                                                            color='rgb(000, 000, 000)'
                                                            ),
                                                                title='Ownership Demographics',
                                                                ),
                                                                title = 'Business Ownership by Race and Gender'),
                    margin=dict(
                            l=20,
                            r=20,
                            b=20,
                            t=20
                        ),)]
    graphJSON = json.dumps(graphs, cls=plotly.utils.PlotlyJSONEncoder)
    print(graphJSON)
    return graphJSON


class ChoiceForm(Form):
    
    choice = SelectField(u'Your state', choices=[("blank", "Make a choice"), ('Alabama','Alabama'),
    ('Alaska','Alaska'),
    ('Arizona','Arizona'),
    ('Arkansas','Arkansas'),
    ('California','California'),
    ('Colorado','Colorado'),
    ('Connecticut','Connecticut'),
    ('Delaware','Delaware'),
    ('Florida','Florida'),
    ('Georgia','Georgia'),
    ('Hawaii','Hawaii'),
    ('Idaho','Idaho'),
    ('Illinois','Illinois'),
    ('Indiana','Indiana'),
    ('Iowa','Iowa'),
    ('Kansas','Kansas'),
    ('Kentucky','Kentucky'),
    ('Louisiana','Louisiana'),
    ('Maine','Maine'),
    ('Maryland','Maryland'),
    ('Massachusetts','Massachusetts'),
    ('Michigan','Michigan'),
    ('Minnesota','Minnesota'),
    ('Mississippi','Mississippi'),
    ('Missouri','Missouri'),
    ('Montana','Montana'),
    ('Nebraska','Nebraska'),
    ('Nevada','Nevada'),
    ('New Hampshire', 'New Hampshire'),
    ('New Jersey', 'New Jersey'),
    ('New Mexico', 'New Mexico'),
    ('New York', 'New York'),
    ('North Carolina', 'North Carolina'),
    ('North Dakota', 'North Dakota'),
    ('Ohio','Ohio'),
    ('Oklahoma','Oklahoma'),
    ('Oregon','Oregon'),
    ('Pennsylvania','Pennsylvania'),
    ('Rhode Island', 'Rhode Island'),
    ('South Carolina', 'South Carolina'),
    ('South Dakota', 'South Dakota'),
    ('Tennessee','Tennessee'),
    ('Texas','Texas'),
    ('Utah','Utah'),
    ('Vermont','Vermont'),
    ('Virginia','Virginia'),
    ('Washington','Washington'),
    ('West Virginia','West Virginia'),
    ('Wyoming','Wyoming'),
    ('Wisconsin','Wisconsin')])
    
    state = SelectField(u'Select a state to compare', choices=[("blank", "Make a choice"), ('Alabama','Alabama'),
('Alaska','Alaska'),
('Arizona','Arizona'),
('Arkansas','Arkansas'),
('California','California'),
('Colorado','Colorado'),
('Connecticut','Connecticut'),
('Delaware','Delaware'),
('Florida','Florida'),
('Georgia','Georgia'),
('Hawaii','Hawaii'),
('Idaho','Idaho'),
('Illinois','Illinois'),
('Indiana','Indiana'),
('Iowa','Iowa'),
('Kansas','Kansas'),
('Kentucky','Kentucky'),
('Louisiana','Louisiana'),
('Maine','Maine'),
('Maryland','Maryland'),
('Massachusetts','Massachusetts'),
('Michigan','Michigan'),
('Minnesota','Minnesota'),
('Mississippi','Mississippi'),
('Missouri','Missouri'),
('Montana','Montana'),
('Nebraska','Nebraska'),
('Nevada','Nevada'),
('New Hampshire', 'New Hampshire'),
('New Jersey', 'New Jersey'),
('New Mexico', 'New Mexico'),
('New York', 'New York'),
('North Carolina', 'North Carolina'),
('North Dakota', 'North Dakota'),
('Ohio','Ohio'),
('Oklahoma','Oklahoma'),
('Oregon','Oregon'),
('Pennsylvania','Pennsylvania'),
('Rhode Island', 'Rhode Island'),
('South Carolina', 'South Carolina'),
('South Dakota', 'South Dakota'),
('Tennessee','Tennessee'),
('Texas','Texas'),
('Utah','Utah'),
('Vermont','Vermont'),
('Virginia','Virginia'),
('Washington','Washington'),
('West Virginia','West Virginia'),
('Wyoming','Wyoming'),
('Wisconsin','Wisconsin')])
    
    gender =SelectField(u'Your gender', choices=[("blank", "Make a choice"), 
        ('Female','Female'),
        ('Male','Male'),
        ('Non-binary','Non-binary'),
	('Other','Other')
        ])
    race = SelectField(u'Your race', choices=[("blank", "Make a choice"),
    ('White','White'),
    ('Black','Black'),
    ('Hispanic','Hispanic'),
    ('Asian/NHPI','Asian/NHPI'),
    ('Native American','Native American'),
    ('Mixed race','Mixed race'),
    ('Other','Other')
    ])
    
    
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
	return render_template('index.html')

@app.route('/match', methods=['GET', 'POST'])
def match():
    
    choice = None
    state = None
    race = None
    gender = None
    ids = []
    id2 = []
    idWR = []
    idBus = []
    idPreg = []
    idPov = []
    idFood = []
    graphJSON = []
    graphJSON2 = []
    graphWageRace = []
    graphBusiness = []
    graphPreg = []
    graphPov = []
    graphFood = []
    form = ChoiceForm()
    if form.validate_on_submit():
        choice = form.choice.data
        state = form.state.data
        race = form.race.data
        gender = form.gender.data
        if choice and state and race and gender != "blank":
            graphJSON = make_bar_wage_chart(choice, state)
            graphJSON2 = make_bar_chart(choice, state)
            graphWageRace = make_bar_wagerace_chart(choice, state)
            graphBusiness = make_barbus_chart(choice, state)
            graphPreg = make_bar_preg(choice, state)
            graphPov = make_bar_poverty(choice, state)
            graphFood = make_bar_food(choice, state)
            ids = ["Bar Chart for x"]
            id2 = ["Scatter Plot for y"]
            idWR = ["Wage Gap by Race"]
            idBus = ["Business Ownership by Race and Gender"]
            idPreg = ["Percentage of Unplanned Pregnancies"]
            idPov = ["Percentage in Poverty"]
            idFood = ["Percentage without Food Security"]
    return render_template('match.html', form=form, choice=choice, state = state,
                           race = race, gender = gender,
                           graphJSON=graphJSON, graphJSON2 = graphJSON2,
                           graphBusiness = graphBusiness, idBus = idBus,
                            graphWageRace = graphWageRace, idWR = idWR,
                           ids=ids, id2 = id2, idPreg = idPreg, graphPreg = graphPreg,
                          graphPov = graphPov, idPov = idPov, idFood = idFood, graphFood = graphFood)

@app.route('/about', methods=['GET', 'POST'])
def about():
    return render_template('about.html')

@app.route('/charities', methods=['GET', 'POST'])
def charities():
    return render_template('charities.html')

@app.route('/healthcare', methods=['GET', 'POST'])
def healthcare():
    return render_template('healthcare.html')

@app.route('/education', methods=['GET', 'POST'])
def education():
    return render_template('education.html')

@app.route('/foodsecurity', methods=['GET', 'POST'])
def foodsecurity():
    return render_template('foodsecurity.html')

@app.route('/minorities', methods=['GET', 'POST'])
def minorities():
    return render_template('minorities.html')

@app.route('/parenthood', methods=['GET', 'POST'])
def parenthood():
    return render_template('parenthood.html')

@app.route('/poverty', methods=['GET', 'POST'])
def poverty():
    return render_template('poverty.html')

if __name__ == '__main__':
    app.run(debug=True, port = 7000)
    #app.run(host='0.0.0.0', port = 1561, debug=True)
