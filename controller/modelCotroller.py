# pylint: skip-file
import joblib
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
import random
from controller.modelProvider import models
class ControllerModel():

    @classmethod
    def DiabetesPredictor(self,to_predict):
        try:
            if len(to_predict[0]) == 8:
                loaded_model = models.diabetesModel()
                res = loaded_model.predict(to_predict)
                probabilty = loaded_model.predict_proba(to_predict)
                result=[]
                print(probabilty)
                result.append(res[0])
                result.append(probabilty)
                return result
            else:
                raise ValueError("Invalid size. Expected size is 8.")
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    @classmethod
    def KidneyPredictor(self, to_predict,size):
        try:
            if size == 24:
                loaded_model = joblib.load("pklfiles\\Kidney.pkl")
                res = loaded_model.predict(to_predict)
                probabilty = loaded_model.predict_proba(to_predict)
                result=[]
                result.append(res[0])
                result.append(probabilty)
                return result
            else:
                raise ValueError("Invalid size. Expected size is 8.")
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    @classmethod
    def LiverPredictor(self, to_predict,size):
            try:
                if size == 9:
                    loaded_model = models.liverModel()
                    print(loaded_model)
                    scaler = StandardScaler()
                    scaler.fit(to_predict)
                    new_list = scaler.transform(to_predict)
                    res = loaded_model.predict(new_list)
                    probabilty = loaded_model.predict_proba(new_list)
                    result=[]

                    if(res[0]==2):
                        res[0] = 0
                    result.append(res[0])
                    result.append(probabilty)
                    print(result)
                    return result
                else:
                    raise ValueError("Invalid size. Expected size is 9.")
            except Exception as e:
                print(f"An error occurred: {e}")
                return []

    @classmethod
    def HepetitisPredictor(self, to_predict,size):
            try:
                if size == 12:
                    loaded_model = models.hepetitisModel()
                    scaler = MinMaxScaler()
                    new_list = scaler.fit_transform(to_predict)
                    res = loaded_model.predict(new_list)
                    probabilty = loaded_model.predict_proba(new_list)
                    print(probabilty)
                    result=[]
                    result.append(res[0])
                    result.append(probabilty)
                    return result
                else:
                    raise ValueError("Invalid size. Expected size is 12.")
            except Exception as e:
                print(f"An error occurred: {e}")
                return None

    @classmethod
    def lungsPredictor(self, to_predict, size):
        try:
            if size == 13:
                loaded_model = models.lungsModel()
                res = loaded_model.predict(to_predict)
                probabilty = loaded_model.predict_proba(to_predict)
                result=[]
                print(probabilty)
                result.append(res[0])
                result.append(probabilty)
                print(result)
                return result
            else:
                raise ValueError("Invalid size. Expected size is 12.")
        except Exception as e:
            print(f"An error occurred in controller: {e}")
            return None

    @classmethod
    def HeartPredictor(self, to_predict,size):
            try:
                if size == 13:
                    loaded_model = models.heartModel()
                    scaler = MinMaxScaler()
                    new_list = scaler.fit_transform(to_predict)
                    res = loaded_model.predict(new_list)
                    probabilty = loaded_model.predict_proba(new_list)
                    result=[]
                    print(probabilty)
                    result.append(res[0])
                    result.append(probabilty)
                    return result
                else:
                    raise ValueError("Invalid size. Expected size is 13.")
            except Exception as e:
                print(f"An error occurred: {e}")
                return None