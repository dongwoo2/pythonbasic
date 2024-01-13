import sqlite3

# 데이터 베이스 연결
conn = sqlite3.connect('example.db')

# 커서 생성
cursor = conn.cursor()

cursor.execute("""DROP TABLE IF EXISTS info""")

# info 테이블 생성
cursor.execute("""
    CREATE TABLE INFO (
        NO INTEGER PRIMARY KEY AUTOINCREMENT,
        NAME TEXT(20) NOT NULL,
        AGE INTEGER CHECK (1 < AGE AND AGE < 120),
        BTYPE TEXT(2),
        BIRTH TEXT
    )
""")

def create_info(name, age, btype, birth):
    cursor.execute("INSERT INTO INFO (NAME, AGE, BTYPE, BIRTH) VALUES (?,?,?,?)", (name,age,btype,birth))
    conn.commit()
    print("New row added.")

def read_info():
    cursor.execute("SELECT * FROM INFO")
    return cursor.fetchall()

def read_info_no(no):
    cursor.execute("SELECT * FROM INFO WHERE NO = ?", (no,))
    return cursor.fetchall()

def read_info_name(name):
    cursor.execute("SELECT * FROM INFO WHERE NAME = ?", (name,))
    return cursor.fetchall()

def update_info(no, name, age, btype, birth):
    cursor.execute("UPDATE INFO SET NAME =?, AGE=?, BTYPE=?, BIRTH=? WHERE NO=?" , (name, age, btype, birth, no))
    conn.commit()
    print(f"Row with NO = {no} updated.")

def delete_info(no):
    cursor.execute("DELECT FROM INFO WHERE NO = ?", (no,))
    conn.commit()
    print(f"Row with NO = {no} deleted.")

create_info('John', 30, 'A', '1993-01-01')

rows = read_info()
for row in rows:
        print(rows)


update_info(1,'Jane',25,'B','1998-04-22')

print(read_info_name('Jane'))

delete_info(1)

#삭제된 놈 조회
print(read_info_no(1))

cursor.close()

conn.close()