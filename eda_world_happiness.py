import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

def read(file_name):
    df = pd.read_csv(file_name)
    df.head()

def data_clean(df):
    df.info()
