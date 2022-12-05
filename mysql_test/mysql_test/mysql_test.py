import pymysql  # pymysql 임포트

# 전역변수 선언부
conn = None
cur = None

sql=""

# 메인 코드
conn = pymysql.connect(host='127.0.0.1', user='root', password='1155', db='pythonDB', charset='utf8')	# 접속정보
cur = conn.cursor()	# 커서생성

sql = "CREATE TABLE IF NOT EXISTS userTable (id char(4), userName char(10), email char(15), birthYear int)"	# 실행할 sql문
cur.execute(sql)	# 커서로 sql문 실행

conn.commit()	# 저장
conn.close()	# 종료