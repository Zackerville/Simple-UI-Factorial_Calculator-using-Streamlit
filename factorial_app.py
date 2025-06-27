import streamlit as st
import os

st.set_page_config(
    page_title='Factorial Calculation',
    layout='wide'
)

def factorial(number):
    if number == 0 or number == 1:
        return 1
    return number * factorial(number - 1)

def load_user():
    '''Read valid user from user.txt'''
    
    try:
        if os.path.exists('user.txt'):
            with open('user.txt', 'r', encoding='utf-8') as file:
                users = [line.strip() for line in file.readlines() if line.strip()]
            return users
        else:
            st.error(f'File user.txt is not exists')
            return None
    except Exception as error:
        st.error(f'Error in reading file: {error}')
        return None

def login_page():
    '''Login page'''
    
    users = load_user()
    st.title('Login')
    st.subheader('Welcome to factorial calculation simulation App')
    st.write('You will need to login to use this service')
    
    username = st.text_input('Type your username')
    if st.button('Login'):
        if username in users:
            st.session_state.logged_in = True
            st.session_state.username = username
            st.rerun()
        else:
            st.session_state.logged_in = False
            st.session_state.username = ''
            st.write('Invalid username to use this service')
            
def factorial_calculator():
    '''Calculate factorial if logged'''
    
    st.title('Factorial Calculation Simulator')
    st.subheader(f'Welcome, {st.session_state.username}')
    
    # Log out
    if st.button('Log out'):
        st.session_state.logged_in = False
        st.session_state.username = ''
        login_page()
        st.rerun()
    
    st.divider()
    
    number = st.number_input('Type a number', min_value=0, max_value=1000)
    if st.button('Calculate'):
        result = factorial(number)
        st.write(f'The factorial of {number} is: {result}')
            
def main():
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
    if 'username' not in st.session_state:
        st.session_state.username = ''
        
    if st.session_state.logged_in:
        factorial_calculator()
    else:
        login_page()

if __name__ == '__main__':
    main()