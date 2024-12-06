import pymysql
import pymysql.cursors

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='1234',
    db='db_test',
    cursorclass=pymysql.cursors.DictCursor
)
with connection.cursor() as cursor:
    ## 1번째 문제
    # sql = '''
    # insert into users(first_name, last_name, email,password, 
    #     address, contact, gender) values ('8ki','joa','joa@oz.com','joajoajoa','인천시 오즈구', '01010101010', 'male')
    # '''
    # cursor.execute(sql)
    # connection.commit()

    # # 2번째 문제
    # sql ="update users set address = '서울특별시 오즈구' where first_name = '8ki'"
    # cursor.execute(sql)
    # connection.commit()
    # sql = "insert into sales_records(user_id, store_id, is_refund) values(12,1,0)" 
    
    # sql = "insert into sales_items(sales_record_id,product_id,quantity) values(11,1,3),(11,2,2),(11,10,5)"
    # sql = "insert into order_records(employee_id, supplier_id, raw_material_id, quantity) values(1,1,1,1),(6,2,4,3),(2,2,2,2)"
    
    # sql = '''insert into stocks(raw_material_id, pre_quantity, quantity, change_type, store_id) values
    #     (1,200,190,"out",1),(1,190,180,"out",1),(1,180,170,"out",1)'''
    # cursor.execute(sql)
    # sql = "select * from stocks order by create_at desc limit 3"
    # cursor.execute(sql)
    sql = '''select users.first_name, users.last_name, products.name, sales_items.quantity, products.price, sales_items.created_at from sales_items
        left join products on products.id = product_id
        left join sales_records on sales_records.id = sales_record_id
        left join users on users.id = sales_records.user_id
        left join stores on stores.id = sales_records.store_id
        where users.first_name = '8ki' and users.last_name='joa'
        order by products.price desc limit 3;
        '''    
    cursor.execute(sql)
    a = cursor.fetchall()
    print(a)


    