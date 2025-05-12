# Chainz_SEE_Balance
### Chainz_SEE_Balance is a Python script that reads a CSV file containing CAT (Catcoin) wallet addresses and queries their balance using the Chainz.Cryptoid.info public API. It's designed to be simple.

## 🔮 Features

-  **Reads wallet addresses from CSV** and checks their balances via API.
-  **Retry logic** for handling API rate limits and network issues.
-  **Exports results** to a timestamped CSV file.
-  **Warnings** for empty or invalid addresses.
-  **Progress tracker** during processing.


## 📦 Requirements

- Python 3.6 or higher
- `pandas`
- `requests`

## 🐲 Usage

Clone this repository:
```bash
sudo git clone https://github.com/yourusername/Chainz_SEE_Balance.git
cd Chainz_SEE_Balance
```
Install dependencies with:
```bash
sudo pip install -r requirements.txt --break-system-packages
```

Prepare your .csv file:

- You can export your wallet addresses from your Qt wallet software.

Run the script:
```bash
sudo python3 chainz_see_balance.py
```
When prompted, select or enter the CSV file name.

Balances will be printed in the terminal and saved as:
`balances_output_YYYYMMDD_HHMMSS.csv`

### Done! Review your balances and enjoy!

## 🧑‍💻 Author
@vm.vest
vmvest.dev@gmail.com

### 🍧 Donations appreciated!

**CAT:** 9TEAitMMnTCWeHAKrEMZ1wxiJkTQZcbqth

**USDT:** 0xc8a3889fBfA929A79122E20bF5f71eDFBFD3C154

**BTC:** bc1qk72w9az3cdsllvnz6u05wsnzv4fqax93yshrwt

**SOL:** qR9dxTzz6XS4NDJkj3Tvfm8555frTcWgi4qv7SXEirk

**TON:** UQCp5ohQ8iqAwbYAGew06XHct9D3HS52iU2Q2XcR-8SLSu24

### 💡 Have a coin you'd like us to support? Open an issue or submit a request — multi-coin support is on our roadmap!
