import pymysql

pymysql.version_info = (1, 4, 13, "final", 0)  # 解决因版本问题报错bug
pymysql.install_as_MySQLdb()
