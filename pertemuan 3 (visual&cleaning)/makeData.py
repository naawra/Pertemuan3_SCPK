import pandas as pd
import numpy as np

data = {
    'Bulan': ['Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct'],
    'Penjualan_Kopi': [150, 200, np.nan, 220, 250, 170, 300, 190, 210, 260],
    'Harga_Rata2': ['25000', '30000', '28000', 'error', '32000', '27000', '35000', '30000', '31000', '33000'],
    'Rating': [85, -99, 90, 88, 95, 80, 92, 70, -99, 89],
    'Usia_Pelanggan': [22, np.nan, 25, 20, 30, 28, 24, 35, 21, np.nan],
    'Metode_Bayar': ['QRIS', 'Cash', 'QRIS', 'Kartu', 'QRIS', 'Cash', 'QRIS', 'Kartu', 'QRIS', 'QRIS']
}

df_setup = pd.DataFrame(data)
df_setup.to_csv('data_kafe.csv', index=False)
print("File 'data_kafe.csv' berhasil dibuat!")