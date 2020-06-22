import streamlit as st
import pandas as pd

def main():
  st.title('Pandas com StreamLit')
  st.image('logo.png')
  file = 'IRIS.csv'
  #file = st.file_uploader('Escolha o arquivo para upload',type='csv')
  if file:
    slider = st.slider('Valores',1,100)
    df = pd.read_csv(file)
    st.dataframe(df.head(slider))

    st.markdown('Table')
    st.table(df.head(slider))
    st.write(df.columns)



if __name__ == '__main__':
  main()