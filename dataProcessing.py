from ExtendEncoding import ExtendEncoding
from Normalize import Normalize
import pickle
import numpy as np

class ProcessData(object):
    def __init__(self):
        self.colorEncoding = self.openPickle_file("requirement/colorEncoding.pkl")
        self.conditionEncoding = self.openPickle_file("requirement/conditionEncoding.pkl")
        self.drive_unitEncoding = self.openPickle_file("requirement/drive_unitEncoding.pkl")
        self.ExtendEncoding = ExtendEncoding()
        self.fuel_typeEncoding = self.openPickle_file("requirement/fuel_typeEncoding.pkl")
        self.makeEncoding = self.openPickle_file("requirement/makeEncoding.pkl")
        self.segmentEncoding = self.openPickle_file("requirement/segmentEncoding.pkl")
        self.transmissionEncoding = self.openPickle_file("requirement/transmissionEncoding.pkl")
        self.Normalize = Normalize()

    def openPickle_file(self, path):
        with open(path, 'rb') as f:
            file = pickle.load(f)
        return file

    def transform_data(self, data):
        data = data.dropna()
        if data.shape[1] != 11:
            print("ERROR DATA SHAPE IS NOT MATCH")
            return
        encodedColor = self.colorEncoding.transform(np.array(data['color']).reshape(-1, 1))
        encodedcondition = self.conditionEncoding.transform(np.array(data['condition']).reshape(-1, 1))
        encodeddriveU = self.drive_unitEncoding.transform(np.array(data['drive_unit']).reshape(-1, 1))
        encodedmodel = self.ExtendEncoding.transform(data[['make', 'model']])
        encodedfuel = self.fuel_typeEncoding.transform(np.array(data['fuel_type']).reshape(-1, 1))
        encodedmake = self.makeEncoding.transform(np.array(data['make']).reshape(-1, 1))
        encodedsegment = self.segmentEncoding.transform(np.array(data['segment']).reshape(-1, 1))
        encodedtrans = self.transmissionEncoding.transform(np.array(data['transmission']).reshape(-1, 1))
        encodedMileage = self.Normalize.transform_Mileage(data['mileage(kilometers)'])
        encodedVolume = self.Normalize.transform_Volume(data['volume(cm3)'])
        year = np.array(data['year']).reshape(-1, 1)


        preprocessed_data = np.hstack((encodedmake, encodedmodel, encodedMileage, encodedVolume, year,
                                       encodedcondition, encodedColor, encodedtrans, encodedfuel,
                                       encodeddriveU, encodedsegment))
        return preprocessed_data
