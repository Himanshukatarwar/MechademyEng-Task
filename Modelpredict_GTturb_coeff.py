from DataNormalize import Normalize
from joblib import load
class Model(object):
    def __init__(self):
        self.normalize = Normalize()
        self.model = load('TrainedModel/TaskA_bestmodel.joblib')
    def predict(self,data):
        data = Normalize().transform(data,'GTturb')
        return self.model.predict(data)


