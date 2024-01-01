from goldhand import *
from tqdm import tqdm
import warnings
warnings.filterwarnings("ignore")

tw=Tw()

for ticker in tqdm(tw.stock['name'][0:5000]):
    try:
        tdf = GoldHand(ticker).df
        tdf.to_csv(f'/content/drive/MyDrive/backtest/stock_data/{ticker}.csv', index=False)
    except:
      pass