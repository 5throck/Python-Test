import pymysql  # pymysql ����Ʈ

# �������� �����
conn = None
cur = None

sql=""

# ���� �ڵ�
conn = pymysql.connect(host='127.0.0.1', user='root', password='1155', db='pythonDB', charset='utf8')	# ��������
cur = conn.cursor()	# Ŀ������

sql = "CREATE TABLE IF NOT EXISTS userTable (id char(4), userName char(10), email char(15), birthYear int)"	# ������ sql��
cur.execute(sql)	# Ŀ���� sql�� ����

conn.commit()	# ����
conn.close()	# ����