# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 15:19:42 2020

@author: rom1l
"""
import plotly.graph_objects as go
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import pandas as pd
import numpy as np

data_modele = {'Modeles' :  ['RL','Lasso','Ridge','Elastic-net','Tree','RF','Extra-Tree','XGB','LGB','RL','Lasso','Ridge','Elastic-net','Tree','RF','Extra-Tree','XGB','LGB'],
        'PreProcess' : ['Oui','Oui','Oui','Oui','Oui','Oui','Oui','Oui','Oui','Non','Non','Non','Non','Non','Non','Non','Non','Non'],
        'AUC': [71.76,83.93,83.41,83.94,83.14,85.11,85.72,85.70,85.49,70.75,74.93,74.78,74.7,82.94,85.70,85.98,85.04,86.01]}
df_modele = pd.DataFrame.from_dict(data_modele)


data_resume = {'Catégories': ['Modèle à base de Regression Logistique', "Modèle à base d'arbre",'Moyenne', 'Modèle à base de Regression Logistique', "Modèle à base d'arbre",'Moyenne'],
               'PreProcess' :['Oui','Oui','Oui','Non','Non','Non'],
                'AUC': [83.76,85.03,83.13,74.83,85.31,80.19]}
df_resume = pd.DataFrame.from_dict(data_resume)

st.write("""
# Présentation des résultats
Sélectionner *** une base de donnée*** and ***un type de préparation*** pour observer les résultats des différents modèles!
         """)

st.sidebar.header('Paramètres')
base = st.sidebar.selectbox('Choix de la base de donnée', ('Churn Modelling', 'Adult', 'Telco Customer Churn', 'CreditCard'))

option = st.sidebar.multiselect('Options',('Préparation des données (Data cleaning, Feature engineering)','Sans Préparation'))
Resume = st.sidebar.checkbox('Résumé des différents modèles')



modeles = ['RL','Lasso','Ridge','Elastic-net','Tree','RF','Extra-Tree','XGB','LGB']
categ = ['Modèle à base de Regression Logistique', "Modèle à base d'arbre",'Moyenne']


#CHURN MODELLING
fig_churn = go.Figure(data=[
                go.Bar(name = 'Avec Préparation des données', x = modeles, y = [71.76,83.93,83.41,83.94,83.14,85.11,85.72,85.70,85.49]),
                go.Bar(name = 'Sans Préparation des données', x= modeles, y =[70.75,74.93,74.78,74.7,82.94,85.70,85.98,85.04,86.01])
                ])
fig_churn.update_layout(title_text='Résultats Churn Modelling',
                  yaxis_title="Moyenne des AUC en %",
                  title_font_color="blue")

fig_churn2 = go.Figure(data=[
                go.Bar(name = 'Sans Préparation des données', x = modeles, y = [70.75,74.93,74.78,74.7,82.94,85.70,85.98,85.04,86.01])
                ])
fig_churn2.update_layout(title_text='Résultats Churn Modelling sans préparation des données',
                  yaxis_title="Moyenne des AUC en %",)


fig_churn1 = go.Figure(data=[
                go.Bar(name = 'Avec Préparation des données', x = modeles, y = [71.76,83.93,83.41,83.94,83.14,85.11,85.72,85.70,85.49])
                ])
fig_churn1.update_layout(title_text='Résultats Churn Modelling avec préparation des données',
                  yaxis_title="Moyenne des AUC en %",)


fig_churn3 = go.Figure(data=[
                go.Bar(name = 'Avec  Préparation des données', x = categ, y = [83.76,85.03,83.13]),
                go.Bar(name = 'Sans Préparation des données', x= categ, y =[74.83,85.31,80.19])
                ])
fig_churn3.update_layout(title_text='Résultats Churn Modelling',
                  yaxis_title="Moyenne des AUC en %",)



#ADULT

fig_adult = go.Figure(data=[
                go.Bar(name = 'Avec Préparation des données', x = modeles, y = [84.65,91.98,91.39,91.94,90.51,91.75,92.01,92.37,92.70]),
                go.Bar(name = 'Sans Préparation des données', x= modeles, y =[73.75,83.01,81.82,83.00,85.29,91.79,91.01,92.59,92.95])
                ])
fig_adult.update_layout(title_text='Résultats Adult',
                  yaxis_title="Moyenne des AUC en %",)

fig_adult1 = go.Figure(data=[
                go.Bar(name = 'Avec Préparation de données', x = modeles, y = [84.65,91.98,91.39,91.94,90.51,91.75,92.01,92.37,92.70])
                ])
fig_adult1.update_layout(title_text='Résultats Adult avec préparation des données',
                  yaxis_title="Moyenne des AUC en %",)

fig_adult2 = go.Figure(data=[
                go.Bar(name = 'Sans Préparation des données', x = modeles, y = [73.75,83.01,81.82,83.00,85.29,91.79,91.01,92.59,92.95])
                ])
fig_adult2.update_layout(title_text='Résultats Adult sans préparation des données',
                  yaxis_title="Moyenne des AUC en %",)

fig_adult3 = go.Figure(data=[
                go.Bar(name = 'Avec Préparation des données', x = categ, y = [91.95,92.23,91.03]),
                go.Bar(name = 'Sans Préparation des données', x= categ, y =[82.61,90.72,86.13])
                ])
fig_adult3.update_layout(title_text='Résultats Telco Customer Churn',
                  yaxis_title="Moyenne des AUC en %",)


#Telco Customer Churn
fig_telco = go.Figure(data=[
                go.Bar(name = 'Avec Préparation des données', x = modeles, y = [84.48,84.55,83.99,84.53,83.19,84.61,84.34,84.64,84.69]),
                go.Bar(name = 'Sans Préparation des données', x= modeles, y =[83.79,81.00,80.75,80.94,80.44,84.42,84.12,84.53,84.48])
                ])
fig_telco.update_layout(title_text='Résultats Telco Customer Churn',
                  yaxis_title="Moyenne des AUC en %",)

fig_telco1 = go.Figure(data=[
                go.Bar(name = 'Avec Préparation des données', x = modeles, y = [84.48,84.55,83.99,84.53,83.19,84.61,84.34,84.64,84.69])
                ])
fig_telco1.update_layout(title_text='Résultats Telco Customer Churn avec préparation des données',
                  yaxis_title="Moyenne des AUC en %",)

fig_telco2 = go.Figure(data=[
                go.Bar(name = 'Sans Préparation des données', x = modeles, y = [83.79,81.00,80.75,80.94,80.44,84.42,84.12,84.53,84.48])
                ])
fig_telco2.update_layout(title_text='Résultats Telco Customer Churn sans préparation des données',
                  yaxis_title="Moyenne des AUC en %",)

fig_telco3 = go.Figure(data=[
                go.Bar(name = 'Avec Préparation des données', x = categ, y = [84.36,84.29,84.33]),
                go.Bar(name = 'Sans Préparation des données', x= categ, y =[80.90,83.60,82.72])
                ])
fig_telco3.update_layout(title_text='Résultats Telco Customer Churn',
                  yaxis_title="Moyenne des AUC en %",)


#Credit card
fig_credit = go.Figure(data=[
                go.Bar(name = 'Avec Préparation des données', x = modeles, y = [96.90,97.14,96.73,97.29,95.87,98.38,98.44,98.71,98.91]),
                go.Bar(name = 'Sans Préparation des données', x= modeles, y =[96.60,91.80,98.03,97.83,94.73,97.96,97.74,98.43,98.05])
                ])
fig_credit.update_layout(title_text='Résultats Credit card',
                  yaxis_title="Moyenne des AUC en %",)

fig_credit1 = go.Figure(data=[
                go.Bar(name = 'Avec Préparation de données', x = modeles, y = [96.90,97.14,96.73,97.29,95.87,98.38,98.44,98.71,98.91])
                ])
fig_credit1.update_layout(title_text='Résultats Credit card avec préparation des données',
                  yaxis_title="Moyenne des AUC en %",)

fig_credit2 = go.Figure(data=[
                go.Bar(name = 'Sans Préparation de données', x = modeles, y = [96.60,91.80,98.03,97.83,94.73,97.96,97.74,98.43,98.05])
                ])
fig_credit2.update_layout(title_text='Résultats Credit card sans préparation des données',
                  yaxis_title="Moyenne des AUC en %",)

fig_credit3 = go.Figure(data=[
                go.Bar(name = 'Avec Préparation de données', x = categ, y = [97.05,98.06,97.60]),
                go.Bar(name = 'Sans Préparation de données', x= categ, y =[95.89,97.38,95.89])
                ])
fig_credit3.update_layout(title_text='Résultats Credit card',
                  yaxis_title="Moyenne des AUC en %",)


if base == 'Churn Modelling':
    if len(option)==2:
          st.plotly_chart(fig_churn)
    elif 'Préparation des données (Data cleaning, Feature engineering)' in option:
            st.plotly_chart(fig_churn1)   
    elif 'Sans Préparation' in option :
            st.plotly_chart(fig_churn2)
    if Resume:
            st.plotly_chart(fig_churn3)
elif base == 'Adult':
    if len(option)==2:
          st.plotly_chart(fig_adult)
    elif 'Préparation des données (Data cleaning, Feature engineering)' in option:
            st.plotly_chart(fig_adult1)   
    elif 'Sans Préparation' in option :
            st.plotly_chart(fig_adult2)
    if Resume:
            st.plotly_chart(fig_adult3)
elif base == 'Telco Customer Churn':
    if len(option)==2:
          st.plotly_chart(fig_telco)
    elif 'Préparation des données (Data cleaning, Feature engineering)' in option:
            st.plotly_chart(fig_telco1)   
    elif 'Sans Préparation' in option :
            st.plotly_chart(fig_telco2)
    if Resume:
            st.plotly_chart(fig_telco3)
elif base == 'CreditCard':
    if len(option)==2:
          st.plotly_chart(fig_credit)
    elif 'Préparation des données (Data cleaning, Feature engineering)' in option:
            st.plotly_chart(fig_credit1)   
    elif 'Sans Préparation' in option :
            st.plotly_chart(fig_credit2)
    if Resume:
            st.plotly_chart(fig_credit3)  









    
    


