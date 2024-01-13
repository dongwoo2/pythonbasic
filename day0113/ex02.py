import sqlite3

conn = sqlite3.connect('example.db') # 데이터 베이스 연결
cursor = conn.cursor() # 커서 생성

try:
    # 데이터 삽입
    cursor.execute("INSERT INTO users (name,age) VALUES (?,?)", ('Alice',20))
    cursor.execute("INSERT INTO users (name,age) VALUES (?,?)", ('Bob',25))
    cursor.execute("INSERT INTO users (name,age) VALUES (?,?)", ('Charlie',30))
    conn.commit()
except Exception as e:
    conn.rollback()
    print(e)
finally:
    # 커서와 연결 닫기
    cursor.close()
    conn.close()
