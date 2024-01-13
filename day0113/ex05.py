import sqlite3

conn = sqlite3.connect('example.db') # 데이터 베이스 연결
cursor = conn.cursor() # 커서 생성 # 쿼리 퍼다 나르는애



try:
    # users 테이블의 모든 행 가져오기
    cursor.execute("SELECT * FROM users")
    rows= cursor.fetchmany(3)


    # 결과 출력
    for row in rows:
        print(row)

    rows = cursor.fetchmany(3)
    for row in rows:
        print(row)
except Exception as e:
    print(e)
finally:
    # 커서와 연결닫기
    cursor.close()
    conn.close()
