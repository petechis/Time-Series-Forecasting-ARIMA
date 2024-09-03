'''Import Libraries: 
    pandas, 
    statsmodels, 
    warnings, 
    relativedelta 
    from dateutil, and streamlit. '''

import pandas as pd
import statsmodels.api as sm
import warnings
from dateutil.relativedelta import relativedelta
import streamlit as st

class SalesPredictor:

    ''' A class for Time series forecasting, a technique that leverages historical
        data to predict future values, e.g. decision-making, resource allocation 
        and risk management.'''

    warnings.filterwarnings("ignore")

    # Configuring the layout of the page as "wide".
    st.set_page_config(layout="wide")

    def __init__(self):

        # Class attribute initialising by reading sales data from a CSV file.
        self.sales_df=pd.read_csv('car-part-sales.csv')

        # Setting up the list of unique products and sellers.
        self.products = list(set(self.sales_df['Product'].tolist()))
        self.sellers = list(set(self.sales_df['Seller'].tolist()))

        # Converting the 'Date' column to a datetime format.
        self.sales_df['Date'] = pd.to_datetime(self.sales_df['Date'])

    def forecast_arima(self, product, seller):
        '''ARIMA Forecasting Method defining the procedures 
           taking a product and seller as inputs.'''

        # Filtering the sales data for the selected product and seller.
        subset = self.sales_df[(self.sales_df['Product'] == product) & (self.sales_df['Seller'] == seller)]
        time_series = pd.Series(subset['Sales'].values, index=subset['Date'])

        # Creating a time series from the filtered sales data.
        last_month = time_series.index[len(time_series) - 1]        
        last_month = last_month + relativedelta(months=1)    
        model = sm.tsa.ARIMA(time_series, order=(2, 1, 1))
        model_fit = model.fit()

        # Using the ARIMA (AutoRegressive Integrated Moving Average) model to forecast sales for the next 3 month.
        forecast_steps = 3
        forecast = model_fit.forecast(steps=forecast_steps)
        dates = pd.date_range(start=last_month, periods=forecast_steps, freq='M')

        date_pred = [date.strftime('%m-%y') for date in dates]        
        seller_pred = [seller] * forecast_steps
        product_pred = [product] * forecast_steps

        # Returning lists of formatted dates, seller names, product names, and forecasted sales values.
        return date_pred, seller_pred, product_pred, forecast.tolist()
    
    def run(self):

        '''This method sets up the Streamlit web application.'''

        # write simple text    
        st.warning("Go ahead and SELECT a PRODUCT / SELLER on the sidebar: Predicted sales for next 3 months will appear here!")

        # The sidebar for user input controls for selecting a product and a seller. 
        col_table, col_graph = st.columns(2)          
        with st.sidebar:
            st.image('arima_image.png')
            st.subheader("ARIMA-Time Series Forecasting")
            st.divider()
            
            selected_product = st.selectbox("Select a product", self.products)
            st.divider()
            selected_seller = st.selectbox("Select a seller", self.sellers)

            # If the “Make Prediction” button is clicked, the forecast_arima method is called to generate forecasts.
            if st.button("Make Prediction"):
                date_pred, seller_pred, product_pred, forecast_pred = self.forecast_arima(selected_product,
                                                                                          selected_seller)
                forecast_pred = [int(item) for item in forecast_pred]  
                predicted_dataframe = pd.DataFrame({
                    "Date": date_pred,
                    "Product": product_pred,
                    "Seller": seller_pred,
                    "Forecast": forecast_pred
                })
               
                col_graph.subheader('Chart showing sales predictions.')
                predicted_dataframe = predicted_dataframe.sort_values(by='Date', ascending=True)
                
                # This function displays forecasts as a line chart in the main content area.
                col_graph.line_chart(
                    predicted_dataframe,
                    use_container_width=True,
                    height=200,
                    x='Date',
                    y='Forecast'               
                ) 
                st.divider()                
                st.success("We done! App showcasing forecasting sales using ARIMA.")  
                st.write(":green[Implemented By Pete Chisamba.]")               

                # The table shows the forecast data.
                col_table.subheader('Predicted product sales per Seller.')
                col_table.write(predicted_dataframe)     
               
# The code block checking if the script is being run as the main program.
if __name__ == "__main__":
    
    # Creating an instance of the class, and calling the run() method to start the Streamlit app.
    predictor = SalesPredictor()    
    predictor.run()
   
    
