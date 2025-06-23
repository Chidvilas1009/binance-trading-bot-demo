from binance.client import Client
import logging
import sys

# Setup Logging
logging.basicConfig(level=logging.INFO, filename='bot.log',
                    format='%(asctime)s - %(levelname)s - %(message)s')

class BasicBot:
    def __init__(self, api_key, api_secret, testnet=True):
        self.client = Client(api_key, api_secret, testnet=testnet)
        logging.info("Bot initialized")

    def place_market_order(self, symbol, side, quantity):
        try:
            # Dummy response
            order = {
                'symbol': symbol,
                'side': side,
                'type': 'MARKET',
                'quantity': quantity,
                'status': 'FILLED (simulated)'
            }
            logging.info(f"[DUMMY] Market Order Successful: {order}")
            print(f"[DUMMY] Market Order Executed: {order}")
        except Exception as e:
            logging.error(f"[DUMMY] Market Order Failed: {e}")
            print(f"[DUMMY] Error placing market order: {e}")

    def place_limit_order(self, symbol, side, quantity, price):
        try:
            # Dummy response
            order = {
                'symbol': symbol,
                'side': side,
                'type': 'LIMIT',
                'price': price,
                'quantity': quantity,
                'status': 'NEW (simulated)'
            }
            logging.info(f"[DUMMY] Limit Order Successful: {order}")
            print(f"[DUMMY] Limit Order Executed: {order}")
        except Exception as e:
            logging.error(f"[DUMMY] Limit Order Failed: {e}")
            print(f"[DUMMY] Error placing limit order: {e}")

if __name__ == "__main__":
    print("=== Simplified Binance Futures Trading Bot ===")

    print("[DUMMY MODE] No real API key needed. Press Enter to continue.")
    api_key = input("Enter your Binance API Key (skip in dummy mode): ")
    api_secret = input("Enter your Binance API Secret (skip in dummy mode): ")

    bot = BasicBot(api_key, api_secret)
    logging.info("Bot started by user (DUMMY MODE)")

    while True:
        print("\n1. Market Order\n2. Limit Order\n3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            symbol = input("Symbol (e.g., BTCUSDT): ")
            side = input("Side (BUY/SELL): ").upper()
            quantity = float(input("Quantity: "))
            logging.info(f"[DUMMY] User requested Market Order - Symbol: {symbol}, Side: {side}, Quantity: {quantity}")
            bot.place_market_order(symbol, side, quantity)

        elif choice == '2':
            symbol = input("Symbol (e.g., BTCUSDT): ")
            side = input("Side (BUY/SELL): ").upper()
            quantity = float(input("Quantity: "))
            price = float(input("Price: "))
            logging.info(f"[DUMMY] User requested Limit Order - Symbol: {symbol}, Side: {side}, Quantity: {quantity}, Price: {price}")
            bot.place_limit_order(symbol, side, quantity, price)

        elif choice == '3':
            logging.info("[DUMMY] Bot exited by user")
            print("Exiting bot...")
            break

        else:
            logging.warning(f"[DUMMY] Invalid option selected: {choice}")
            print("Invalid option. Please try again.")
