
# -*- coding: utf-8 -*-
"""FinalProjectDemo.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1cfpFlrKa_25xSYj_oShMH1vAZOc1o6bu
"""
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from textblob import TextBlob

def analyze_sentiment(text_content):
    try:
        analysis = TextBlob(text_content)
        return analysis.sentiment.polarity, analysis.sentiment.subjectivity
    except Exception as e:
        st.write("Error in sentiment analysis:", e)
        return None, None

def load_data():
    data = pd.read_csv('b_fixed.csv')
    return data

df = load_data()
results = []
for review in df['Review']:
    results.append(analyze_sentiment(review))

df['sentiment_polarity'], df['sentiment_subjectivity'] = zip(*results)
df.to_csv('analyzed_reviews.csv', index=False)

st.write("Sentiment Analysis Results:")
st.dataframe(df.head())

# Example of additional visualization
st.line_chart(df['sentiment_polarity'])
