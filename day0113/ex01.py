import sqlite3

# 데이터 베이스 연결
conn = sqlite3.connect('example.db')

# 커서 생성
cursor = conn.cursor()

# users 테이블 생성
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL
    )
""")

# 커밋 오라클이나 MYSQL은 테이블 생성하거나 지울 때 트랜잭션의 범위에 적용이 안되는데
# SQLITE는 DDL(CREATE,DELETE,ALTER(SQLITE는 ALTER 문법 없음)도 트랜잭션의 범위로 쳐서 COMMIT을 해야함)
conn.commit() # SAVE 라고 생각하자

# 커서와 연결 닫기
cursor.close()
conn.close()