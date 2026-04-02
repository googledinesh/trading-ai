import sqlite3

class TradeHistoryDB:
    def __init__(self, db_name='trade_history.db'):
        self.connection = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):
        c = self.connection.cursor()
        # Create trades table
        c.execute('''CREATE TABLE IF NOT EXISTS trades ( \
            id INTEGER PRIMARY KEY AUTOINCREMENT, \
            symbol TEXT, \
            amount REAL, \
            price REAL, \
            trade_type TEXT, \
            date TEXT)''')
        # Create signals table
        c.execute('''CREATE TABLE IF NOT EXISTS signals ( \
            id INTEGER PRIMARY KEY AUTOINCREMENT, \
            symbol TEXT, \
            signal_type TEXT, \
            date TEXT)''')
        # Create performance table
        c.execute('''CREATE TABLE IF NOT EXISTS performance ( \
            id INTEGER PRIMARY KEY AUTOINCREMENT, \
            total_trades INTEGER, \
            win_rate REAL, \
            average_return REAL)''')
        self.connection.commit()

    def add_trade(self, symbol, amount, price, trade_type, date):
        c = self.connection.cursor()
        c.execute('''INSERT INTO trades (symbol, amount, price, trade_type, date) \
                     VALUES (?, ?, ?, ?, ?)''', (symbol, amount, price, trade_type, date))
        self.connection.commit()

    def add_signal(self, symbol, signal_type, date):
        c = self.connection.cursor()
        c.execute('''INSERT INTO signals (symbol, signal_type, date) \
                     VALUES (?, ?, ?)''', (symbol, signal_type, date))
        self.connection.commit()

    def update_performance(self, total_trades, win_rate, average_return):
        c = self.connection.cursor()
        c.execute('''INSERT INTO performance (total_trades, win_rate, average_return) \
                     VALUES (?, ?, ?)''', (total_trades, win_rate, average_return))
        self.connection.commit()

    def close(self):
        self.connection.close()