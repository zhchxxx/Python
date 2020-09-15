import pymysql

class MysqlHelper(object):
    def __init__(self):
        self.conn = pymysql.connect(
            host = '127.0.0.1',
            port = 3306,
            user = 'root',
            passwd = 'root',
            db = 'sexdb',
            charset = 'utf8mb4'
        )
        self.cursor = self.conn.cursor()

    def execute_modify_sql(self,sql,data):
        self.cursor.execute(sql,data)
        self.conn.commit()

    def is_has_same_data(self,sql,data):
       try:
            self.cursor.execute(sql,data)
            results = self.cursor.fetchone()
            # print(results)
            count = results[0]
            # print(count)
            if int(count) > 0:
                return 1
            else:
                return 0
       except:
           return 0

    def __del__(self):
        self.cursor.close()
        self.conn.close()

if __name__ == '__main__':
    helper = MysqlHelper()
    # insert_sql = 'INSERT INTO weibo_test (weibo_text) VALUES (%s); '
    # data = ('这是你发的一条微博',)
    # helper.execute_modify_sql(insert_sql,data)

    # querysql = 'SELECT COUNT(id) FROM title WHERE title = \'' + '[MP4]【极品风骚】辽宁沈阳交友' + '\''
    # print(querysql)
    # result =  helper.is_has_same_data(querysql)

    querysql = 'SELECT COUNT(id) FROM title WHERE title = %s and url = %s '
    data = ('爆乳女神吴梦梦调教系列 黑丝高跟鞋穿风衣 挑战户外车上高潮 酒店啪啪巨乳摇拽','https://k6.7086xx.xyz/pw/html_data/5/2009/4953193.html',)
    result =  helper.is_has_same_data(querysql,data)

    if result == 1:
        print('has same data')
    else:
        print('has not same data')