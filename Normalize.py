import numpy as np
class Normalize(object):


    def transform_Mileage(self, data):
        """ Return transformed data Mileage """
        Mileagemax = 9999999.0
        Mileagemin = 0.0
        return np.array(((data - Mileagemin) / (Mileagemax - Mileagemin))).reshape(-1,1)
    def transform_Volume(self,data):
        """  Return Transformed data for Volume """

        Volumemax = 20000.0
        Volumemin = 500.0
        return np.array(((data - Volumemin) / (Volumemax - Volumemin))).reshape(-1,1)
