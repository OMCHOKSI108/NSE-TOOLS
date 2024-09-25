import pandas as pd
from nsepython import option_chain

# Fetch Nifty and Bank Nifty option chain data
nifty_option_chain = option_chain("NIFTY")
banknifty_option_chain = option_chain("BANKNIFTY")

# Function to generate custom strike prices (first 130 strikes)
def generate_custom_strikes():
    # Example strike price range for Bank Nifty and Nifty
    strikes = list(range(37500, 61000, 100))[:130]  # Adjust based on real data if needed
    return strikes

# Function to collect option chain data for the given strike prices
def collect_option_chain(option_chain, custom_strikes):
    data = {
        "Strike Price": [],
        "Call OI": [], "Call Chng in OI": [], "Call Volume": [], "Call IV": [], "Call LTP": [], "Call Chng": [], 
        "Call Bid Qty": [], "Call Bid": [], "Call Ask Qty": [],
        "Put OI": [], "Put Chng in OI": [], "Put Volume": [], "Put IV": [], "Put LTP": [], "Put Chng": [], 
        "Put Bid Qty": [], "Put Bid": [], "Put Ask Qty": []
    }
    
    for entry in option_chain['records']['data']:
        strike_price = entry['strikePrice']
        
        # Only include custom strike prices
        if strike_price in custom_strikes:
            data['Strike Price'].append(strike_price)
            
            # Collect call data
            if 'CE' in entry:
                data['Call OI'].append(entry['CE']['openInterest'])
                data['Call Chng in OI'].append(entry['CE']['changeinOpenInterest'])
                data['Call Volume'].append(entry['CE']['totalTradedVolume'])
                data['Call IV'].append(entry['CE']['impliedVolatility'])
                data['Call LTP'].append(entry['CE']['lastPrice'])
                data['Call Chng'].append(entry['CE']['change'])
                data['Call Bid Qty'].append(entry['CE']['bidQty'])
                data['Call Bid'].append(entry['CE']['bidprice'])
                data['Call Ask Qty'].append(entry['CE']['askQty'])
            else:
                # Append empty values if CE data is not available
                data['Call OI'].append('-')
                data['Call Chng in OI'].append('-')
                data['Call Volume'].append('-')
                data['Call IV'].append('-')
                data['Call LTP'].append('-')
                data['Call Chng'].append('-')
                data['Call Bid Qty'].append('-')
                data['Call Bid'].append('-')
                data['Call Ask Qty'].append('-')

            # Collect put data
            if 'PE' in entry:
                data['Put OI'].append(entry['PE']['openInterest'])
                data['Put Chng in OI'].append(entry['PE']['changeinOpenInterest'])
                data['Put Volume'].append(entry['PE']['totalTradedVolume'])
                data['Put IV'].append(entry['PE']['impliedVolatility'])
                data['Put LTP'].append(entry['PE']['lastPrice'])
                data['Put Chng'].append(entry['PE']['change'])
                data['Put Bid Qty'].append(entry['PE']['bidQty'])
                data['Put Bid'].append(entry['PE']['bidprice'])
                data['Put Ask Qty'].append(entry['PE']['askQty'])
            else:
                # Append empty values if PE data is not available
                data['Put OI'].append('-')
                data['Put Chng in OI'].append('-')
                data['Put Volume'].append('-')
                data['Put IV'].append('-')
                data['Put LTP'].append('-')
                data['Put Chng'].append('-')
                data['Put Bid Qty'].append('-')
                data['Put Bid'].append('-')
                data['Put Ask Qty'].append('-')

    return pd.DataFrame(data)

# Generate custom strike prices for filtering (130 strikes)
custom_strikes = generate_custom_strikes()

# Collect data for Nifty and Bank Nifty
nifty_data = collect_option_chain(nifty_option_chain, custom_strikes)
banknifty_data = collect_option_chain(banknifty_option_chain, custom_strikes)

# Save the result to Excel with the strike price column in the center
with pd.ExcelWriter('option_chain_data_strikes.xlsx') as writer:
    # Write the Nifty option chain data
    nifty_df = nifty_data[
        ['Call OI', 'Call Chng in OI', 'Call Volume', 'Call IV', 'Call LTP', 'Call Chng', 'Call Bid Qty', 'Call Bid', 'Call Ask Qty', 
         'Strike Price', 
         'Put Bid', 'Put Bid Qty', 'Put Ask Qty', 'Put Chng', 'Put LTP', 'Put IV', 'Put Volume', 'Put Chng in OI', 'Put OI']
    ]
    nifty_df.to_excel(writer, sheet_name='Nifty Option Chain', index=False)

    # Write the Bank Nifty option chain data
    banknifty_df = banknifty_data[
        ['Call OI', 'Call Chng in OI', 'Call Volume', 'Call IV', 'Call LTP', 'Call Chng', 'Call Bid Qty', 'Call Bid', 'Call Ask Qty', 
         'Strike Price', 
         'Put Bid', 'Put Bid Qty', 'Put Ask Qty', 'Put Chng', 'Put LTP', 'Put IV', 'Put Volume', 'Put Chng in OI', 'Put OI']
    ]
    banknifty_df.to_excel(writer, sheet_name='Bank Nifty Option Chain', index=False)

print("Option chain data with 130 strike prices saved successfully to 'option_chain_data_strikes.xlsx'!")
