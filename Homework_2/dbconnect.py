import sqlite3


def opendb(): 
    """
    Open the SQLite database
    """
    global conn
    conn = sqlite3.connect('diners.db')
    print("Database opened successfully!")


def create_tables():
    """
    Create tables CANTEEN and PROVIDER in DINERS
    """
    conn.execute('''CREATE TABLE CANTEEN
            (ID INTEGER PRIMARY KEY AUTOINCREMENT,
            ProviderID TEXT NOT NULL, 
            Name TEXT NOT NULL,
            Location VARCHAR(50) NOT NULL,
            time_open TIME NOT NULL,
            time_closed TIME NOT NULL,
            FOREIGN KEY(ProviderID) REFERENCES PROVIDER(ProviderName));''')

    conn.execute('''CREATE TABLE PROVIDER
            (ID INTEGER PRIMARY KEY AUTOINCREMENT,
            ProviderName TEXT NOT NULL);''')

    print("Tables created successfully!")


def closeconn():
    """
    Close connection to diners database
    """
    conn.close()
    print("Connection closed.")


if __name__ == "__main__":
    opendb()
    create_tables()
