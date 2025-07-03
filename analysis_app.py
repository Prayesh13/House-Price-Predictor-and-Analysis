import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from flask import request
import pickle
import numpy as np


df = pickle.load(open("datasets/data.pkl","rb"))
new_df = pd.read_csv("datasets/new_df.csv")
group_df = new_df.groupby('location')[['price','price_per_sqft','built_up_area','latitude','longitude']].mean()


def generate_map():
    fig = px.scatter_mapbox(
        group_df,
        lat='latitude',
        lon='longitude',
        color='price_per_sqft',
        size='built_up_area',
        color_continuous_scale=px.colors.cyclical.IceFire,
        zoom=10,
        size_max=30,
        mapbox_style="open-street-map",
        hover_name=group_df.index
    )

    fig.update_layout(height=700)  

    return fig.to_html(full_html=False)

def scatter_plot_builtup_area_price(selected_category=None):
    # Create the scatter plot with a cold color palette
    luxury_categories = df['luxury_category'].unique()

    # Filter the DataFrame based on the selected category
    if selected_category:
        filtered_df = df[df['luxury_category'] == selected_category]
    else:
        filtered_df = df  # Use full DataFrame if no category is selected

    fig = px.scatter(filtered_df, x='built_up_area', y='price', color='bhk', 
                     title='Area Vs Price', color_continuous_scale='Blues')
    
    fig.update_layout(height=700)

    # Convert Plotly figure to HTML div
    plot_html = fig.to_html(full_html=False)

    # Return as Markup to embed it safely in Jinja2 templates
    return plot_html,luxury_categories

def boxplot_bhk_price(selected_category=None):
    # Get unique luxury categories
    luxury_categories = df['luxury_category'].unique()

    # Filter the DataFrame based on the selected category
    if selected_category:
        filtered_df = df[df['luxury_category'] == selected_category]
    else:
        filtered_df = df  # Use full DataFrame if no category is selected

    # Generate the boxplot using the filtered data
    fig = px.box(filtered_df, x='bhk', y='price', title="BHK vs Price Boxplot", color_discrete_sequence=['#2a9df4'])
    fig.update_layout(height=700)
    boxplot_html = fig.to_html(full_html=False)

    return boxplot_html, luxury_categories


def bhk_pie(selected_category=None):
    # Get unique luxury categories
    location = df['location'].unique()

    # Filter the DataFrame based on the selected category
    if selected_category:
        filtered_df = df[df['luxury_category'] == selected_category]
    else:
        filtered_df = df

    fig = px.pie(df, names='bhk', title='BHK Distribution by Location')
    fig.update_layout(height=700)
    pie_html = fig.to_html(full_html=False)

    return pie_html, location


def dist_price():
    price_data = df['price']

    fig = px.histogram(price_data, nbins=50, opacity=0.7, histnorm='density', title='Distribution of Price')
    fig.update_traces(marker_color='lightskyblue', marker_line_color='black', marker_line_width=1.2)

    fig.update_layout(
        xaxis_title="Price",
        yaxis_title="Density",
        height=700,
        template="plotly_white"
    )

    # fig.update_layout(height=700)
    dist_html = fig.to_html(full_html=False)

    return dist_html