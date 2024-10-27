
from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

# Datos de ejemplo
data = {
    'Column 1': [1, 2, 3, 4],
    'Column 2': [10, 20, 30, 40]
}
df = pd.DataFrame(data)

@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(df.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)
