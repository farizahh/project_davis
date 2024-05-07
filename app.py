import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# Membaca database
data = pd.read_csv("tips.csv")

# Menampilkan judul di halaman web
st.title('Scatter Plot')

# Penyebaran plot dengan data tip
plt.scatter(data['day'], data['tip'], c=data['size'], 
            s=data['total_bill'])

# Menambahkan judul dalam Plot
plt.title("Scatter Plot")

# Mengatur label X dan Y
plt.xlabel('Day')
plt.ylabel('Tip')

plt.colorbar()

plt.show()
