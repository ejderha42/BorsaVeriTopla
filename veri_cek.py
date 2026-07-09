import yfinance as yf
import pandas as pd
from datetime import datetime
import os   


# hisseler.txt dosyasını oku
with open("hisseler.txt", "r") as f:
    hisseler = [line.strip() for line in f if line.strip()]

# sonuçları tut
data = []

for hisse in hisseler:
    try:
        ticker = yf.Ticker(hisse + ".IS")  # BIST için .IS uzantısı
        fiyat = ticker.history(period="1d").tail(1)["Close"].values[0]
        degisim = ticker.history(period="1d").tail(1)["Close"].pct_change().values[-1] * 100
        data.append([datetime.now(), hisse, fiyat, degisim])
    except Exception as e:
        print(f"{hisse} için veri alınamadı: {e}")

# CSV’ye ekle
df = pd.DataFrame(data, columns=["Zaman", "Hisse", "Fiyat", "%Değişim"])
# df.to_csv("hisse_verileri.csv", mode="a", header=False, index=False)
dosya = "hisse_verileri.csv"

df.to_csv(
    dosya,
    mode="a",
    header=not os.path.exists(dosya),
    index=False
)