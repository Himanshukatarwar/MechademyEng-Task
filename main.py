import pandas as pd
from  Modelpredict_GTturb_coeff import Model

if __name__ == "__main__":
    df = pd.read_csv('propulsion.csv')
    df = df.drop(['GT Compressor decay state coefficient.','Unnamed: 0','GT Turbine decay state coefficient.'], axis=1)
    print(df.columns)
    model = Model()
    print(model.predict(df))

