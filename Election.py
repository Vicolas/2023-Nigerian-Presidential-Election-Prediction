#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 00:20:33 2023

@author: mac
"""

import streamlit as st
import pandas as pd
import plotly.express as px



#dataset = pd.read_csv('./data/election_predict.csv')
dataset = pd.read_csv('/Users/mac/Downloads/election_predict.csv')


st.set_page_config(page_title='2023 Nigerian Presdential Election Prediction', page_icon=None, layout="wide", initial_sidebar_state="auto", menu_items=None)


st.header(('2023 Nigerian Presdential Election Prediction'))
st.text('This dataset visualizes the forth coming 2023 Nigerian Presidential Election \nusing the sentiment of its citizens, gathered from twitter.')


st.sidebar.header('Filter By:')
st.sidebar.text('Have a general overview of \nall parties or make a selection \nof preferred party.')

party=st.sidebar.multiselect('Filter By Party:',
                                  options=dataset['party'].unique(),
                                  default=dataset['party'].unique())
selection_query=dataset.query(
    'party==@party'
)


st.header(('Election Prediction Dashboard'))
st.text('The dashboards visualizes the total sentiments (specific views and opinions) of \nNigerian citizens across the globe. It displays Sentiment score to the left \nand Ratio which describes the kind and level of sentiment the people have \ntowards a party.')

sentiment=(selection_query['sentiment_score'].sum())
rating= (selection_query['Analysis'].value_counts(normalize=True)*100)
         

first_column,second_column=st.columns(2)
with first_column:
    st.markdown('### Sentiment Score:')
    st.subheader(f'{sentiment}')
with second_column:
    st.markdown('### % Rating')
    st.subheader(f'{rating}')
    
st.markdown('----')

sentiment_by_party=(selection_query.groupby(by=['party']).sum()[['sentiment_score']])


sentiment_by_party_barchart=px.bar(sentiment_by_party,
                                   x='sentiment_score',
                                   y=sentiment_by_party.index,
                                   title='Sentiment By Party',
                                   color_discrete_sequence=['#17f50c'],
                                   )

rating_by_party=(selection_query.groupby(by=['Analysis']).mean()[['sentiment_score']])
                 #mean()[['sentiment_score']])
                 
              

#rating_by_party_piechart=px.pie(rating_by_party)

sentiment_by_party_barchart.update_layout(plot_bgcolor = 'rgba(0,0,0,0)', xaxis=dict(showgrid=False))
#rating_by_party_piechart=px.pie(rating_by_party, names=rating_by_party.index, values=(rating), color_discrete_sequence=px.colors.sequential.RdPu_r)


#rating_by_party_histogramchart = px.histogram(rating_by_party, y='sentiment_score')


left_column, right_column=st.columns(2)
#left_column.plotly_chart(sentiment_by_party_barchart,use_container_width=True)
left_column.plotly_chart(sentiment_by_party_barchart,use_container_width=True)
