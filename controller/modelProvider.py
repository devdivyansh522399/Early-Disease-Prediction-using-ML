# pylint: skip-file

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from xgboost import XGBClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.preprocessing import StandardScaler, MinMaxScaler
import warnings

warnings.filterwarnings("ignore", category=FutureWarning)


class models():
    @classmethod
    def diabetesModel(self):
        df = pd.read_csv("cleanData\\diabetes.csv")
        y_resampled = df['Outcome'];
        df = df.drop('Outcome', axis=1)
        X_train, X_test, y_train, y_test = train_test_split(df, y_resampled, test_size=0.2, random_state=42)
        rf_model = RandomForestClassifier(random_state=42)
        rf_model.fit(X_train, y_train)
        return rf_model

    @classmethod
    def heartModel(self):
        df = pd.read_csv("cleanData\\heart.csv")
        y = df['output'];
        Features = df.drop('output', axis=1)
        scaler = MinMaxScaler()
        Norm_data = scaler.fit_transform(Features)
        Norm_df = pd.DataFrame(Norm_data, columns= Features.columns)
        X = Norm_df
        X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.2, random_state=40)
        model = SVC(C= 5, kernel= 'linear', probability=True)
        model.fit(X_train, y_train)
        return model


    @classmethod
    def hepetitisModel(self):
        df = pd.read_csv("cleanData\\hepetitis.csv")
        y_resampled = df['Outcome'];
        Features = df.drop('Outcome', axis=1)
        scaler = MinMaxScaler()
        Norm_data = scaler.fit_transform(Features)
        Norm_df = pd.DataFrame(Norm_data, columns= Features.columns)
        X = Norm_df
        X_train, X_test, y_train, y_test = train_test_split(Norm_df,y_resampled, test_size = 0.2, random_state=40)
        model =  SVC(C= 20, kernel= 'linear', probability=True)
        model.fit(X_train, y_train)
        return model


    @classmethod
    def lungsModel(self):
        try:
            df = pd.read_csv("cleanData\\lungs.csv")
            y = df['Outcome']
            X = df.drop('Outcome', axis=1)
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=40)
            model = LogisticRegression(random_state=0)
            model.fit(X_train, y_train.ravel())
            return model
        except FileNotFoundError:
            print("Error: File not found. Please check the file path and try again.")
        except ValueError as ve:
            print(f"ValueError: {ve}")
        except Exception as e:
            print(f"An error occurred: {e}")

    @classmethod
    def liverModel(self):
        try:
            df = pd.read_csv("cleanData\\liver.csv")
            y = df['Outcome']
            X = df.drop('Outcome', axis=1)
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=40)
            model = XGBClassifier(max_depth=5, random_state=40, n_estimators=10)
            model.fit(X_train, y_train)
            return model
        except FileNotFoundError:
            print("Error: File not found. Please check the file path and try again.")
        except ValueError as ve:
            print(f"ValueError: {ve}")
        except Exception as e:
            print(f"An error occurred: {e}")