

import streamlit as st
# Declare a form and call methods directly on the returned object
form = st.form(key='my_form')
a=form.number_input(label='Enter Number A  ')
b=form.number_input(label='Enter Number B')

c=form.number_input(label='Enter Number C')



submit_button = form.form_submit_button(label='Submit')

 
st.write('Press submit to Find Greater Value ')

if submit_button:
    if a>b:
        if a>c :
            st.write(f' {a}is greater')
        else:    
            st.write(f' {c}is greater')
    else: 
        if b>c :
            st.write(f' {b}is greater')
        else:    
            st.write(f' {c}is greater')
