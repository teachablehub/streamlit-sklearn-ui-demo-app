import streamlit as st
import pandas as pd

# https://plotly.com/python/plotly-express/
import plotly.express as px

from teachablehub.clients import TeachableHubPredictAPI

teachable = TeachableHubPredictAPI(
    teachable=os.environ.get('TH_TEACHABLE', 'user/teachable'),
    environment=os.environ.get('TH_ENVIRONMENT', 'experiments'),
    serving_key=os.environ.get('TH_SERVING_KEY', 'you-serving-key')
)

st.markdown("""
# TeachableHub Iris Classifier App

This is a Interactive Application Interface integrated with the Teachable Prediction API for Realtime Cloud predictions from every device.

## **Features**
""")

sepal_length = st.slider('sepal_length', 0.0, 20.0, (3.1, ), key='sepal_length')
sepal_width = st.slider('sepal_width', 0.0, 20.0, (1.3, ), key='sepal_width')
petal_length = st.slider('petal_length', 0.0, 20.0, (4.7, ), key='petal_length')
petal_width = st.slider('petal_width', 0.0, 20.0, (2.5, ), key='petal_width')

predictions = teachable.predict([[sepal_length[0], sepal_width[0], petal_length[0], petal_width[0]]])

classes = []
probabilities = []

for prediction in predictions:
    classes.append(prediction['className'])
    probabilities.append(prediction['probability'])

chart_data = pd.DataFrame({
    "Probablities": probabilities,
    "Classes": classes,
})

# https://www.analyticsvidhya.com/blog/2020/10/create-interactive-dashboards-with-streamlit-and-python/
state_total_graph = px.bar(
    chart_data.sort_values(by=['Classes']),
    x='Probablities',
    y='Classes',
    color='Classes')
st.plotly_chart(state_total_graph)
