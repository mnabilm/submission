# Import Library
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as mticker

# Load dataset
days_df = pd.read_csv("./days_df_clean.csv")
hours_df = pd.read_csv("./hours_df_clean.csv")

# Konfigurasi Streamlit
st.set_page_config(page_title="Bike Sharing Dashboard", layout="wide")

# Sidebar Filter Musim
seasons = {0: "Spring", 1: "Summer", 2: "Fall", 3: "Winter"}
selected_season = st.sidebar.selectbox("Pilih Musim", ["Semua"] + list(seasons.values()))

# Filter Data
if selected_season != "Semua":
    season_key = list(seasons.keys())[list(seasons.values()).index(selected_season)]
    filtered_days_df = days_df[days_df["season"] == season_key]
else:
    filtered_days_df = days_df

# Judul Dashboard
st.title("Bike Sharing Dashboard")

# 1. Visualisasi Pola Peminjaman Sepeda Berdasarkan Musim
st.subheader("Total Peminjaman Sepeda Berdasarkan Musim")
fig, ax = plt.subplots(figsize=(8, 6))
sns.barplot(x='season', y='cnt', data=filtered_days_df, estimator=sum, palette='Blues', ax=ax)
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: int(x)))
ax.set_xlabel("Musim")
ax.set_ylabel("Total Peminjaman Sepeda")
ax.set_xticklabels(['Spring', 'Summer', 'Fall', 'Winter'])
st.pyplot(fig)

# 2. Visualisasi Tren Peminjaman Sepeda Berdasarkan Jam dalam Sehari
st.subheader("Tren Peminjaman Sepeda Berdasarkan Jam dalam Sehari")
fig, ax = plt.subplots(figsize=(10, 6))
sns.lineplot(x='hr', y='cnt', data=hours_df, estimator=sum, marker='o', color='b', ax=ax)
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: int(x)))
ax.set_xlabel("Jam")
ax.set_ylabel("Total Peminjaman Sepeda")
ax.set_xticks(range(0, 24))
ax.grid(True)
st.pyplot(fig)

# 3. Visualisasi Pengaruh Kondisi Cuaca terhadap Jumlah Peminjaman Sepeda
st.subheader("Pengaruh Kondisi Cuaca terhadap Peminjaman Sepeda")
fig, ax = plt.subplots(figsize=(8, 6))
sns.barplot(x='weathersit', y='cnt', data=hours_df, estimator=sum, palette='coolwarm', ax=ax)
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: int(x)))
ax.set_xlabel("Kondisi Cuaca")
ax.set_ylabel("Total Peminjaman Sepeda")
ax.set_xticklabels(['Clear', 'Mist/Cloudy', 'Light Rain/Snow'])
st.pyplot(fig)

# Footer
st.caption("Copyright (c) 2025 Bike Sharing Analysis")
