import pandas as pd
import matplotlib.pyplot as plt

class SalesAnalysis:
    def __init__(self, filepath):
        self.filepath = filepath

    def load_data(self):
        """Loads sales data from a CSV file."""
        return pd.read_csv(self.filepath)

    def total_sales_per_month(self, data):
        """Calculates and returns total sales per month."""
        data['Date'] = pd.to_datetime(data['Date'])
        data['Month'] = data['Date'].dt.month
        monthly_sales = data.groupby('Month')['Sales'].sum()
        return monthly_sales

    def plot_sales_trends(self, sales_data):
        """Plots the sales trends over months."""
        sales_data.plot(kind='bar', figsize=(10, 6), color='skyblue')
        plt.title('Total Sales Per Month')
        plt.xlabel('Month')
        plt.ylabel('Sales')
        plt.xticks(range(len(sales_data.index)), ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], rotation='horizontal')
        plt.show()

if __name__ == "__main__":
    filepath = 'sales_data.csv'
    sales_analysis = SalesAnalysis(filepath)
    data = sales_analysis.load_data()
    monthly_sales = sales_analysis.total_sales_per_month(data)
    sales_analysis.plot_sales_trends(monthly_sales)
