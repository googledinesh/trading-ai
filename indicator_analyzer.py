# indicator_analyzer.py
import pandas as pd
import numpy as np

class IndicatorAnalyzer:
    def __init__(self, data: pd.DataFrame):
        self.data = data
    
    def calculate_moving_average(self, period: int):
        return self.data['Close'].rolling(window=period).mean()

    def generate_signals(self):
        signals = []
        for i in range(len(self.data)):
            if (self.data['Close'][i] > self.calculate_moving_average(50)[i]):
                signals.append('Buy')
            elif (self.data['Close'][i] < self.calculate_moving_average(50)[i]):
                signals.append('Sell')
            else:
                signals.append('Hold')
        return signals

    def run_analysis(self):
        self.data['Signals'] = self.generate_signals()
        return self.data

# Example usage:
# df = pd.read_csv('path_to_your_data.csv')
# analyzer = IndicatorAnalyzer(df)
# results = analyzer.run_analysis()
# print(results)