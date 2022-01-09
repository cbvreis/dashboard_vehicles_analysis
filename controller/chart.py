import plotly.express as px
import plotly.graph_objects as go


class Chart:
    def create_box_plot(self, df, x, y, color, title, category_orders):
        '''
        Funtion to create box plot
        :param df:
        :param x:
        :param y:
        :param color:
        :param title:
        :param category_orders:
        :return:
        '''
        fig = px.box(df, x=x,
                     y=y,
                     color=color,
                     color_discrete_sequence=px.colors.qualitative.Dark24,
                     category_orders=category_orders,
                     title=title)
        return fig

    def create_bar_plot(self, df, x, y, color, title, category_orders):
        '''
        Function to create bar plot
        :param df:
        :param x:
        :param y:
        :param color:
        :param title:
        :param category_orders:
        :return:
        '''
        fig = px.bar(df, x=x,
                     y=y,
                     color=color,
                     barmode='group',
                     color_discrete_sequence=px.colors.qualitative.Dark24,
                     category_orders=category_orders,
                     title=title)
        return fig

    def create_matrix(self, values, df, filter, x1, x2, x3):
        '''
        Function to create matrix plot
        :param values:
        :param df:
        :param filter:
        :param x1:
        :param x2:
        :param x3:
        :return:
        '''
        fig = go.Figure(data=[go.Table(header=
                                       dict(values=values,
                                            fill_color='grey',
                                            font=dict(color='Black', size=16),
                                            align='left')
                                       ,
                                       cells=dict(values=[
                                           df.groupby(filter)[x1].nunique().index.to_list(),
                                           df.groupby(filter)[x1].nunique().to_list(),
                                           df.groupby(filter).agg({x2: 'mean'}).round(2),
                                           df.groupby(filter).agg({x3: 'mean'}).round(2),
                                       ],
                                           fill_color='lightgrey',
                                           font=dict(color='Black', size=16),
                                           align='left')
                                       )
                              ])
        return fig
