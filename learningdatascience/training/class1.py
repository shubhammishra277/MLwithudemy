import pandas as pd
import numpy as np
from configparser import ConfigParser
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer 
from commonutilities.loggermodule import loggerfunc

class dataprocessing(object):
    
    def __init__(self):
        self.confreader()
        loggerobj=loggerfunc(self.level)
        self.logger=loggerobj.logger()
        self.data=pd.read_csv(self.input_path)

        
    def confreader(self):
        parser=ConfigParser()
        parser.read('/home/fractaluser/learningdatascience/training/config_files/global_config.ini')
        self.level=parser["COMMON"]["Logging_level"]
        self.test_split=parser["COMMON"]["test_split"]
        self.input_path=parser["COMMON"]["input_path"]
        
        
    def independent_dependentvar(self):
        collist=list(self.data)
        X=self.data.iloc[:,:-1].values
        Y=self.data.iloc[:,3].values
        self.logger.info("list of dependent variables : %s"%str(collist[:-1]))
        self.logger.info("independent variable: %s"%str(collist[3]))
        return(X,Y)
        
        
    def missingvalueremoval(self):
        X,Y=self.independent_dependentvar()
        imputer=SimpleImputer(missing_values=np.nan,strategy="mean")
        X[:,1:3]=imputer.fit_transform(X[:,1:3])
        return(X,Y)
        
    def categoricaldatahandle(self):
        X,Y=self.missingvalueremoval()
        labelencoder_x=LabelEncoder()
        X[:,0]=labelencoder_x.fit_transform(X[:,0])
        onehotencoder=OneHotEncoder(categorical_features=[0])
        X=onehotencoder.fit_transform(X).toarray()
        labelencoder_y=LabelEncoder()
        Y=labelencoder_y.fit_transform(Y)
        return(X,Y)
        
    def featurescaling(self):
        X,Y=self.categoricaldatahandle()
        sc_X=StandardScaler()
        X=sc_X.fit_transform(X)
        return(X,Y)
        
    def train_testsplit_generate(self):
        X,Y=self.featurescaling()
        X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=float(self.test_split),random_state=42)
        return(X_train,X_test,Y_train,Y_test)
        
        
if __name__=="__main__":
      dataprocobj=dataprocessing()
      X_train,X_test,Y_train,Y_test=dataprocobj.train_testsplit_generate()
      
    
        
    
        
        
        
        
        
        
        
        
        
