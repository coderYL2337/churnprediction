import plotly.graph_objects as go


def create_gauge_chart(probability):
    # Determine color based on churn probability
    if probability < 0.3:
        color = "green"
    elif probability < 0.6:
        color = "yellow"
    else:
        color = "red"

    # Create a gauge chart
    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=probability * 100,
            domain={'x': [0, 1], 'y': [0, 1]},
            title={
                'text': "Churn Probability",
                'font': {'size': 24}
            },
            number={'font': {'size': 40}},
            gauge={
                'axis': {
                    'range': [0, 100],
                    'tickwidth': 1,
                    'tickmode': 'array',
                    'tickvals': [0, 20, 40, 60, 80, 100] # Update tick values if needed
                },
                'bar': {'color': color},
                'bgcolor': "rgba(0,0,0,0)",
                'borderwidth': 2,
                'steps': [
                    {'range': [0, 30], 'color': "rgba(0,255,0,0.3)"},
                    {'range': [30, 60], 'color': "rgba(255,255,0,0.3)"},
                    {'range': [60, 100], 'color': "rgba(255,0,0,0.3)"}
                ],
                'threshold': {
                    'line': {'width': 4},
                    'thickness': 0.75,
                    'value': 100
                }
            }
        )
    )

    # Update chart layout
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        width=400,
        height=300,
        margin=dict(l=20, r=30, t=50, b=20)
    )

    # Configuration for the plot, including the color-changing script
    config = {
        'displayModeBar': False,
        'responsive': True,
        'postScript': """
        function updateColors(darkMode) {
            var textColor = darkMode ? 'white' : 'black';
            var update = {
                'title.font.color': textColor,
                'gauge.axis.tickcolor': textColor,
                'gauge.bordercolor': textColor,
                'gauge.threshold.line.color': textColor,
                'number.font.color': textColor
            };
            Plotly.relayout(document.getElementsByClassName('js-plotly-plot')[0], update);
        }

        function checkDarkMode() {
            var darkMode = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
            updateColors(darkMode);
        }

        window.matchMedia('(prefers-color-scheme: dark)').addListener(function(e) {
            updateColors(e.matches);
        });

        checkDarkMode();
        """
    }

    return fig, config


# def create_gauge_chart(probability):
#   #determine color based on churn probability
#   if probability<0.3:
#     color ="green"
#   elif probability <0.6:
#     color ="yellow"
#   else:
#     color ="red"

#   #create a gauge chart
#   fig = go.Figure(
#     go.Indicator(
#       mode = "gauge+number",
#       value=probability*100,
#       domain={
#         'x':[0,1],
#         'y':[0,1]
#       },
#       title={
#         'text':"Churn Probability",
#         'font':{
#           'size':24,
#           'color':'white'
#           }
#       },
#         number ={
#           'font':{
#           'size':40,
#           'color':'white'
#            }
#          },
#       gauge ={
#         'axis':{
#           'range':[0,100],
#           'tickwidth':1,
#           'tickcolor':'white'
#         },
#         'bar':{
#           'color':color
#         },
#         'bgcolor': "rgba(0,0,0,0)",
#         'borderwidth':2,
#         'bordercolor':'white',
#         'steps':[{
#           'range':[0,30],
#           'color':"rgba(0,255,0,0.3)"
#         },
#          {
#            'range':[30,60],
#            'color':"rgba(255,255,0,0.3)"
#          },
#          {
#            'range':[60,100],
#            'color':"rgba(255,0,0,0.3)"
#          }
#         ],
#          'threshold':{
#            'line':{
#              'color':'white',
#              'width':4
#            },
#            'thickness':0.75,
#            'value':100
#          }            
#       }))
#   #update chart layout
#   fig.update_layout(paper_bgcolor="rgba(0,0,0,0)",
#                     plot_bgcolor ="rgba(0,0,0,0)",
#                     font={'color':"white"},
#                     width = 400,
#                     height = 300,
#                     margin =dict(l=20, r=20, t=50, b=20)
#                    )
#   return fig


def create_model_probability_chart(probabilities):
  models=list(probabilities.keys())
  probs=list(probabilities.values())
  fig = go.Figure(data=[
    go.Bar(
      y=models,
      x=probs,
      orientation ='h',
      text = [f'{p:.2%}'for p in probs],
      textposition ='auto'
    )
  ])

  fig.update_layout(title='Churn Probability by Model',
                    yaxis_title='Models',
                    xaxis_title='Probability',
                    xaxis=dict(tickformat='.0%',range=[0,1]),
                    height=400,
                    margin=dict(l=20, r=20, t=40, b=20))


  return fig