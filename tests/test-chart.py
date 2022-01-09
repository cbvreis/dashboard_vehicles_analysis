import unittest
import pandas as pd
from controller.chart import Chart
from sklearn.datasets import load_iris
import plotly


class TestBoxPlot(unittest.TestCase):
    def test_box_plot(self):
        chart = Chart()
        #convert load_iris to dataframe pandas
        data = load_iris()
        df = pd.DataFrame(data=data.data, columns=data.feature_names)
        fig = chart.create_box_plot(df, 'sepal length (cm)', 'sepal length (cm)','sepal length (cm)','Iris Dataset', None)
        self.assertEqual(fig, plotly.graph_objs._figure.Figure)