import dataProcessing
from joblib import load



class Model(object):

    def __init__(self):
        self.process_data = dataProcessing.ProcessData()

    def predict(self, data):
        process_data = self.process_data.transform_data(data)
        model = load('TrainedModel/carpriceprediction_model.joblib')
        return model.predict(process_data)
