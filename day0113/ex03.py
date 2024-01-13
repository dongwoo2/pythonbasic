import sqlite3

conn = sqlite3.connect('example.db') # 데이터 베이스 연결
cursor = conn.cursor() # 커서 생성 # 쿼리 퍼다 나르는애

# 데이터 삽입을 위한 파라미터 세트
data = [('John', 30), ('Jane', 25), ('Mike',40)]

try:
    # executemary() 메서드를 사용하여 여러 개의 데이터를 삽입
    cursor.executemany("INSERT INTO users (name,age) VALUES (?,?)", data)
    conn.commit() # 커밋
except Exception as e:
    conn.rollback() # 롤백
    print(e)
finally:
    # 커서와 연결 닫기
    cursor.close()
    conn.close()
