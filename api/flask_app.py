from flask import Flask, request
import model
import pickle
import requests 
import numpy as np

# ML Imports
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression


# load the model from disk
filename = 'model/final_model.sav'

classifier_model = pickle.load(open(filename, 'rb'))

with open('model/scaler.pkl','rb') as f:
    sc = pickle.load(f)


# loaded_model.predict()
# print(result)

app = Flask(__name__)

@app.route('/api/risk', methods=['POST'])
def riskPredictor() -> bool:
    data = request.get_json() # Get data posted as a json
    if not data:
        return "Bad Request", 400
    else:
        features = [
                    'ExternalRiskEstimate', 
                    'MSinceOldestTradeOpen',
                    'MSinceMostRecentTradeOpen',
                    'AverageMInFile',
                    'NumSatisfactoryTrades',
                    'NumTrades60Ever2DerogPubRec',
                    'NumTrades90Ever2DerogPubRec',
                    'PercentTradesNeverDelq',
                    'MSinceMostRecentDelq',
                    'MaxDelq2PublicRecLast12M',
                    'MaxDelqEver',
                    'NumTotalTrades',
                    'NumTradesOpeninLast12M',
                    'PercentInstallTrades',
                    'MSinceMostRecentInqexcl7days',
                    'NumInqLast6M',
                    'NumInqLast6Mexcl7days',
                    'NetFractionRevolvingBurden',
                    'NetFractionInstallBurden',
                    'NumRevolvingTradesWBalance',
                    'NumInstallTradesWBalance',
                    'NumBank2NatlTradesWHighUtilization',
                    'PercentTradesWBalance'
                    ]

        values = np.array([data.get(feature, 0.0) for feature in features])
        scaled_values =  sc.transform( [values] )
        return str(classifier_model.predict(scaled_values)), 200

if __name__ == '__main__':
    app.run()