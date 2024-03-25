from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Load the Excel file into a DataFrame
df = pd.read_excel('books_database.xlsx')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    query = request.form['query']
    
    # Filter the DataFrame based on the query
    results = df[df['Book Name'].str.contains(query, case=False) |
                 df['Author Name'].str.contains(query, case=False) |
                 df['Subject'].str.contains(query, case=False)]
    
    return render_template('results.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)
