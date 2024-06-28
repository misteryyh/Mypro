# coding:utf-8

"""
creatime:2021-08-19
creatby:meilulin@yeah.net
"""


from faker import Faker
import random
import os
import openpyxl

header = ['报备人', '招聘渠道', '管道名称', '市场属性',
          '用工类型','证件类型', '证件号码', '手机号', '面试时间', '姓名', '性别']
channel = ['供应商','自主招聘',]
# '供应商','自主招聘','企业转移','内荐'
# yuanxiao = ['湖南大学']
conduit = ['供应商A']
# neibuqudao = ['上海优尔蓝陕西分公司','上海优尔蓝绍兴分公司','江西优尔蓝']
neijian = ['410203199506296492']
market = ['本地市场', '外地市场']
em_type = ['劳动合同','兼职协议','实习协议','劳务协议','退休返聘','第三方雇员']
creatby = ['杨永辉']
eger = ['男', '女']


def creat_report(number):
    filepath = os.getcwd() + '\报备导入测试数据{0}条.xlsx'.format(number)
    fake = Faker('zh_CN')
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.append(header)
    for _ in range(number):
        a1 = random.choice(channel)
        # if a1 == '院校':
        #     a2 = random.choice(yuanxiao)
        if a1 == '供应商':
            a2 = random.choice(conduit)
        elif a1 == '内荐':
            a2 = random.choice(neijian)
        else:
            a2 = random.choice(creatby)
        test_lst = [random.choice(creatby), a1, a2, random.choice(
            market), random.choice(em_type),'居民身份证', fake.ssn(min_age=18, max_age=50), fake.phone_number(),
            fake.date_this_month(before_today=True, after_today=False), fake.name()]
        ws.append(test_lst)
    wb.save(filepath)
    print('创建成功:', filepath)
    wb.close()


if __name__ == '__main__':
    number = 3
    try:
        creat_report(int(number))
    except Exception as e:
        print('创建失败:', e)


# fake = Faker('zh_TW')
# print(fake.profile(fields=None, sex=None))