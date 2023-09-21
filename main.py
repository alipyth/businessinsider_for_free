import databutton as db
import streamlit as st
import requests
from selectolax.parser import HTMLParser
st.title('read Not Free businessinsider articles for free :)')

#r = 'https://fortune.com/crypto/2023/09/01/uniswap-class-action-dismissal-coinbase-tornado-cash-implications/'

r = st.text_input('paste the url of businessinsider article')
st.info('By Ali Jahani https://jahaniwww.com')
sub = st.button('read :)')
if r is not None and sub :
    rr = requests.get(r)
    #articleContent
    parser = HTMLParser(rr.content)
    for p in parser.css('.content-lock-content p'):
        st.markdown(p.text())
