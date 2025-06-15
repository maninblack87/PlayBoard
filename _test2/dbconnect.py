import mysql.connector
from mysql.connector import Error

# 1) 'starcraft' 데이터베이스를 연결한다
# 2) 'starcraft' 데이터베이스가 없다면 새로만든다
def connect_to_mysql():

    # 일단 수행
    try:
        connection = mysql.connector.connect(
            host = 'localhost',
            user = 'root',          # 변경 가능(사용자 이름)
            password = 'maninblack87*',      # 변경 가능(사용자 비밀번호)
            charset = 'utf8mb4',
            use_unicode = True,
        )

        if connection.is_connected():
            print('MySQL 서버에 연결됨')

            # 해당 커넥션의 DB목록을 살펴보고 리스트로 저장
            cursor = connection.cursor()
            cursor.execute("SHOW DATABASES")
            existing_dbs = [db[0] for db in cursor.fetchall()]
            # starcraft DB가 있는지 체크
            # 없으면 새로 생성
            db_name = "starcraft"
            if db_name in existing_dbs:
                print(f"이미 존재하는 DB '{db_name}' 사용")
            else:
                cursor.execute(
                    f"CREATE DATABASE {db_name} CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci"
                )
                print(f"DB '{db_name}' 생성 완료")

            # starcraft DB로 재연결
            connection.database = db_name
            print(f"현재 사용 중인 데이터베이스: {connection.database}")

            # 이후 쿼리 등에서 사용할 수 있도록 반환
            return connection

    # 에러 발생시
    except Error as e:
        print(f"오류발생 : {e}")
        return None
    

# 3) 단독으로 이 모듈을 실행시킬 때 연결 성공시 연결 종료를
if __name__ == "__main__":
    conn = connect_to_mysql()
    if conn:
        conn.close()
        print("연결 종료")