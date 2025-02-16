from flask import Flask,render_template,redirect,url_for,request
import pickle
import numpy as np
from price_prediction import price_predictor
from analysis_app import (
    generate_map,
    scatter_plot_builtup_area_price,
    boxplot_bhk_price,
    bhk_pie,
    dist_price
    )
import joblib


with open('Model/pipeline_xgb.pkl', 'rb') as file:
    pipeline_xgb = pickle.load(file)

# pipeline_xgb = joblib.load("pipeline_xgb.joblib")

df = joblib.load('datasets/data.joblib')


unique_values = {col: df[col].unique().tolist() for col in ['location', 'transaction', 'status', 'furnishing', 'facing', 'floor_category', 'luxury_category']}


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/analysis")
def analysis():
    return render_template("analysis.html")


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        location = request.form['location']
        bhk = int(request.form['bhk'])
        built_up_area = int(request.form['built_up_area'])
        transaction = request.form['transaction']
        status = request.form['status']
        totalfloor = int(request.form['totalfloor'])
        furnishing = request.form['furnishing']
        facing = request.form['facing']
        bathroom = int(request.form['bathroom'])
        floor_category = request.form['floor_category']
        luxury_category = request.form['luxury_category']

        low, high = price_predictor(location, bhk, built_up_area, transaction, status,
                                    totalfloor, furnishing, facing, bathroom, floor_category, luxury_category)

        return render_template('price_prediction.html', low=low, high=high, unique_values=unique_values)

    return render_template('price_prediction.html', unique_values=unique_values)


@app.route("/geo_map_analysis")
def geo_map_analysis():
    return render_template("geo_map_analysis.html", graph_html=generate_map())

@app.route("/scatter_analysis")
def scatter_analysis():
    selected_category = request.args.get('luxury_category')

    scatter_html, luxury_categories = scatter_plot_builtup_area_price(selected_category)
    return render_template("scatter_analysis.html", scatter_html=scatter_html,
                           luxury_categories=luxury_categories,selected_category=selected_category)

@app.route("/boxplot_analysis")
def boxplot_analysis():
    # Get the luxury_category from the query parameters
    selected_category = request.args.get('luxury_category')

    # Generate the boxplot and get unique luxury categories for the dropdown
    boxplot_html, luxury_categories = boxplot_bhk_price(selected_category)

    # Render template with boxplot and dropdown options
    return render_template(
        "boxplot_analysis.html",
        boxplot_html=boxplot_html,
        luxury_categories=luxury_categories,
        selected_category=selected_category
    )

@app.route("/bhk_pie_analysis")
def bhk_pie_analysis():
    selected_category = request.args.get('location')

    # Generate the boxplot and get unique luxury categories for the dropdown
    pie_html, location = bhk_pie(selected_category)

    # Render template with boxplot and dropdown options
    return render_template(
        "bhk_pie_analysis.html",
        pie_html=pie_html,
        location=location,
        selected_category=selected_category
    )

@app.route("/dist_analysis")
def dist_analysis():
    return render_template("dist_analysis.html", dist_html=dist_price())

if __name__ == "__main__":
    app.run(debug=True)
