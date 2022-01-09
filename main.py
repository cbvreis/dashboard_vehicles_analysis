"""
## APP NAME

DESCRIPTION

Author: [Cássio Henrique Resende Reis]
Source: [Github](https://github.com/cbvreis)
"""

import streamlit as st

from controller import chart, processing, data

chart = chart.Chart()
st.set_page_config(layout='wide')


def main():
    df, df_cons = data.load_data()
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
        fig3 = chart.create_box_plot(_temp, 'Weekday', 'Diff Km', 'veh_line_desc',
                                     "Boxplot of quilometrage by Weekdays", {
                                         "Weekday": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday",
                                                     "Sunday"]})
        col3.plotly_chart(fig3)

        # By Cod Vin
        _temp = df[df['veh_line_desc'].isin(vehicle_line)]
        cod_vin = st.multiselect('Select Vin Line', _temp['Cod_Vin'].unique())
        if cod_vin:
            col1, col2, col3 = st.columns(3)

            # Barplot
            _temp = _temp[_temp['Cod_Vin'].isin(cod_vin)]
            fig4 = chart.create_bar_plot(_temp, 'Weekday', 'Diff Km', 'veh_line_desc',
                                         'Barplot of quilometrage by Weekdays', {
                                             "Weekday": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday",
                                                         "Saturday", "Sunday"]})
            col1.plotly_chart(fig4)

            # Matriz
            fig5 = chart.create_matrix(['Line', 'Count Vehicles', 'Avg Km/Day', 'Avg Duration Trip'], _temp,
                                       'veh_line_desc', 'Cod_Vin', 'Diff Km', 'Vel_Media')
            col2.plotly_chart(fig5)

            # Boxplot consumo
            _temp = df[df['veh_line_desc'].isin(vehicle_line)]
            _temp = _temp[(_temp['Km/L'] > 0) & (_temp['Km/L'] < 20)]
            fig6 = chart.create_box_plot(_temp, 'veh_line_desc', 'Km/L', 'veh_line_desc',
                                         "Boxplot of consumption by vehicle line", None)
            col3.plotly_chart(fig6)


if __name__ == "__main__":
    main()
