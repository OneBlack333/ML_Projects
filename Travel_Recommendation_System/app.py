import streamlit as st
import pickle
import pandas as pd
import spacy
nlp = spacy.load("en_core_web_lg")

df = pickle.load(open('travel_place.pkl','rb'))

st.title('Travel Recommendation System')
text = nlp(st.text_input("Free_Style_Search"))
n = st.number_input("Number of recommend",min_value=1, step=1)

if st.button('Recommend'):
    score_list = []
    rating_list = []

    for i in df['about_place']:
        z = nlp(i)
        score_list.append(text.similarity(z))
    index_value = sorted(enumerate(score_list),reverse=True,key = lambda x:x[1])[0:n]

    for index,value in index_value:
        st.header(f"Place Name: {df['place_name'][index]}")
        st.image(df['link'][index])
        col1, col2 = st.columns(2)
        with col1:
            st.header(f"Rating: {df['rating'][index]}")
        with col2:
            st.header(f"Best Time to Visit: {df['best_time_to_visit'][index]}")
