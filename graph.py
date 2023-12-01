import matplotlib.pyplot as plt
import pandas as pd 
caminho_sem = "runs/detect/train9/results.csv"
caminho_com = "runs/detect/train11/results.csv"
df = pd.read_csv(caminho_sem)
print(df.columns)

plt.plot(df['                  epoch'],df['           val/cls_loss'])
plt.show()