# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 22:55:08 2023

@author: JOJIG
"""
import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd
def search_website(website, words):
    response = requests.get(website)
    soup = BeautifulSoup(response.text, "html.parser")
    lines = soup.prettify().splitlines()
    results = []
    for i, line in enumerate(lines):
        for word in words:
            if word in line:
                results.append({"line": i, "word": word})
    df = pd.DataFrame(results)
    return df
def main():
    st.title("Website Search")
    website = st.text_input("Enter the website URL")
    words = [st.text_input(f"Enter word {i+1}") for i in range(5)]
    if website and all(words):
        df = search_website(website, words)
        st.write(df)
        df.to_excel("results.xlsx", index=False)
        st.write("Results saved to excel sheet.")
if __name__ == "__main__":
    main()
