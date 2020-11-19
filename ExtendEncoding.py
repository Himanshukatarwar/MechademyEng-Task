import pickle
import numpy as np


class ExtendEncoding(object):
    """ Encoding the model features with respective to there manufacture of cars """
    """ Getting unique manufacture of cars and encode model of manufacture cars with unique id 
      Parameters:
  
          Manufacture : - Get the unique id of manufactures
          Total_manufacture_model = Get the max id given to the manufacture's model 
          manuf_encoder_dict = Get the model with unique id 
      return :
            Tranformed data 
  
      """

    def __init__(self):

        with open('requirement/total_manufacture_model.pickle', 'rb') as handle:
            self.total_manufacture_model = pickle.load(handle)
        with open('requirement/manufacture.pickle', 'rb') as handle:
            self.manufacture = pickle.load(handle)
        with open('requirement/make_encoder_dict.pickle', 'rb') as handle:
            self.make_encoder_dict = pickle.load(handle)

    def transform(self, data):
        transform_data = []
        for make, model in zip(data['make'], data['model']):
            try:
                transform_data.append(self.make_encoder_dict[model])
            except:
                self.total_manufacture_model[make] += 1
                transform_data.append(self.total_manufacture_model[make])
        return np.array(transform_data).reshape(-1, 1)
