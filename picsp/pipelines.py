# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql


class PicspPipeline(object):
    def __init__(self):
        self.conn = pymysql.connect(host='127.0.0.1', user='root', password='123456', db='picsp', charset='utf8')

    def process_item(self, item, spider):
        # for j in range(0,len(item['pic_name'])):
        #     pic_name = item['pic_name'][j]
        #     pic_url = item['pic_url'][j]
        #     sql = "insert into pic(name,url) values ('"+str(pic_name[0])+"','"+str(pic_url[0])+"')"
        #     self.conn.query(sql)
        #     self.conn.commit()
        return item

    def close_spider(self, spider):
        self.conn.close()
