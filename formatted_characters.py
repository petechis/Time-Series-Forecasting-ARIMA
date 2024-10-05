import streamlit as st

# constant Variables
star_and_space = '&#x2605;&nbsp;'
square_bullet_point0 ='&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&#x2751'
square_bullet_point1 = '&#x2751;&nbsp;'
circke_bullet_point = '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&#x2022;&nbsp;'


def custom_title(title, color, fsize, weight):
    st.markdown(f"<p style='text-align: center; color : {color}; font-size:{fsize}px; font-weight:{weight}'>{title}</p>", unsafe_allow_html=True)

def custom_sidebar_title(title, color, fsize, weight):
    st.sidebar.markdown(f"<p style='text-align: left; color : {color}; font-size:{fsize}px; font-weight:{weight}'>{title}</p>", unsafe_allow_html=True)

def custom_text(text, color, fsize, weight):
    st.sidebar.markdown(f"<p style='text-align: left; color : {color}; font-size:{fsize}px; font-weight:{weight}'>{text}</p>", unsafe_allow_html=True)

def custom_text_main(title, color, fsize, weight, align):
    st.markdown(f"<p style='text-align: {align}; color : {color}; font-size:{fsize}px; font-weight:{weight}'>{title}</p>", unsafe_allow_html=True)

intro = f"{square_bullet_point1} Use Case:<br>Using historical data, the ARIMA Forecasting Method defines the steps for taking a product and auto dealers as inputs, and then predicts the sales of three car dealers (Robin, Prince, and George). Based on past data trends, the app projects automobile sales for Mercedes-Benz, BMW, and Volkswagen over the following three months.<br>{circke_bullet_point} This could affect or aid demand adjustments, replenishments, management tactics, and even the assessment of dealers' skill levels."
evaluation = f"{square_bullet_point1} Example Evaluation of Results:<br>{circke_bullet_point} Historical Performance: Strong sales growth in the last year, especially in the SUV segment. Historical Performance: Steady sales with a slight decline in the sedan category, but growth in electric vehicle (EV) sales. Historical Performance: Consistent luxury segment sales, with a spike during year-end sales events."
insights =f"{square_bullet_point1}Example Insights: <br> {circke_bullet_point} Dealer George anticipates increase in VW Sales due to new model releases and seasonal promotions. {square_bullet_point1} Robin Mercedes Benz sales are projected to rise due to end-of-year incentives and strong brand loyalty. {square_bullet_point1} There's a expected growth in Prince's BMW sales driven by EV demand and holiday promotions."
summary = f"{square_bullet_point1}Example Summary:<br>{circke_bullet_point}Overall Trends: All three dealers and brands are expected to see an upward trend in sales over the next three months, with VW leading in volume due to its broader appeal and strategic push in the EV market.<br>{circke_bullet_point}Recommendations: Focus on targeted marketing campaigns for new models and leverage seasonal promotions to maximize sales potential across all brands.<br>This simulation provides a snapshot of expected performance based on historical sales data and market trends."