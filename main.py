from view import View
'''
人：
类名：Person
属性：姓名，身份证号， 电话号， 卡

卡：
类名：Card
属性：卡号，密码，余额


提款机类：
名称：ATM
属性：
方法：开户，查询，取款，存储，转账，改密，锁定，解锁，补卡，销户，退出


银行：
名称：Bank

界面：


'''


def main():
    #用户管理员开机界面显示
    view = View()
    if view.printAdminView():
        return -1
    view.sysFunctionView()

if __name__ == '__main__':
    main()