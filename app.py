from flask import Flask, request, render_template
import pandas as pd

app = Flask(__name__)

data = pd.read_excel('data.xlsx')


@app.route('/')
def home():
	return render_template('index.html')


@app.route('/search', methods=['GET'])
def search():
	query = request.args.get('query', '').lower()
	results = data[data['Name'].str.lower().str.contains(query)]
	return render_template('index.html', query=query, results=results.to_dict(orient='records'))


if __name__ == '__main__':
	app.run(debug=True)
