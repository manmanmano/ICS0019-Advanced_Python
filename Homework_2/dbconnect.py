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
            time_open TIME NOT NULL,
            time_closed TIME NOT NULL,
            FOREIGN KEY(ProviderID) REFERENCES PROVIDER(ID));''')

    # create table PROVIDER
    conn.execute('''CREATE TABLE IF NOT EXISTS PROVIDER
            (ID INTEGER PRIMARY KEY AUTOINCREMENT,
            ProviderName TEXT NOT NULL);''')

    print("Tables created successfully!")


def checkRecords(cursor, table, column, data): 
    """
    Checks if value in column already exists. Returns True if record is not found.
    """
    cursor.execute(f"SELECT * FROM {table} WHERE {column} = ?", (data, ))
    # get number of records
    nr_records = cursor.fetchall()
    # if record is not found execute, else do nothing
    if len(nr_records) == 0:
        return True


def createRecords():
    """
    Create required records in tables CANTEEN and PROVIDER
    """
    # add provider data
    cursor = conn.cursor()
    provider_data = ["Rahva toit", "Balitc Restaurants Estonia AS", "TTÜ Sport OÜ", "bitStop Kohvik OÜ"]
    for data in provider_data: 
        format_str = """INSERT INTO PROVIDER (ProviderName) VALUES ("{provider_name}");"""
        sql_command = format_str.format(provider_name=data)
        if checkRecords(cursor, "PROVIDER", "ProviderName",  data):
            cursor.execute(sql_command)

    # add IT-College data with a separate statement as requirement said
    sql_command = """INSERT INTO CANTEEN (ProviderID, Name, Location, time_open, time_closed)
    VALUES ("4", "bitStop KOHVIK", "IT College, Raja 4c", "9:30", "16:00")"""
    if checkRecords(conn.cursor(), "CANTEEN", "Location", "IT College, Raja 4c"):
        cursor.execute(sql_command)

    # add remaining canteen data with lists
    canteen_data = [("1", "Economics- and social science building canteen", "Akadeemia tee 3, SOC-building", "8:30", "18:30"), 
        ("1", "Library canteen", "Akadeemia tee 1/Ehitajate tee 7", "8:30", "19:00"), 
        ("2", "Main building Deli cafe", "Ehitajate tee 5, U01 building", "9:00", "16:30"),
        ("2", "Main building Daily lunch restaurant", "Ehitajate tee 5, U01 building", "9:00", "16:30"),
        ("1", "U06 building canteen", "U06 building", "9:00", "16:00"),
        ("2", "Natural Science building canteen", "Akadeemia tee 15, SCI building", "9:00", "16:00"),
        ("2", "ICT building canteen", "Raja 15/Mäepealse 1", "9:00", "16:00"),
        ("3", "Sports building canteen", "Männiliiva 7, S01 building", "11:00", "20:00")] 



    conn.commit()
    print("Data records inserted successfully!")


def closeconn():
    """
    Close connection to diners database
    """
    conn.close()
    print("Connection closed.")


if __name__ == "__main__":
    opendb()
    create_tables()
    createRecords()
    closeconn()
