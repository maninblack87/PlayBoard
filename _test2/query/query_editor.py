from tkinter import messagebox
from mysql.connector import Error
from dbconnect import connect_to_mysql

# (데이터 테이블이 없다면) 데이터 테이블 생성 함수
def create_unit_table():

    # 데이터베이스 연결
    # 커서 생성(SQL문 수행을 위한)
    dbconn = connect_to_mysql()
    cursor = dbconn.cursor()

    # SQL문(유닛 테이블 생성(해당 테이블이 없으면 실행되는))
    # SQL문 수행
    create_table_query = """
    CREATE TABLE IF NOT EXISTS unit(
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(50) NOT NULL,
        atk INT NOT NULL,
        dur INT NOT NULL
    ) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
    """
    cursor.execute(create_table_query)
    dbconn.commit()

    # 성공 메세지
    messagebox.showinfo("unit 테이블 생성 완료", "unit 테이블이 성공적으로 생성되었습니다.")


# 유닛 등록(추가) 함수
def register_unit(name, img, atk, dur):

    # 데이터베이스 연결
    # 커서 생성(SQL문 수행을 위한)
    dbconn = connect_to_mysql()
    cursor = dbconn.cursor()

    # SQL문 수행
    insert_query = "INSERT INTO unit VALUES(%s, %s, %s, %s)"
    cursor.execute(insert_query, (name, img, atk, dur))
    dbconn.commit()

    # 성공 메세지
    messagebox.showinfo("유닛 등록(추가) 완료", f"unit 테이블에 성공적으로 등록(추가)되었습니다.\n유닛이름:{name}")