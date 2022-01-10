"""
## APP NAME

DESCRIPTION

Author: [Cássio Henrique Resende Reis]
Source: [Github](https://github.com/cbvreis)
"""
import pandas as pd
import streamlit as st
from controller import chart, processing, data
import plotly.graph_objects as go
import numpy as np

chart = chart.Chart()
st.set_page_config(layout='wide')


def main():
    #df, df_cons = data.load_data()
    df = data.load_data()
    df = processing.process_data(df)

    st.title('Trip Analysis')
    st.markdown('### Explore the data')
    if st.checkbox('Show data'):
        st.write(df)
    st.markdown('### Boxplot of quilometrage by weekdays')
    vehicle_line = st.multiselect('Select Vehicle Line', df['veh_line_desc'].unique())
    if vehicle_line:
        col1, col2, col3 = st.columns(3)

        _temp = df[df['veh_line_desc'].isin(vehicle_line)]
        fig1 = chart.create_box_plot(_temp, 'Month', 'Diff Km', 'veh_line_desc', 'Boxplot of quilometrage by Months',
                                     {"Month": ["January", "February", "March", "April", "May", "June", "July",
                                                "August", "September", "October", "November", "December"]})
        col1.plotly_chart(fig1)

        # By weekyear
        _temp = df[df['veh_line_desc'].isin(vehicle_line)]
        fig2 = chart.create_box_plot(_temp, 'Weekyear', 'Diff Km', 'veh_line_desc',
                                     "Boxplot of quilometrage by Weekyear", {"Weekyear": list(range(244))})
        col2.plotly_chart(fig2)

        # By weekdays
        _temp = df[df['veh_line_desc'].isin(vehicle_line)]
        _temp.groupby('Weekday').agg({'Diff Km': 'sum'})
        fig3 = chart.create_box_plot(_temp, 'Weekday', 'Diff Km', 'veh_line_desc',
                                     "Boxplot of quilometrage by Weekdays", {
                                         "Weekday": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday",
                                                     "Sunday"]})
        col3.plotly_chart(fig3)

        st.markdown('---')
        col1, col2, col3 = st.columns(3)

        # Barplot
        fig4 = chart.create_bar_plot(_temp, 'Weekday', 'Diff Km', 'veh_line_desc',
                                     'Barplot of quilometrage by Weekdays', {
                                         "Weekday": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday",
                                                     "Saturday", "Sunday"]})
        col1.plotly_chart(fig4)
        # Matriz
        fig5 = chart.create_matrix(['Line', 'Count Vehicles', 'Avg Km/Day', 'Avg Duration Trip'], df,
                                   'veh_line_desc', 'Cod_Vin', 'Diff Km', 'Vel_Media')
        col3.plotly_chart(fig5)

        # Boxplot consumo
        _temp = _temp[(_temp['Km/L'] > 0) & (_temp['Km/L'] < 20)]
        fig6 = chart.create_box_plot(_temp, 'veh_line_desc', 'Km/L', 'veh_line_desc',
                                     "Boxplot of consumption by vehicle line", None)
        col2.plotly_chart(fig6)



        # By Cod Vin
        cod_vin = st.multiselect('Select Vin Line', _temp['Cod_Vin'].unique())
        if cod_vin:
            col1, col2, col3 = st.columns(3)

            # Lineplot
            _temp = _temp[_temp['Cod_Vin'].isin(cod_vin)]
            fig7 = chart.create_line_plot(_temp, 'Data','Odometro_final','Cod_Vin','Lineplot of quilometrage by Vin')


            col1.plotly_chart(fig7)

            # Map
            cols=['Latitude_inicial','Longitude_inicial']
            _=_temp[cols]
            _.columns=['latitude','longitude']
            col2.text('Map of trips by Vin')
            col2.map(_.dropna())

            # Boxplot consumo


            _temp = _temp[_temp['Cod_Vin'].isin(cod_vin)]
            _temp = _temp[(_temp['Km/L'] > 0) & (_temp['Km/L'] < 20)]
            fig = go.Figure(data=[go.Table(header=
                                           dict(values=['Vin','Line', 'Avg Consumption Line(Km/L)', 'Avg Consumption Vin(Km/L)'],
                                                fill_color='grey',
                                                font=dict(color='Black', size=16),
                                                align='left')
                                           ,
                                           cells=dict(values=[
                                               _temp.groupby('Cod_Vin')['veh_line_desc'].nunique().index.to_list(),
                                               _temp.groupby('Cod_Vin')['veh_line_desc'].unique(),
                                               np.round(df[df['veh_line_desc'].isin(vehicle_line)].groupby('veh_line_desc')['Km/L'].median(),2),
                                               np.round(_temp.groupby('Cod_Vin')['Km/L'].mean().to_list(),2)


                                           ],
                                               fill_color='lightgrey',
                                               font=dict(color='Black', size=16),
                                               align='left')
                                           )
                                  ])
            col3.plotly_chart(fig)



if __name__ == "__main__":
    main()
