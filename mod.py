def preturn():

  import numpy as np
  import pandas as pd
  import matplotlib.pyplot as plt
  import yfinance as yf

#securities: a list of the ticker symbols of the securities
  securities = []
  while True:
    tickers = input("Enter ticker of chosen single security (Enter to exit):")
    if not tickers:
      break
    securities.append(tickers)
#weights: a numpy array of the weights of the securities in the portfolio
  weights = []
  while True:
    weight_input = input("Enter weigths of securities in order (Enter to exit):")
    if not weight_input:
      break
    weights.append(float(weight_input))
  weights = np.array(weights)

#checking the input data
  if len(securities) != len(weights):
        print("Error: The number of securities and weights must be the same.")

  if sum(weights) != 1:
        print("Error: The sum of weights cannot be different than 1.")

#downloading the data of securities
  df=pd.DataFrame()
  for x in securities:
    df[x]=yf.download(x,start='2013-1-1')['Adj Close']

#calculating porfolio returns
  returns = (df/df.shift(1))-1
  returns.head()
  a_returns = (returns.mean()*250)
  a_returns.head()

  par=np.dot(a_returns, weights)
  print("Annual return on portfolio: in %" ,par*100)
