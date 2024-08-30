import pandas as pd
import numpy as np

class ReturnsCalculator:
    
    def __init__(self, df, asset_column, date_column, price_column):
        self.df = df
        self.asset_column = asset_column
        self.date_column = date_column
        self.price_column = price_column

    def cagr(self):        
        self.df = self.df.sort_values(by = [self.asset_column,self.date_column])
        
        self.df = self.df.groupby(self.asset_column).agg(start_date = (self.date_column,'first'), end_date = (self.date_column,'last'),
                                                        start_value = (self.price_column,'first'),
                                                        end_value = (self.price_column,'last')).reset_index()   

        self.df['period'] = (self.df['end_date'] - self.df['start_date']).dt.days / 365        
        self.df['CAGR'] = ((self.df['end_value']/self.df['start_value']) ** (1/self.df['period']) - 1) * 100
        
        return self.df[[self.asset_column, 'CAGR', 'start_date', 'end_date']]
        
    
    def absreturn(self):
        self.df = self.df.sort_values(by = [self.asset_column,self.date_column])
        
        self.df = self.df.groupby(self.asset_column).agg(start_date = (self.date_column,'first'), end_date = (self.date_column,'last'),
                                                        start_value = (self.price_column,'first'),
                                                        end_value = (self.price_column,'last')).reset_index()
        
        self.df['AbsoluteReturn'] = ((self.df['end_value']/self.df['start_value']) - 1) * 100
        
        return self.df[[self.asset_column, 'AbsoluteReturn', 'start_date', 'end_date']]

    def cyreturn(self):
        self.df = self.df.sort_values(by = [self.asset_column,self.date_column])
        self.df['Period'] = self.df[self.date_column].dt.year
        self.df = self.df.groupby([self.asset_column,'Period']).agg(end_value = (self.price_column,'last')).reset_index()
        self.df['start_value'] = self.df['end_value'].shift(1)
        self.df['Return'] = ((self.df['end_value']/self.df['start_value']) - 1) * 100
        
        return self.df[[self.asset_column, 'Period', 'Return']]

    def _calculatefyperiod(self, date):
        if date.month < 4:
            return f"FY{date.year}"
        else:
            return f"FY{date.year + 1}"

    def fyreturn(self):
        self.df = self.df.sort_values(by = [self.asset_column,self.date_column])
        self.df['Period'] = self.df[self.date_column].apply(self._calculatefyperiod)
        
        self.df = self.df.groupby([self.asset_column,'Period']).agg(end_value = (self.price_column,'last')).reset_index()
        self.df['start_value'] = self.df['end_value'].shift(1)
        self.df['Return'] = ((self.df['end_value']/self.df['start_value']) - 1) * 100
        
        return self.df[[self.asset_column, 'Period', 'Return']]

    def monthlyreturn(self):
        self.df = self.df.sort_values(by = [self.asset_column,self.date_column])
        self.df['Period'] = pd.to_datetime(self.df[self.date_column]).dt.to_period('M')
        
        self.df = self.df.groupby([self.asset_column,'Period']).agg(end_value = (self.price_column,'last')).reset_index()
        self.df['start_value'] = self.df['end_value'].shift(1)
        self.df['Return'] = ((self.df['end_value']/self.df['start_value']) - 1) * 100
        
        return self.df[[self.asset_column, 'Period', 'Return']]
