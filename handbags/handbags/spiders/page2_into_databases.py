import MySQLdb
import sys


def main():
    db = MySQLdb.connect("localhost","root","6Tresxcvbhy","flipkart")
    cursor = db.cursor()

    sql = """ create table if not exists bag_info ( id int  auto_increment PRIMARY KEY, item_title varchar(100), colour varchar(255), image_links varchar(255), discount varchar(50), price varchar(50), seller_name varchar(255), date TIMESTAMP DEFAULT CURRENT_TIMESTAMP);"""
    cursor.execute(sql)

    f = open("page2_hand_bag_info")

    for l in f:
        value = tuple(l.split(","))
        item_title = value[0].strip()
	colour = value[1].strip()
	image_links = value[2].strip()
	discount = value[3].strip()
	price = value[4].strip()
	seller_name = value[5].strip()

	value = item_title, colour, image_links, discount, price, seller_name

	sql = """insert into bag_info (item_title, colour, image_links, discount, price, seller_name) values ("%s", "%s", "%s", "%s", "%s", "%s")"""%(value)
        #print sql
        #sys.exit()
	cursor.execute(sql)
	db.commit()


    f.close()
    db.close()


    
if __name__=="__main__":
    main()
