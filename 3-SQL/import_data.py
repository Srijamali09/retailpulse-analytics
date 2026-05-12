import pandas as pd
import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Admin@1234',
    database='retailpulse'
)

df = pd.read_csv('C:/Users/91630/Documents/RetailPulse-Analytics/1-Data/train_fixed.csv')

cursor = conn.cursor()
cursor.execute('TRUNCATE TABLE sales')

success = 0
errors = 0

for _, row in df.iterrows():
    try:
        cursor.execute('''INSERT INTO sales VALUES 
        (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)''', 
        list(row))
        success += 1
    except Exception as e:
        errors += 1
        if errors <= 3:
            print('Error:', e)

conn.commit()
print(f'Success: {success}, Errors: {errors}')
conn.close()