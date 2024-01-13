import sqlite3

conn = sqlite3.connect('example.db') # 데이터 베이스 연결
cursor = conn.cursor() # 커서 생성 # 쿼리 퍼다 나르는애



try:
    # users 테이블의 모든 행 가져오기
    cursor.execute("SELECT * FROM users")
    row = cursor.fetchone()

    # 결과 출력
    if row:
        print(row)
    else:
        print("No data")


    row = cursor.fetchone()

    # 결과 출력
    if row:
        print(row)
    else:
        print("No data")
        
except Exception as e:
    print(e)
finally:
    # 커서와 연결닫기
    cursor.close()
    conn.close()
