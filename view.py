import time


class View(object):
    admin = '1'
    passwd = '1'
    # def __init__(self, admin):
    #     self.__admin = admin

    def printAdminView(self):
        print("**************************************************************")
        print("*                                                            *")
        print("*                                                            *")
        print("*                     欢迎登陆银行                            *")
        print("*                                                            *")
        print("*                                                            *")
        print("**************************************************************")

        inputAdmin = input("请输入管理员账号：")
        if self.admin != inputAdmin:
            print("账号输入有误！")
            return -1

        inputPasswd = input("请输入管理员密码： ")
        if self.passwd != inputPasswd:
            print("密码输入有误！")
            return -1

        print("登陆成功！请稍后……")
        time.sleep(2)
        return 0

    def sysFunctionView(self):
        print("**************************************************************")
        print("*                  开户(1)     查询(2)                        *")
        print("*                  取款(3)     查询(4)                        *")
        print("*                  转账(5)     改密(6)                        *")
        print("*                                                            *")
        print("*                                                            *")
        print("**************************************************************")