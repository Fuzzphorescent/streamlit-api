from flask import Flask, jsonify
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

app = Flask(__name__)

# Load data
data = pd.read_csv('output.csv')

# Create static directory for saving plots
if not os.path.exists('static'):
    os.makedirs('static')

# Route to generate Price vs. Age scatter plot
@app.route('/api/plot/age-vs-price', methods=['GET'])
def plot_age_vs_price():
    brand_selected = 'Toyota'  # Default brand; replace as needed
    model_selected = 'Corolla'  # Default model; replace as needed

    data_filtered = data[(data['brand'] == brand_selected) & (data['model'] == model_selected)]
    
    fig, ax = plt.subplots()
    sns.scatterplot(x='age', y='price', data=data_filtered, ax=ax)
    plt.title(f'Price Trend Over Age for {brand_selected} {model_selected}')
    
    # Save the plot as an image
    plot_path = 'static/age_vs_price.png'
    plt.savefig(plot_path)
    
    # Clear the figure after saving
    plt.clf()
    
    return jsonify({'image_url': f'/static/age_vs_price.png'})

# Route to generate Price vs. Model box plot
@app.route('/api/plot/model-vs-price', methods=['GET'])
def plot_model_vs_price():
    brand_selected = 'Toyota'  # Default brand; replace as needed

    same_brand_data = data[data['brand'] == brand_selected]
    
    fig, ax = plt.subplots()
    sns.boxplot(x='price', y='model', data=same_brand_data, ax=ax)
    plt.title(f'Price Distribution Across Models for {brand_selected}')
    
    # Save the plot as an image
    plot_path = 'static/model_vs_price.png'
    plt.savefig(plot_path)
    
    # Clear the figure after saving
    plt.clf()

    return jsonify({'image_url': f'/static/model_vs_price.png'})

# Route to generate Price vs. Kilometers scatter plot
@app.route('/api/plot/km-vs-price', methods=['GET'])
def plot_km_vs_price():
    brand_selected = 'Hyundai'  # Default brand; replace as needed
    model_selected = 'i20'  # Default model; replace as needed

    data_filtered = data[(data['brand'] == brand_selected) & (data['model'] == model_selected)]
    
    fig, ax = plt.subplots()
    sns.scatterplot(x='km', y='price', data=data_filtered, ax=ax)
    sns.regplot(x='km', y='price', data=data_filtered, scatter=False, ax=ax, color='red', ci=None)
    plt.title(f'Price vs. Kilometers Driven for {brand_selected} {model_selected}')
    
    # Save the plot as an image
    plot_path = 'static/km_vs_price.png'
    plt.savefig(plot_path)
    
    # Clear the figure after saving
    plt.clf()

    return jsonify({'image_url': f'/static/km_vs_price.png'})

# Route to calculate average price
@app.route('/api/average-price', methods=['GET'])
def average_price():
    brand_selected = 'Hyundai'  # Default brand; replace as needed
    model_selected = 'i20'  # Default model; replace as needed

    data_filtered = data[(data['brand'] == brand_selected) & (data['model'] == model_selected)]
    avg_price = int(round(data_filtered['price'].mean(), -3))

    return jsonify({'average_price': avg_price})

if __name__ == '__main__':
    app.run(debug=True)
