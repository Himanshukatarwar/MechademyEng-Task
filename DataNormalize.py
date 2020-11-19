import pickle

class Normalize():
    def __init__(self):
        with open('supporting file/Normalize.pkl', 'rb') as handle:
            self.normalize= pickle.load(handle)
    def transform(self,data,state = 'GTCOMP'):
        data = data.dropna()
        data = data.drop(['GT Compressor inlet air temperature (T1) [C]','GT Compressor inlet air pressure (P1) [bar]','Ship speed (v) [knots]'
                            ,'Starboard Propeller Torque (Ts) [kN]','HP Turbine exit pressure (P48) [bar]'],axis= 1)
        if state != 'GTCOMP':
            data = self.normalize.transform(data)
        return data
