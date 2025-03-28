import streamlit as st
import pandas as pd
from functions import get_weather_data

pd.set_option('display.max_rows', None)

lat = 52.5
lon = 13.4

st.title("Temperatur Stunden Tool")
st.write("Stadt = Berlin")

with st.form("my_form"):
  year = st.number_input("Jahr", min_value=2010, max_value=2023, step=1)
  temperature_threshold = st.number_input("Bivalenzpunkt", step=1)
  button = st.form_submit_button('Los gehts')

start_date = f"{year}-01-01"
end_date = f"{year}-12-31T23:00"

if button:
  weather_data = get_weather_data(lat, lon, start_date, end_date)
  
  df = pd.DataFrame(weather_data)
  df = df[['timestamp', 'temperature']]
  
  hours_below_threshold = df[df['temperature'] < temperature_threshold].shape[0]
  st.write(f"Anzahl Stunden unter {temperature_threshold}°C: {hours_below_threshold}h")
  
  st.header("Alle Stunden des Jahres")
  st.dataframe(df)
  # Temperatur runden auf ganze Zahl
  df_rounded = df
  df_rounded = df.dropna(subset=['temperature'])
  df_rounded['temperature_rounded'] = df_rounded['temperature'].round().astype(int)
  

  st.header("Anzahl der Stunden mit genannten Temperaturen")
  # Stunden pro gerundeter Temperatur zählen
  temp_counts = df_rounded['temperature_rounded'].value_counts().sort_index()
  # Nur Werte ≤ Threshold anzeigen
  filtered_counts = temp_counts[temp_counts.index <= temperature_threshold]
  st.dataframe(filtered_counts)

  st.bar_chart(data=filtered_counts)