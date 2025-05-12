import pandas as pd
import requests
import time
import os
from datetime import datetime
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

# ANSI escape codes for colors
COLOR_RESET = "\033[0m"
COLOR_PINK = "\033[38;5;211m"
COLOR_GREEN = "\033[38;5;119m"
COLOR_RED = "\033[38;5;197m"
COLOR_CYAN = "\033[38;5;51m"
COLOR_YELLOW = "\033[38;5;226m"
COLOR_PASTEL_YELLOW = "\033[38;5;229m"
COLOR_ORANGE = "\033[38;5;214m"
COLOR_ORAN_ = "\033[38;5;229m"
COLOR_SOFT_PINK = "\033[38;5;225m"
SEPARATOR_COLOR = "\033[38;5;229m"
SEPARATOR = f"{SEPARATOR_COLOR}{'-' * 70}{COLOR_RESET}"
# ASCII Art
ascii_art = rf"""{COLOR_SOFT_PINK}


                                
          __   __   __    __                 __   __   ______     ______     ______  
         /\ \ / /  /\ "-./  \               /\ \ / /  /\  ___\   /\  ___\   /\__  _\ 
         \ \ \'/   \ \ \-./\ \              \ \ \'/   \ \  __\   \ \___  \  \/_/\ \/ 
          \ \__|    \ \_\ \ \_\              \ \__|    \ \_____\  \/\_____\    \ \_\ 
           \/_/      \/_/  \/_/      ______   \/_/      \/_____/   \/_____/     \/_/ 
                                   /\______\                                                         
                                   \/______/
                                
                          
          ***************************************************************************
          *                                                                         *
          *                 Welcome to Your Chainz_SEE_Balance V0.5                 *
          *                 Author: @vm.vest, vmvest.dev@gmail.com                  *
          *                                                                         *
          *           🍧Donations appreciated!                                      *
          *                                                                         *
          *            9TEAitMMnTCWeHAKrEMZ1wxiJkTQZcbqth                   (CAT)   *
          *            0xc8a3889fBfA929A79122E20bF5f71eDFBFD3C154          (USDT)   *
          *            bc1qk72w9az3cdsllvnz6u05wsnzv4fqax93yshrwt           (BTC)   *
          *            qR9dxTzz6XS4NDJkj3Tvfm8555frTcWgi4qv7SXEirk          (SOL)   *
          *            UQCp5ohQ8iqAwbYAGew06XHct9D3HS52iU2Q2XcR-8SLSu24     (TON)   *
          *                                                                         *
          *                                                                         *
          ***************************************************************************
          
          

{COLOR_RESET}"""
# Setup requests session with retry logic
session = requests.Session()
retry = Retry(total=3, backoff_factor=1, status_forcelist=[429, 500, 502, 503, 504])
adapter = HTTPAdapter(max_retries=retry)
session.mount("https://", adapter)

def get_balance(address):
    url = f"https://chainz.cryptoid.info/cat/api.dws?q=getbalance&a={address}"
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        response = session.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        balance = response.text.strip()
        try:
            float(balance)
        except ValueError:
            print(f"{COLOR_ORANGE}⚠️ Invalid balance returned for {address}: {balance}{COLOR_RESET}")
            return "N/A"
        return balance
    except Exception as e:
        print(f"{COLOR_RED}❌ Error fetching balance for {address}: {e}{COLOR_RESET}")
        return "Error"

def get_csv_path_from_user():
    current_dir_files = [f for f in os.listdir('.') if f.endswith('.csv')]
    if current_dir_files:
        print(f"{COLOR_YELLOW}📁 CSV files in current directory:{COLOR_RESET}")
        for f in current_dir_files:
            print(f" - {COLOR_PASTEL_YELLOW}{f}{COLOR_RESET}")
        file_name = input(f"{COLOR_YELLOW}📦 Enter the CSV file name (e.g., data.csv): {COLOR_RESET}").strip()
        if not file_name.endswith('.csv'):
            file_name += '.csv'
        return file_name
    else:
        return input(f"{COLOR_YELLOW}📦 Enter full path to the CSV file: {COLOR_RESET}").strip()

def process_csv(file_path):
    # Early validation
    if not os.path.isfile(file_path):
        print(f"{COLOR_RED}❌ File does not exist: {file_path}{COLOR_RESET}")
        return

    try:
        df = pd.read_csv(file_path)

        if 'Address' not in df.columns:
            print(f"{COLOR_RED}❌ CSV must contain an 'Address' column.{COLOR_RESET}")
            return

        print(f"\n{COLOR_GREEN}🧾 Address Balances:{COLOR_RESET}")
        print(SEPARATOR)

        results = []

        for idx, address in enumerate(df['Address'], 1):
            if pd.isna(address) or not str(address).strip():
                print(f"{COLOR_ORANGE}⚠️ Skipping empty address at row {idx}{COLOR_RESET}")
                results.append({"Address": address, "Balance": "Invalid"})
                continue

            print(f"{COLOR_PASTEL_YELLOW}🫧 [{idx}/{len(df)}] ({(idx/len(df))*100:.1f}%) Checking {address} ...{COLOR_RESET}")
            balance = get_balance(address)
            try:
                balance_float = float(balance)
                if balance_float > 0:
                    color = COLOR_GREEN
                else:
                    color = COLOR_PINK
            except:
                color = COLOR_PINK  # Default if balance is "N/A" or "Error"

            print(f"→ {address}: {color}{balance} CAT{COLOR_RESET}\n")

            results.append({"Address": address, "Balance": balance})
            time.sleep(1)

        output_df = pd.DataFrame(results)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = f"balances_output_{timestamp}.csv"
        output_df.to_csv(output_file, index=False)
        print(f"{COLOR_GREEN}✅ Results saved to {output_file}{COLOR_RESET}")

    except Exception as e:
        print(f"{COLOR_RED}❌ Error reading CSV: {e}{COLOR_RESET}")

# Main flow
if __name__ == "__main__":
    print(ascii_art)
    csv_path = get_csv_path_from_user()
    process_csv(csv_path)
