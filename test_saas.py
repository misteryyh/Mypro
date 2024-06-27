# coding:utf-8

"""
creatime:2021-08-19
creatby:meilulin@yeah.net
"""


from faker import Faker
import random
import os
import openpyxl

header = ['报备人','姓名','手机号','证件类型','证件号码','入职项目','用工性质','招聘渠道','管道名称','市场属性','面试时间','性别',
          '入职时间','劳动合同主体','薪资发放主体','合同类型','合同开始日期','合同结束日期','邮箱','工号','入职部门','入职岗位','工作制','试用期(天)','转正工资','试用期工资','户口性质','工作地址','民族','户籍地址','现住址','政治面貌','婚姻状况','学历','毕业院校','毕业专业','首次参加工作时间','年龄','个人社保账号','个人公积金账号','工资卡开户行','工资卡账号','开户行地址','开户行所在省','开户行所在市','紧急联系人姓名','紧急联系人关系','紧急联系人电话','是否有亲朋同行','同行人姓名','同行人部门','同行人岗位','同行人电话']
channel = ['内荐']
# '供应商','自主招聘','企业转移','内荐','呼叫中心'
# yuanxiao = ['湖南大学']
conduit = ['道锦AAA人才招聘']
guandaomingcheng = ['杨永辉','谭啸钦','仇洪伟']
neijian = ['231282199508211686', '21030320020718550X']
market = ['本地市场', '外地市场']
em_type = ['劳动合同','实习协议','劳务协议','退休返聘','第三方订单']
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
        if a1 == '供应商':
            a2 = random.choice(conduit)
        elif a1 == '内荐':
            a2 = random.choice(neijian)
        else:
            a2 = random.choice(creatby)
        test_lst = [random.choice(creatby),fake.name(),fake.phone_number(),'居民身份证',fake.ssn(min_age=18, max_age=50),'新菲光信息科技有限公司',
                    random.choice(em_type),a1,a2,random.choice(market),
                    fake.date_this_month(before_today=True, after_today=False)]
        ws.append(test_lst)
    wb.save(filepath)
    print('创建成功:', filepath)
    wb.close()


if __name__ == '__main__':
    number = 5
    try:
        creat_report(int(number))
    except Exception as e:
        print('创建失败:', e)

# fake = Faker('zh_TW')
# print(fake.profile(fields=None, sex=None))
