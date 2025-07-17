# import base64
# import streamlit as st
# import pickle
# # from sklearn.metrics import accuracy_score
# import pandas as pd
# @st.cache_data
# def get_img_as_base64(file):
#     with open(file, "rb") as f:
#         data = f.read()
#     return base64.b64encode(data).decode()


# img = get_img_as_base64("background.jpg")
# # data:image/png;base64,{img}
# page_bg_img = f"""
# <style>
# [data-testid="stAppViewContainer"] > .main {{
# background-image: url("data:image/png;base64,{img}");
# width: 100%;
# height:100%
# background-repeat: no-repeat;
# background-attachment: fixed;
# background-size: cover;
# }}

# [data-testid="stSidebar"] > div:first-child {{
# background-image: url("data:image/png;base64,{img}");
# background-position: center; 
# background-repeat: no-repeat;
# background-attachment: fixed;
# }}

# [data-testid="stHeader"] {{
# background: rgba(0,0,0,0);
# }}

# [data-testid="stToolbar"] {{
# right: 2rem;
# }}
# </style>
# """
# teams =['--- select ---',
#         'Sunrisers Hyderabad',
#         'Mumbai Indians',
#         'Kolkata Knight Riders',
#         'Royal Challengers Bangalore',
#         'Kings XI Punjab',
#         'Chennai Super Kings',
#         'Rajasthan Royals',
#         'Delhi Capitals']
# cities =['Bangalore', 'Hyderabad', 'Kolkata', 'Mumbai', 'Visakhapatnam',
#        'Indore', 'Durban', 'Chandigarh', 'Delhi', 'Dharamsala',
#        'Ahmedabad', 'Chennai', 'Ranchi', 'Nagpur', 'Mohali', 'Pune',
#        'Bengaluru', 'Jaipur', 'Port Elizabeth', 'Centurion', 'Raipur',
#        'Sharjah', 'Cuttack', 'Johannesburg', 'Cape Town', 'East London',
#        'Abu Dhabi', 'Kimberley', 'Bloemfontein']

# pipe = pickle.load(open('pipe.pkl','rb'))

# st.markdown(page_bg_img, unsafe_allow_html=True)
# st.markdown("""
#     # **IPL VICTORY PREDICTOR**            
# """)
# # st.title("IPL Victory Predictor")

# col1, col2 = st.columns(2)

# with col1:
   
#    batting_team =  st.selectbox('Select Batting Team',teams)

# with col2:
#     if batting_team == '--- select ---':
#         bowling_team = st.selectbox('Select Bowling Team', teams)
#     else:
#         filtered_teams = [team for team in teams if team != batting_team]
#         bowling_team = st.selectbox('Select Bowling Team', filtered_teams)

# seleted_city = st.selectbox('Select Venue',cities)

# target = st.number_input('Target')

# col1,col2,col3 = st.columns(3)

# with col1:
#     score = st.number_input('Score')
# with col2:
#     overs = st.number_input("Over Completed")
# with col3:
#     wickets = st.number_input("wicktes down")

# if st.button('Predict Winning Probability'):
#     try:
#         runs_left = target - score
#         balls_left = 120 - (overs*6)
#         wickets = 10-wickets
#         crr = score/overs
#         rrr = runs_left/(balls_left/6)
    
#         input_data = pd.DataFrame({'batting_team':[batting_team],'bowling_team':[bowling_team],
#                          'city':[seleted_city],'runs_left':[runs_left],'balls_left':[balls_left],
#                          'wickets_remaining':[wickets],'total_runs_x':[target],'crr':[crr],'rrr':[rrr]})
       
        
#         result = pipe.predict_proba(input_data)
    
#         loss = result[0][0]
#         win =  result[0][1]
#         st.header(batting_team + " = "+str(round(win*100)) + "%")
#         st.header(bowling_team + " = "+str(round(loss*100)) + "%")
#     except:
#         st.header("Some error occured.. Please check you inputs !!")




















