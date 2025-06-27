import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import io
from PIL import Image 

st.set_page_config(
    page_title='Student Score Analysis',
    layout='wide'
)


st.title('Student Score Analysis Application')
st.write('Please upload a .xlsx file (have student scores column)')
uploaded_file = st.file_uploader("Select .xlsx file that have student scores column", type=['xlsx'])

def calculate_avg(scores):
    return sum(scores) / len(scores)

def calculate_score_distribution(scores):
    distribution = {
        '<50': 0,
        '50-60': 0,
        '61-70': 0,
        '71-80': 0,
        '81-90': 0,
        '91-100': 0,
    }
    for score in scores:
        if score < 50:
            distribution['<50'] += 1
        elif 50 <= score <= 60: 
            distribution['50-60'] += 1
        elif 61 <= score <= 70:
            distribution['61-70'] += 1
        elif 71 <= score <= 80: 
            distribution['71-80'] += 1
        elif 81 <= score <= 90:
            distribution['81-90'] += 1
        else:
            distribution['91-100'] += 1
                
    return distribution

if uploaded_file is not None:
    try:
        df = pd.read_excel(uploaded_file)
        scores = df['Điểm số'].dropna().astype(float).tolist()
        
        if scores:
            st.write(f'Total Student: {len(scores)}')
            st.write(f'Average Score: {round(calculate_avg(scores), 2)}')
        
            distribute = calculate_score_distribution(scores)
            score_grp = list(distribute.keys())
            score_val = list(distribute.values())
        
            fig, ax = plt.subplots(figsize=(3, 3))
            ax.pie(score_val, labels=score_grp, autopct='%1.1f%%', startangle=90)
            ax.axis('equal')
            plt.tight_layout(pad=0.1)
        
            buf = io.BytesIO()
            fig.savefig(buf, format='png', dpi=300)
            buf.seek(0)
        
            st.write('Score Distibution Chart')
            img = Image.open(buf)
            
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                st.image(img, width=250)
                st.markdown('Student Score Distribution Chart')
            
    except Exception as error:
        st.error(f'Error: {error}')
        st.error('Please upload file with extension .xlsx')