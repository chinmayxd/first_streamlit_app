import streamlit

streamlit.title('My parents new healty dinner')
streamlit.header ('Breakfast Menu')
streamlit.text ('🥣 Omega three and Blueberry oatmeal')
streamlit.text ('🥗 Kale,spinach & rocket smoothie')
streamlit.text ('🐔  Hard-Boiled Free-Range Egg ')
streamlit.text ( '🥑🍞 avacado toast ')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
