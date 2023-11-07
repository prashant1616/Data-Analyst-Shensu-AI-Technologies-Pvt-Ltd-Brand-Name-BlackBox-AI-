#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


import numpy as np


# In[27]:


# Loading the tradelog data from the CSV file tradelog.csv
trade_log = pd.read_csv(r"C:\Users\user\Desktop\task\task1\tradelog.csv")


# In[8]:


trade_log.shape
#having 249 rows and 6 columns


# In[28]:


trade_log.head()


# In[29]:


trade_log.columns


# In[30]:


trade_log


# In[31]:


#description of data in the data frame
trade_log.describe() 


# In[17]:


# Defining constants
initial_portfolio_value = 6500  # Initial portfolio value
risk_free_rate = 0.05  # 5% risk-free rate


# In[136]:


#1
# Calculating Total trades

total_trades = len(trade_log)
print(len(trade_log))


# In[137]:


#2
#total number of profitable trade

profitable_trades = print(len(trade_log[trade_log[("Profit_loss")] > 0]))


# In[138]:


#3
# total number of trades in which 'Exit Price'<'Entry Price'

loss_making_trades = print(len(trade_log[trade_log['Profit_loss'] < 0]))


# In[169]:


#changing value of profitable_trades ,total_trades in int for calculating win_rate

profitable_trades = (int("153"))
print(profitable_trades)
loss_making_trades = (int("96"))
print(loss_making_trades)
total_trades = (int("249"))
print(total_trades)


# In[141]:


#4
#Win rate: Win Rate is the ratio of profitable trades to all trades

win_rate = profitable_trades / total_trades
print(win_rate)


# In[142]:


#5
#Average Profit per trade

average_profit_per_trade = trade_log[trade_log['Profit_loss'] > 0]['Profit_loss'].mean()
print(average_profit_per_trade)


# In[143]:


#6
#Average Loss per trade

average_loss_per_trade = trade_log[trade_log['Profit_loss'] < 0]['Profit_loss'].mean()
print(average_loss_per_trade)


# In[145]:


#7
#Risk Reward ratio: Risk Reward Ratio is the ratio of average profit to average loss.

risk_reward_ratio = abs(average_profit_per_trade) / abs(average_loss_per_trade)
print(risk_reward_ratio)


# In[146]:


# calculating loss rate for expectancy formula

loss_rate = 1 - win_rate
print(loss_rate)


# In[147]:


#8
#Expectancy : (Win Rate x Average Profit) - (Loss Rate x Average Loss)

expectancy = (win_rate * average_profit_per_trade) - (loss_rate * average_loss_per_trade)
print(expectancy)


# In[148]:


#9
#Average ROR per trade:

average_ror_per_trade = expectancy / trade_log['Profit_loss'].std()
print(average_ror_per_trade)


# In[149]:


# calculating portfolio return

portfolio_returns = trade_log['Profit_loss'].pct_change().dropna()
print(portfolio_returns)


# In[150]:


#10
#Sharpe Ratio

sharpe_ratio = (portfolio_returns.mean() - risk_free_rate) / portfolio_returns.std()
print(sharpe_ratio)
print(risk_free_rate)


# In[151]:


#11
#Drawdown - Deduction of capital from peak to trough
#Max Drawdown: MDD = (trough — Peak Value) / Peak Value

trough = (1 + portfolio_returns).cumprod()
peak = trough.expanding().max()
drawdown = (trough - peak) / peak
max_drawdown = drawdown.min()
max_drawdown_percentage = max_drawdown * 100
print(max_drawdown)


# In[152]:


#12
#Max Drawdown Percentage

max_drawdown_percentage = max_drawdown * 100
print(max_drawdown_percentage)


# In[153]:


#13
#CAGR -Compound annual growth rate

ending_portfolio_value = initial_portfolio_value + trade_log['Profit_loss'].sum()
print(ending_portfolio_value)

cagr = (ending_portfolio_value / initial_portfolio_value) ** ((1 / total_trades ) - 1)
print(cagr)


# In[154]:


#14
#Calmar Ratio = average annual rate / max drawdown

calmar_ratio = cagr / max_drawdown_percentage
print(calmar_ratio)


# In[170]:


results = pd.DataFrame({
    'Total Trades': [total_trades],
    'Profitable Trades': [profitable_trades],
    'Loss-Making Trades': [loss_making_trades],
    'Win Rate': [win_rate],
    'Average Profit per trade': [average_profit_per_trade],
    'Average Loss per trade': [average_loss_per_trade],
    'Risk Reward ratio': [risk_reward_ratio],
    'Expectancy': [expectancy],
    'Average ROR per trade': [average_ror_per_trade],
    'Sharpe Ratio': [sharpe_ratio],
    'Max Drawdown': [max_drawdown],
    'Max Drawdown Percentage': [max_drawdown_percentage],
    'CAGR': [cagr],
    'Calmar Ratio': [calmar_ratio]
})
results


# In[171]:


# Saving the results to a CSV file
results.to_csv(r"C:\Users\user\Desktop\task\task1\task1.csv",index = False)


# In[ ]:




