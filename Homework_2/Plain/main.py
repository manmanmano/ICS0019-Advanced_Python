import sqlite3


def opendb(): 
    """
    Open the SQLite database diners
    """
    global conn
    conn = sqlite3.connect('diners.db')
    print("Database opened successfully!")


def create_tables():
    """
    Create tables CANTEEN and PROVIDER in DINERS
    """
    # create table CANTEEN
    conn.execute('''CREATE TABLE IF NOT EXISTS CANTEEN
            (ID INTEGER PRIMARY KEY AUTOINCREMENT,
            ProviderID INT NOT NULL,
            Name TEXT NOT NULL,
            Location VARCHAR(100) NOT NULL,
            time_open INT NOT NULL,
            time_closed INT NOT NULL,
            FOREIGN KEY(ProviderID) REFERENCES PROVIDER(ID),
            UNIQUE(Name));''')

    # create table PROVIDER
    conn.execute('''CREATE TABLE IF NOT EXISTS PROVIDER
            (ID INTEGER PRIMARY KEY AUTOINCREMENT,
            ProviderName TEXT NOT NULL,
            UNIQUE(ProviderName));''')

    print("Tables created successfully!")


def createRecords():
    """
    Create required records in tables CANTEEN and PROVIDER
    """
    # add provider data
    cursor = conn.cursor()
    provider_data = ["Rahva toit", "Balitc Restaurants Estonia AS", "TTÜ Sport OÜ", "bitStop Kohvik OÜ"]
    for data in provider_data: 
        format_str = """INSERT OR IGNORE INTO PROVIDER (ProviderName) VALUES ("{provider_name}");"""
        sql_command = format_str.format(provider_name=data)
        cursor.execute(sql_command)

    # add IT-College data with a separate statement as requirement said
    sql_command = """INSERT OR IGNORE INTO CANTEEN (ProviderID, Name, Location, time_open, time_closed)
    VALUES ("4", "bitStop KOHVIK", "IT College, Raja 4c", "930", "1600")"""
    cursor.execute(sql_command)

    # add remaining canteen data with lists
    canteen_data = [("1", "Economics- and social science building canteen", "Akadeemia tee 3, SOC-building", "830", "1830"), 
        ("1", "Library canteen", "Akadeemia tee 1/Ehitajate tee 7", "830", "1900"), 
        ("2", "Main building Deli cafe", "Ehitajate tee 5, U01 building", "900", "1630"),
        ("2", "Main building Daily lunch restaurant", "Ehitajate tee 5, U01 building", "1400", "1630"),
        ("1", "U06 building canteen", "U06 building", "900", "1600"),
        ("2", "Natural Science building canteen", "Akadeemia tee 15, SCI building", "900", "1600"),
        ("2", "ICT building canteen", "Raja 15/Mäepealse 1", "900", "1600"),
        ("3", "Sports building canteen", "Männiliiva 7, S01 building", "1100", "2000")] 
    for data in canteen_data: 
        format_str = """INSERT OR IGNORE INTO CANTEEN (ProviderID, Name, Location, time_open, time_closed) 
        VALUES ("{provider_id}", "{name}", "{location}", "{time_open}", "{time_closed}");"""
        sql_command = format_str.format(provider_id=data[0], name=data[1], location=data[2], time_open=data[3], time_closed=data[4])
        cursor.execute(sql_command)

    conn.commit()
    print("Data records inserted successfully!\n")


def printRecord(cursor):
    """
    Format a record and then print it. Takes query cursor as input.
    """
    for row in cursor:
        print("CANTEEN ID = ", row[0])
        print("PROVIDER ID = ", row[1])
        print("NAME = ", row[2])
        print("LOCATION = ", row[3])
        print("OPENING TIME = ", row[4])
        print("CLOSING TIME = ", row[5], '\n')


def selectRecords():
    """
    fetch and display records from the CANTEEN table
    """
    print("Canteens opened 16:15 - 18:00:\n")
    cursor = conn.execute("SELECT * FROM CANTEEN WHERE time_open <= 1615 AND time_closed >= 1800")
    printRecord(cursor)

    print("Canteens served by Rahva Toit:\n")
    cursor = conn.execute("""SELECT * FROM CANTEEN C INNER JOIN PROVIDER P ON 
            P.ID=C.ProviderID WHERE P.ProviderName='Rahva toit'""")
    printRecord(cursor)


def closeconn():
    """
    Close connection to diners database
    """
    conn.close()
    print("Connection closed.")


if __name__ == "__main__":
    print("\n")
    opendb()
    create_tables()
    createRecords()
    selectRecords()
    closeconn()
    print("\n")
