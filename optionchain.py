import pandas as pd
from nsepython import option_chain

# Fetch Nifty and Bank Nifty option chain data
nifty_option_chain = option_chain("NIFTY")
banknifty_option_chain = option_chain("BANKNIFTY")

# Function to format and collect option chain data
def collect_option_chain(option_chain, index_name):
    option_data = []
    
    for entry in option_chain['records']['data']:
        strike_price = entry['strikePrice']
        
        # Extract call option data
        if 'CE' in entry:
            call_oi = entry['CE']['openInterest']
            call_ltp = entry['CE']['lastPrice']
        else:
            call_oi = call_ltp = '-'
        
        # Extract put option data
        if 'PE' in entry:
            put_oi = entry['PE']['openInterest']
            put_ltp = entry['PE']['lastPrice']
        else:
            put_oi = put_ltp = '-'
        
        # Append the data to the list
        option_data.append({
            'Strike Price': strike_price,
            'Call OI': call_oi,
            'Call LTP': call_ltp,
            'Put LTP': put_ltp,
            'Put OI': put_oi,
        })
    
    return option_data

# Collect data for both indices
nifty_data = collect_option_chain(nifty_option_chain, "Nifty")
banknifty_data = collect_option_chain(banknifty_option_chain, "Bank Nifty")

# Create DataFrames
nifty_df = pd.DataFrame(nifty_data)
banknifty_df = pd.DataFrame(banknifty_data)

# Save to Excel
with pd.ExcelWriter('option_chain_data.xlsx') as writer:
    nifty_df.to_excel(writer, sheet_name='Nifty Option Chain', index=False)
    banknifty_df.to_excel(writer, sheet_name='Bank Nifty Option Chain', index=False)

print("Option chain data saved to 'option_chain_data.xlsx' successfully!")