import base64
import streamlit as st
import pickle
import pandas as pd

@st.cache_data
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

img = get_img_as_base64("background.jpg")

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
    background-image: url("data:image/png;base64,{img}");
    background-size: cover;
    background-repeat: no-repeat;
    background-attachment: fixed;
    padding: 2rem;
}}

[data-testid="stSidebar"] > div:first-child {{
    background-color: rgba(0,0,0,0.7);
    border-radius: 10px;
}}

h1, h2, h3, .stSelectbox label, .stNumberInput label {{
    color: #ffffff !important;
    font-weight: bold;
}}

[data-testid="stButton"] > button {{
    background-color: #FF5733;
    color: white;
    font-size: 18px;
    border-radius: 8px;
    padding: 10px;
}}
[data-testid="stButton"] > button:hover {{
    background-color: #C70039;
}}

.stNumberInput input, .stSelectbox select {{
    border-radius: 10px;
    padding: 8px;
}}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)
st.markdown("""
    <h1 style='text-align: center; color: white;'>🏏 IPL Victory Predictor 🏆</h1>
""", unsafe_allow_html=True)

teams = ['--- select ---', 'Sunrisers Hyderabad', 'Mumbai Indians', 'Kolkata Knight Riders',
         'Royal Challengers Bangalore', 'Kings XI Punjab', 'Chennai Super Kings',
         'Rajasthan Royals', 'Delhi Capitals']

cities = ['Bangalore', 'Hyderabad', 'Kolkata', 'Mumbai', 'Visakhapatnam', 'Indore',
          'Durban', 'Chandigarh', 'Delhi', 'Dharamsala', 'Ahmedabad', 'Chennai', 'Ranchi',
          'Nagpur', 'Mohali', 'Pune', 'Bengaluru', 'Jaipur', 'Port Elizabeth',
          'Centurion', 'Raipur', 'Sharjah', 'Cuttack', 'Johannesburg', 'Cape Town',
          'East London', 'Abu Dhabi', 'Kimberley', 'Bloemfontein']

pipe = pickle.load(open('pipe.pkl', 'rb'))

col1, col2 = st.columns(2)
with col1:
    batting_team = st.selectbox('Select Batting Team', teams)
with col2:
    if batting_team == '--- select ---':
        bowling_team = st.selectbox('Select Bowling Team', teams)
    else:
        filtered_teams = [team for team in teams if team != batting_team]
        bowling_team = st.selectbox('Select Bowling Team', filtered_teams)

seleted_city = st.selectbox('Select Venue', cities)

target = st.number_input('Target', min_value=1)

col1, col2, col3 = st.columns(3)
with col1:
    score = st.number_input('Score', min_value=0)
with col2:
    overs = st.number_input("Overs Completed", min_value=0.0, max_value=20.0, step=0.1)
with col3:
    wickets = st.number_input("Wickets Down", min_value=0, max_value=10)

if st.button('Predict Winning Probability'):
    try:
        if overs == 0:
            st.warning("Overs cannot be zero. Please enter a valid number.")
        else:
            runs_left = target - score
            balls_left = 120 - (overs * 6)
            wickets_remaining = 10 - wickets
            crr = score / overs
            rrr = runs_left / (balls_left / 6) if balls_left > 0 else 0
            
            input_data = pd.DataFrame({
                'batting_team': [batting_team], 'bowling_team': [bowling_team],
                'city': [seleted_city], 'runs_left': [runs_left], 'balls_left': [balls_left],
                'wickets_remaining': [wickets_remaining], 'total_runs_x': [target],
                'crr': [crr], 'rrr': [rrr]
            })
            
            result = pipe.predict_proba(input_data)
            loss, win = result[0]
            
            st.success(f"🏏 {batting_team}: {round(win * 100)}% chances to win")
            st.error(f"🏏 {bowling_team}: {round(loss * 100)}% chances to win")
    except Exception as e:
        st.error(f"An error occurred: {e}")
