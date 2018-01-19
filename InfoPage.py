# encoding: utf-8
import pymysql
import datetime
from tkinter import *
from tkinter.messagebox import *
import M_GUI as M
con = pymysql.connect(host='localhost', user='root', passwd='610339Cl1p', db='cr', port=3306, charset='utf8')
cur = con.cursor()


class ShowUser(object):
    def __init__(self, master=None):
        self.root = master  # 定义内部变量
        self.root.geometry('620x350+200+20')  # 设置窗口大小、位置
        self.root.title('当前用户列表')
        self.createpage()

    def createpage(self):
        self.page = Frame(self.root)
        self.page.pack()
        self.getmsg()

    def getmsg(self):
        cur.execute("select count(id_s) from stu")  # 获取当前用户/id个数
        self.data_count = cur.fetchall()
        cur.execute("select id_s from stu")  # 获取编号/id列
        self.data_id = cur.fetchall()
        cur.execute("select name from stu")  # 获取名字列
        self.data_nm = cur.fetchall()
        cur.execute("select cls from stu")  # 获取班级列
        self.data_cs = cur.fetchall()
        cur.execute("select sx from stu")  # 获取性别列
        self.data_sx = cur.fetchall()
        cur.execute("select sno from stu")  # 获取学/账号列
        self.data_sn = cur.fetchall()

        self.show()

    def show(self):
        Label(self.page, text='编号').grid(row=0, column=0)  # 标签
        Label(self.page, text='名字').grid(row=0, column=1)  # 标签
        Label(self.page, text='班级').grid(row=0, column=2)  # 标签
        Label(self.page, text='性别').grid(row=0, column=3)  # 标签
        Label(self.page, text='学/账号').grid(row=0, column=4)  # 标签

        self.back = Menu(self.root)  # 创建返回栏
        self.back.add_command(label='返回系统', command=self.jumpback)
        self.root['menu'] = self.back  # 设置返回菜单
        self.lb_1 = Listbox(self.page, width=4, height=self.data_count, selectmode=EXTENDED)  # 编号/id
        self.lb_2 = Listbox(self.page, width=12, height=self.data_count, selectmode=EXTENDED)  # 名字
        self.lb_3 = Listbox(self.page, width=12, height=self.data_count, selectmode=EXTENDED)  # 班级
        self.lb_4 = Listbox(self.page, width=4, height=self.data_count, selectmode=EXTENDED)  # 性别
        self.lb_5 = Listbox(self.page, width=17, height=self.data_count, selectmode=EXTENDED)  # 学/账号

        for self.row in self.data_id:
            for self.col in self.row:
                self.lb_1.insert(END, self.col)
        for self.row in self.data_nm:
            for self.col in self.row:
                self.lb_2.insert(END, self.col)
        for self.row in self.data_cs:
            for self.col in self.row:
                self.lb_3.insert(END, self.col)
        for self.row in self.data_sx:
            for self.col in self.row:
                self.lb_4.insert(END, self.col)
        for self.row in self.data_sn:
            for self.col in self.row:
                self.lb_5.insert(END, self.col)

        self.lb_1.grid(row=1, column=0)
        self.lb_2.grid(row=1, column=1)
        self.lb_3.grid(row=1, column=2)
        self.lb_4.grid(row=1, column=3)
        self.lb_5.grid(row=1, column=4)

    def jumpback(self):
        self.page.destroy()
        M.M_GUI(self.root)


class AddUser(object):
    def __init__(self, master=None):
        self.root = master  # 定义内部变量
        self.root.geometry('620x350+200+20')  # 设置窗口大小、位置
        self.root.title('注册新用户')
        self.varN = StringVar()  # 姓名
        self.varP = StringVar()  # 密码
        self.varC = StringVar()  # 班级
        self.varR = IntVar()  # 性别
        self.varR.set(1)
        self.back = Menu(self.root)  # 创建返回栏
        self.back.add_command(label='返回系统', command=self.jumpback)
        self.root['menu'] = self.back  # 设置返回菜单
        self.createpage()

    def createpage(self):
        self.page = Frame(self.root)
        self.page.pack()
        self.blank()

    def blank(self):
        Label(self.page, text='姓名').grid(row=0, column=0)  # 标签 .place(x=20, y=10)
        Radiobutton(self.page, variable=self.varR, text='男', value=1).grid(row=0, column=2)
        Radiobutton(self.page, variable=self.varR, text='女', value=0).grid(row=0, column=4)
        Label(self.page, text='班级').grid(row=1, column=0)  # .place(x=20, y=40)
        Label(self.page, text='密码').grid(row=2, column=0)  # .place(x=20, y=40)
        Entry(self.page, width=24, textvariable=self.varN).grid(row=0, column=1)  # 文本框（姓名）
        Entry(self.page, width=24, textvariable=self.varC).grid(row=1, column=1)  # 文本框（班级）
        Entry(self.page, width=24, textvariable=self.varP).grid(row=2, column=1)  # 文本框（密码）
        Button(self.page, text='注册', width=4, height=2, command=self.wrtmsg).grid(row=2, column=50, rowspan=4)

    def wrtmsg(self):
        if self.varP.get() != '' and self.varC.get() != '' and self.varN.get != '':
            cur.execute("select count(id_s) from stu")  # 获取当前用户/id个数
            self.data_count = cur.fetchall()
            self.sx = '男'
            if self.varR.get() == 0:
                self.sx = '女'
            self.sno = '2015070403' + str(19-int(str(self.data_count[0][0])))
            self.ins = str(int(self.data_count[0][0])+1) + ', \'' + self.varN.get() + '\', \'' + self.varC.get() + '\', \'' + self.varP.get() + '\', \'' + self.sx + '\', \'' + self.sno + '\''
            cur.execute('insert into stu values(' + self.ins + ')')
            showinfo(title='成功注册', message=('您的账号为：' + self.sno))
            # con.commit()  # ******************************************************************************************
            self.jumpback()
        else:
            showinfo(title='警告', message='请务必填写所有栏！')

    def jumpback(self):
        self.page.destroy()
        M.M_GUI(self.root)


class DelUser(object):
    def __init__(self, master=None):
        self.root = master  # 定义内部变量
        self.root.geometry('620x350+200+20')  # 设置窗口大小、位置
        self.root.title('删除用户')
        self.varI = StringVar()  # id
        self.varS = StringVar()  # 学/账号
        self.back = Menu(self.root)  # 创建返回栏
        self.back.add_command(label='返回系统', command=self.jumpback)
        self.root['menu'] = self.back  # 设置返回菜单
        self.createpage()

    def createpage(self):
        self.page = Frame(self.root)
        self.page.pack()
        self.blank()

    def blank(self):
        Label(self.page, text='请至少提供以上一项').grid(row=2, column=1)  # .place(x=20, y=40)
        Label(self.page, text='账号').grid(row=0, column=0)  # 标签 .place(x=20, y=10)
        Label(self.page, text=' id').grid(row=1, column=0)  # .place(x=20, y=40)
        Entry(self.page, width=24, textvariable=self.varS).grid(row=0, column=1)  # 文本框（账号）
        Entry(self.page, width=24, textvariable=self.varI).grid(row=1, column=1)  # 文本框（id）
        Button(self.page, text='删除', width=4, height=2, command=self.getmsg).grid(row=1, column=50)

    def getmsg(self):  # ———————————————————————————————————————————————————————————————————————————————————————————————
        cur.execute("select sno from stu where id_s =%s", self.varI.get())
        self.data_sno = cur.fetchall()

        cur.execute("select id_s from stu where sno =%s", self.varS.get())
        self.data_id = cur.fetchall()

        if self.varI.get() == '':
            if self.varS.get() == '':
                showinfo(title='错误', message='至少一项！')
            elif str(self.data_id) == '()':
                showinfo(title='错误', message='账号错误！')
            else:
                cur.execute('delete from stu where sno =' + self.varS.get())
                showinfo(title='提示', message='删除成功！')
                # con.commit()  # **************************************************************************************
                self.jumpback()

        elif str(self.data_sno) == '()':
            if self.varS.get() == '':
                showinfo(title='错误', message='id错误！')
            elif str(self.data_id) == '()':
                showinfo(title='错误', message='请填写正确信息！')
            else:
                showinfo(title='错误', message='id错误！')

        else:
            if self.varS.get() == '':
                cur.execute('delete from stu where id_s =' + self.varI.get())
                showinfo(title='提示', message='删除成功！')
                # con.commit()  # **************************************************************************************
                self.jumpback()
            elif str(self.data_id) == '()':
                showinfo(title='错误', message='账号错误！')

            elif self.varI.get() != str(self.data_id[0][0]):
                showinfo(title='错误', message='账号与id不匹配！')
            else:
                cur.execute('delete from stu where sno =' + self.varS.get())
                showinfo(title='提示', message='删除成功！')
                # con.commit() # ***************************************************************************************
                self.jumpback()  # —————————————————————————————————————————————————————————————————————————————————————

    def jumpback(self):
        self.page.destroy()
        M.M_GUI(self.root)


class MdfyUser(object):
    def __init__(self, master=None):
        self.root = master  # 定义内部变量
        self.root.geometry('620x350+200+20')  # 设置窗口大小、位置
        self.varI = StringVar()  # id
        self.varS = StringVar()  # 学/账号
        self.root.title('修改入口')
        self.varN = StringVar()  # 姓名
        self.varP = StringVar()  # 密码
        self.varC = StringVar()  # 班级
        self.varR = IntVar()  # 性别
        self.varR.set(1)
        self.flag = 0
        self.back = Menu(self.root)  # 创建返回栏
        self.back.add_command(label='返回系统', command=self.jumpback)
        self.root['menu'] = self.back  # 设置返回菜单
        self.createpage()

    def createpage(self):
        self.page = Frame(self.root)
        self.page.pack()
        self.blank()

    def blank(self):
        Label(self.page, text='请至少提供以上一项，进入修改').grid(row=2, column=1)  # .place(x=20, y=40)
        Label(self.page, text='账号').grid(row=0, column=0)  # 标签 .place(x=20, y=10)
        Label(self.page, text=' id').grid(row=1, column=0)  # .place(x=20, y=40)
        Entry(self.page, width=24, textvariable=self.varS).grid(row=0, column=1)  # 文本框（账号）
        Entry(self.page, width=24, textvariable=self.varI).grid(row=1, column=1)  # 文本框（id）
        Button(self.page, text='提交', width=4, height=2, command=self.getmsg).grid(row=1, column=50)

    def getmsg(self):  # ———————————————————————————————————————————————————————————————————————————————————————————————
        cur.execute("select sno from stu where id_s =%s", self.varI.get())
        self.data_sno = cur.fetchall()

        cur.execute("select id_s from stu where sno =%s", self.varS.get())
        self.data_id = cur.fetchall()

        if self.varI.get() == '':
            if self.varS.get() == '':
                showinfo(title='错误', message='至少填写一项！')
            elif str(self.data_id) == '()':
                showinfo(title='错误', message='账号错误！')
            else:
                self.recreatepage()

        elif str(self.data_sno) == '()':
            if self.varS.get() == '':
                showinfo(title='错误', message='id错误！')
            elif str(self.data_id) == '()':
                showinfo(title='错误', message='请填写正确信息！')
            else:
                showinfo(title='错误', message='id错误！')

        else:
            if self.varS.get() == '':
                self.flag = 1
                self.recreatepage()
            elif str(self.data_id) == '()':
                showinfo(title='错误', message='账号错误！')

            elif self.varI.get() != str(self.data_id[0][0]):
                showinfo(title='错误', message='账号与id不匹配！')
            else:
                self.recreatepage()  # —————————————————————————————————————————————————————————————————————————————————

    def recreatepage(self):
        self.root.title('修改信息')
        self.page.destroy()
        self.page = Frame(self.root)
        self.page.pack()
        self.blank_2()

    def blank_2(self):
        # print(self.flag)
        if self.flag == 1:
            cur.execute("select name from stu where id_s =%s", self.varI.get())
            self.varN.set(cur.fetchall()[0][0])
            cur.execute("select cls from stu where id_s =%s", self.varI.get())
            self.varC.set(cur.fetchall()[0][0])
            '''cur.execute("select psw from stu where id_s =%s", self.varI.get())
            self.varP.set(cur.fetchall()[0][0])'''

            cur.execute("select sx from stu where id_s =%s", self.varI.get())
            self.sex = cur.fetchall()[0][0]
            if self.sex == '女':
                self.varR.set(0)

        elif self.flag == 0:
            cur.execute("select name from stu where sno =%s", self.varS.get())
            self.varN.set(cur.fetchall()[0][0])
            cur.execute("select cls from stu where sno =%s", self.varS.get())
            self.varC.set(cur.fetchall()[0][0])
            '''cur.execute("select psw from stu where sno =%s", self.varS.get())
            self.varP.set(cur.fetchall()[0][0])'''

            cur.execute("select sx from stu where sno =%s", self.varS.get())
            self.sex = cur.fetchall()[0][0]
            if self.sex == '女':
                self.varR.set(0)

        Label(self.page, text='姓名').grid(row=0, column=0)  # 标签 .place(x=20, y=10)
        Radiobutton(self.page, variable=self.varR, text='男', value=1).grid(row=0, column=2)
        Radiobutton(self.page, variable=self.varR, text='女', value=0).grid(row=0, column=4)
        Label(self.page, text='班级').grid(row=1, column=0)  # .place(x=20, y=40)
        Label(self.page, text='密码').grid(row=2, column=0)  # .place(x=20, y=40)
        Entry(self.page, width=24, textvariable=self.varN).grid(row=0, column=1)  # 文本框（姓名）
        Entry(self.page, width=24, textvariable=self.varC).grid(row=1, column=1)  # 文本框（班级）
        Entry(self.page, width=24, textvariable=self.varP).grid(row=2, column=1)  # 文本框（密码)
        Button(self.page, text='修改', width=4, height=2, command=self.wrtmsg).grid(row=2, column=50, rowspan=4)

    def wrtmsg(self):
        if self.varP.get() != '' and self.varC.get() != '' and self.varN.get != '':
            self.sx = '男'
            if self.varR.get() == 0:
                self.sx = '女'
            if self.flag == 1:
                cur.execute('update stu set name =\'' + self.varN.get() + '\', cls =\'' + self.varC.get() + '\', psw =\'' + self.varP.get() + '\', sx =\'' + self.sx + '\' where id_s =' + self.varI.get())
            elif self.flag == 0:
                cur.execute('update stu set name =\'' + self.varN.get() + '\', cls =\'' + self.varC.get() + '\', psw =\'' + self.varP.get() + '\', sx =\'' + self.sx + '\' where sno =' + self.varS.get())
            showinfo(title='提示', message='修改成功！')
            # con.commit() # *******************************************************************************************
            self.jumpback()
        else:
            showinfo(title='警告', message='请务必填写所有栏！')

    def jumpback(self):
        self.page.destroy()
        M.M_GUI(self.root)


class showCptr_L(object):
    def __init__(self, master=None):
        self.root = master  # 定义内部变量
        self.root.geometry('620x350+200+20')  # 设置窗口大小、位置
        self.root.title('空闲机位')
        self.back = Menu(self.root)  # 创建返回栏
        self.back.add_command(label='返回系统', command=self.jumpback)
        self.root['menu'] = self.back  # 设置返回菜单
        self.createpage()

    def createpage(self):
        self.page = Frame(self.root)
        self.page.pack()
        self.getmsg()

    def getmsg(self):
        cur.execute("select count(id_c) from c_sta where ocu ='N'")  # 获取当前空闲机位的个数
        self.data_count = cur.fetchall()
        cur.execute("select id_c from c_sta where ocu ='N'")  # 获取当前空闲机位的个数
        self.data_id_c = cur.fetchall()
        cur.execute("select oft from c_sta where ocu ='N'")  # 获取当前空闲机位的下机时间
        self.data_oft = cur.fetchall()
        '''img_1 = PhotoImage(file='TIM.jpg')
        Label(self.root, image=img_1).pack()'''
        if self.data_count[0][0] == 0:
            Label(self.page, text='当前没有空余机位！').grid(row=0, column=0)
        else:
            Label(self.page, text='机位号').grid(row=0, column=0)
            Label(self.page, text='下机时间').grid(row=0, column=1)
            self.lb = Listbox(self.page, width=4, height=self.data_count[0][0], selectmode=EXTENDED)
            self.lb2 = Listbox(self.page, width=20, height=self.data_count[0][0], selectmode=EXTENDED)
            for n in self.data_id_c:
                self.lb.insert(END, n[0])
            self.lb.grid(row=1, column=0)
            for i in self.data_oft:
                if i[0] == None:
                    self.lb2.insert(END, ' ')
                else:
                    self.lb2.insert(END, i[0])

            self.lb.grid(row=1, column=0)
            self.lb2.grid(row=1, column=1)

    def jumpback(self):
        self.page.destroy()
        M.M_GUI(self.root)


class showCptr_E(object):
    def __init__(self, master=None):
        self.root = master  # 定义内部变量
        self.root.geometry('620x350+200+20')  # 设置窗口大小、位置
        self.root.title('已占机位')
        self.back = Menu(self.root)  # 创建返回栏
        self.back.add_command(label='返回系统', command=self.jumpback)
        self.root['menu'] = self.back  # 设置返回菜单
        self.createpage()

    def createpage(self):
        self.page = Frame(self.root)
        self.page.pack()
        self.getmsg()

    def getmsg(self):
        cur.execute("select count(id_c) from c_sta where ocu ='Y'")  # 获取当已占用机位的个数
        self.data_count = cur.fetchall()
        cur.execute("select id_c from c_sta where ocu ='Y'")  # 获取当前已占机位的个数
        self.data_id_c = cur.fetchall()
        cur.execute("select ont from c_sta where ocu ='Y'")  # 获取当前已占机位的上机时间
        self.data_ont = cur.fetchall()

        if self.data_count[0][0] == 0:
            Label(self.page, text='当前没有已占机位').grid(row=0, column=0)
        else:
            Label(self.page, text='机位号').grid(row=0, column=0)
            Label(self.page, text='上机时间').grid(row=0, column=1)
            self.lb = Listbox(self.page, width=4, height=self.data_count[0][0], selectmode=EXTENDED)
            self.lb2 = Listbox(self.page, width=20, height=self.data_count[0][0], selectmode=EXTENDED)
            for n in self.data_id_c:
                self.lb.insert(END, n[0])
            for i in self.data_ont:
                self.lb2.insert(END, i[0])

            self.lb.grid(row=1, column=0)
            self.lb2.grid(row=1, column=1)

    def jumpback(self):
        self.page.destroy()
        M.M_GUI(self.root)


class OnLine(object):
    def __init__(self, master=None):
        self.root = master  # 定义内部变量
        self.root.geometry('620x350+200+20')  # 设置窗口大小、位置
        self.root.title('选择上机')
        self.varIC = StringVar()  # 机位号
        self.varOT = StringVar()  # 上机时间
        self.back = Menu(self.root)  # 创建返回栏
        self.back.add_command(label='返回系统', command=self.jumpback)
        self.root['menu'] = self.back  # 设置返回菜单
        self.createpage()

    def createpage(self):
        self.page = Frame(self.root)
        self.page.pack()
        self.blank()

    def blank(self):
        Label(self.page, text='此处应为空闲机号').grid(row=1, column=1)  # .place(x=20, y=40)
        Label(self.page, text='机位').grid(row=0, column=0)  # 标签 .place(x=20, y=10)
        Entry(self.page, width=24, textvariable=self.varIC).grid(row=0, column=1)  # 文本框（id_c）
        Button(self.page, text='上机', width=4, height=2, command=self.getmsg).grid(row=0, column=50)

    def getmsg(self):
        if self.varIC.get() == '':
            showinfo(title='警告', message='请键入机位！')
        else:
            cur.execute("select id_c from c_sta where id_c =%s", self.varIC.get())
            self.data_id_c = cur.fetchall()
            if str(self.data_id_c) == '()':
                showinfo(title='错误', message='不存在此机位！')
            else:
                cur.execute("select id_c from c_sta where id_c =%s and ocu ='N'", self.varIC.get())
                self.data_id_c = cur.fetchall()
                if str(self.data_id_c) == '()':
                    showinfo(title='错误', message='该机位已上机！')
                else:
                    cur.execute("update c_sta set ocu ='Y' where id_c =%s", self.varIC.get())
                    self.varOT = datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")
                    self.ins = 'update c_sta set ont =\'' + self.varOT + '\' where id_c =' + self.varIC.get()
                    # print(self.ins)
                    cur.execute(self.ins)
                    # con.commit()  # **********************************************************************************
                    showinfo(title='提示', message=self.varIC.get()+'号成功上机！')
                    self.jumpback()
                    # print(self.varOT)

    def jumpback(self):
        self.page.destroy()
        M.M_GUI(self.root)


class OffLine(object):
    def __init__(self, master=None):
        self.root = master  # 定义内部变量
        self.root.geometry('620x350+200+20')  # 设置窗口大小、位置
        self.root.title('选择下机')
        self.varIC = StringVar()  # 机位号
        self.varFT = StringVar()  # 下机时间
        self.back = Menu(self.root)  # 创建返回栏
        self.back.add_command(label='返回系统', command=self.jumpback)
        self.root['menu'] = self.back  # 设置返回菜单
        self.createpage()

    def createpage(self):
        self.page = Frame(self.root)
        self.page.pack()
        self.blank()

    def blank(self):
        Label(self.page, text='此处应为已占机号').grid(row=1, column=1)  # .place(x=20, y=40)
        Label(self.page, text='机位').grid(row=0, column=0)  # 标签 .place(x=20, y=10)
        Entry(self.page, width=24, textvariable=self.varIC).grid(row=0, column=1)  # 文本框（id_c）
        Button(self.page, text='下机', width=4, height=2, command=self.getmsg).grid(row=0, column=50)

    def getmsg(self):
        if self.varIC.get() == '':
            showinfo(title='警告', message='请键入机位！')
        else:
            cur.execute("select id_c from c_sta where id_c =%s", self.varIC.get())
            self.data_id_c = cur.fetchall()
            if str(self.data_id_c) == '()':
                showinfo(title='错误', message='不存在此机位！')
            else:
                cur.execute("select id_c from c_sta where id_c =%s and ocu ='Y'", self.varIC.get())
                self.data_id_c = cur.fetchall()
                if str(self.data_id_c) == '()':
                    showinfo(title='错误', message='该机位已下机！')
                else:
                    cur.execute("update c_sta set ocu ='N' where id_c =%s", self.varIC.get())
                    self.varFT = datetime.datetime.today()  # .strftime("%Y-%m-%d %H:%M:%S")  # 获取当前datetime类的对象
                    self.varFT_s = self.varFT.strftime("%Y-%m-%d %H:%M:%S")  # 将获取到的对象转化为字符串
                    cur.execute('select netfee from rate')
                    self.varNF = cur.fetchall()
                    # ___________________________________________________________________________TABLE d_total__________
                    cur.execute("select ont from c_sta where id_c =%s", self.varIC.get())
                    self.varOT = cur.fetchall()[0][0]  # 获取到上机时的datetime对象
                    self.td = self.varFT - self.varOT  # 两个datetime对象相减，返回timedelta对象
                    # print(self.td.seconds*100)
                    self.ins = 'insert into d_total values(\'' + str(self.td) + '\', ' + str(self.td.seconds*self.varNF[0][0]) + ', ' + self.varIC.get() + ')'
                    # print(self.ins)
                    cur.execute(self.ins)
                    # __________________________________________________________________________________________________
                    self.ins = 'update c_sta set oft =\'' + self.varFT_s + '\' where id_c =' + self.varIC.get()
                    # print(self.ins)
                    cur.execute(self.ins)
                    self.ins = 'update c_sta set inco =inco+' + str(self.td.seconds*self.varNF[0][0]) + ' where id_c =' + self.varIC.get()
                    # print(self.ins)
                    cur.execute(self.ins)
                    # con.commit()  # **********************************************************************************
                    showinfo(title='费用——' + str(self.td.seconds) + '元', message=self.varIC.get()+'号成功下机！')
                    self.jumpback()

    def jumpback(self):
        self.page.destroy()
        M.M_GUI(self.root)


class AddCptr(object):
    def __init__(self, master=None):
        self.root = master  # 定义内部变量
        self.root.geometry('620x350+200+20')  # 设置窗口大小、位置
        self.root.title('添加机位')
        self.varIC = StringVar()  # 机位号
        self.back = Menu(self.root)  # 创建返回栏
        self.back.add_command(label='返回系统', command=self.jumpback)
        self.root['menu'] = self.back  # 设置返回菜单
        self.createpage()

    def createpage(self):
        self.page = Frame(self.root)
        self.page.pack()
        self.blank()

    def blank(self):
        Label(self.page, text='机位号').grid(row=0, column=0)  # 标签 .place(x=20, y=10)
        Entry(self.page, width=24, textvariable=self.varIC).grid(row=0, column=1)  # 文本框（id_c）
        Button(self.page, text='添加', width=4, height=2, command=self.getmsg).grid(row=0, column=50)

    def getmsg(self):
        if self.varIC.get() == '':
            showinfo(title='警告', message='请键入机位号！')
        else:
            cur.execute("select id_c from c_sta where id_c =%s", self.varIC.get())
            self.data_id_c = cur.fetchall()
            if str(self.data_id_c) != '()':
                showinfo(title='错误', message='已存在此机位！')
            else:
                try:
                    cur.execute("insert into c_sta values(%s, 'N', NULL, NULL, 0)", self.varIC.get())
                    # con.commit()  # **************************************************************************************
                    showinfo(title='提示', message='成功添加' + self.varIC.get() + '号机位！')
                    self.jumpback()
                except pymysql.err.InternalError:
                    showinfo(title='错误', message='请输入正确的格式！！')

    def jumpback(self):
        self.page.destroy()
        M.M_GUI(self.root)


class DelCptr(object):
    def __init__(self, master=None):
        self.root = master  # 定义内部变量
        self.root.geometry('620x350+200+20')  # 设置窗口大小、位置
        self.root.title('移除机位')
        self.varIC = StringVar()  # 机位号
        self.back = Menu(self.root)  # 创建返回栏
        self.back.add_command(label='返回系统', command=self.jumpback)
        self.root['menu'] = self.back  # 设置返回菜单
        self.createpage()

    def createpage(self):
        self.page = Frame(self.root)
        self.page.pack()
        self.blank()

    def blank(self):
        Label(self.page, text='机位号').grid(row=0, column=0)  # 标签 .place(x=20, y=10)
        Entry(self.page, width=24, textvariable=self.varIC).grid(row=0, column=1)  # 文本框（id_c）
        Button(self.page, text='移除', width=4, height=2, command=self.getmsg).grid(row=0, column=50)

    def getmsg(self):
        if self.varIC.get() == '':
            showinfo(title='警告', message='请键入机位号！')
        else:
            cur.execute("select id_c from c_sta where id_c =%s", self.varIC.get())
            self.data_id_c = cur.fetchall()
            if str(self.data_id_c) == '()':
                showinfo(title='错误', message='不存在此机位！')
            else:
                cur.execute("delete from c_sta where id_c =%s", self.varIC.get())
                # con.commit() # ***************************************************************************************
                showinfo(title='提示', message='成功移除' + self.varIC.get() + '号机位！')
                self.jumpback()

    def jumpback(self):
        self.page.destroy()
        M.M_GUI(self.root)


class showIncm_s(object):
    def __init__(self, master=None):
        self.root = master  # 定义内部变量
        self.root.geometry('620x350+200+20')  # 设置窗口大小、位置
        self.root.title('收入总和')
        self.varIC = StringVar()  # 机位号
        self.back = Menu(self.root)  # 创建返回栏
        self.back.add_command(label='返回系统', command=self.jumpback)
        self.root['menu'] = self.back  # 设置返回菜单
        self.createpage()

    def createpage(self):
        self.page = Frame(self.root)
        self.page.pack()
        self.blank()

    def blank(self):
        cur.execute('select count(ic_da) from d_total')  # 获取收入记录的个数
        self.data_count = cur.fetchall()
        if self.data_count[0][0] == 0:
            Label(self.page, text='目前还没有收入').grid(row=0, column=0)
        else:
            cur.execute("select sum(inco) from d_total")
            self.data_inco = str(cur.fetchall()[0][0]) + '元'
            Label(self.page, text=self.data_inco).grid(row=1, column=1)  # .place(x=20, y=40)

    def jumpback(self):
        self.page.destroy()
        M.M_GUI(self.root)


class ShowIncm(object):
    def __init__(self, master=None):
        self.root = master  # 定义内部变量
        self.root.geometry('620x350+200+20')  # 设置窗口大小、位置
        self.root.title('收入统计——分时')
        self.varIC = StringVar()  # 机位号
        self.back = Menu(self.root)  # 创建返回栏
        self.back.add_command(label='返回系统', command=self.jumpback)
        self.root['menu'] = self.back  # 设置返回菜单
        self.createpage()

    def createpage(self):
        self.page = Frame(self.root)
        self.page.pack()
        self.getmsg()

    def getmsg(self):
        cur.execute('select count(ic_da) from d_total')  # 获取收入记录的个数
        self.data_count = cur.fetchall()
        cur.execute('select id_c from d_total')  # 获取所有收入对应的机位
        self.data_id_c = cur.fetchall()
        cur.execute('select ic_da from d_total')  # 获取所有收入时间的记录
        self.data_ic_da = cur.fetchall()
        cur.execute('select inco from d_total')  # 获取所有收入的记录
        self.data_inco= cur.fetchall()

        if self.data_count[0][0] == 0:
            Label(self.page, text='目前还没有收入').grid(row=0, column=0)
        else:
            Label(self.page, text='上机时长').grid(row=0, column=0)
            Label(self.page, text='收入记录').grid(row=0, column=1)
            Label(self.page, text='机位指向').grid(row=0, column=2)
            self.lb = Listbox(self.page, width=17, height=self.data_count[0][0], selectmode=EXTENDED)
            self.lb2 = Listbox(self.page, width=10, height=self.data_count[0][0], selectmode=EXTENDED)
            self.lb3 = Listbox(self.page, width=5, height=self.data_count[0][0], selectmode=EXTENDED)
            self.lb4 = Listbox(self.page, width=20, height=self.data_count[0][0], selectmode=EXTENDED)
            for n in self.data_ic_da:
                self.lb.insert(END, n[0])
            for i in self.data_inco:
                self.lb2.insert(END, i[0])
            for j in self.data_id_c:
                self.lb3.insert(END, j[0])

            self.lb.grid(row=1, column=0)
            self.lb2.grid(row=1, column=1)
            self.lb3.grid(row=1, column=2)


    def jumpback(self):
        self.page.destroy()
        M.M_GUI(self.root)


class showIncm_i(object):
    def __init__(self, master=None):
        self.root = master  # 定义内部变量
        self.root.geometry('620x350+200+20')  # 设置窗口大小、位置
        self.root.title('收入统计——机位')
        self.varIC = StringVar()  # 机位号
        self.back = Menu(self.root)  # 创建返回栏
        self.back.add_command(label='返回系统', command=self.jumpback)
        self.root['menu'] = self.back  # 设置返回菜单
        self.createpage()

    def createpage(self):
        self.page = Frame(self.root)
        self.page.pack()
        self.getmsg()

    def getmsg(self):
        cur.execute('select count(id_c) from c_sta')  # 获取收入记录的个数
        self.data_count = cur.fetchall()
        cur.execute('select id_c from c_sta')  # 获取所有收入时间的记录
        self.data_id_c = cur.fetchall()
        cur.execute('select inco from c_sta')  # 获取所有收入时间的记录
        self.data_incm = cur.fetchall()

        if self.data_count[0][0] == 0:
            Label(self.page, text='目前还没有机位').grid(row=0, column=0)
        else:
            Label(self.page, text='机位').grid(row=0, column=0)
            Label(self.page, text='收入').grid(row=0, column=1)
            self.lb = Listbox(self.page, width=5, height=self.data_count[0][0], selectmode=EXTENDED)
            self.lb2 = Listbox(self.page, width=10, height=self.data_count[0][0], selectmode=EXTENDED)
            for n in self.data_id_c:
                self.lb.insert(END, n[0])
            for i in self.data_incm:
                if i[0] == 0.0:
                    self.lb2.insert(END, ' ')
                else:
                    self.lb2.insert(END, i[0])

            self.lb.grid(row=1, column=0)
            self.lb2.grid(row=1, column=1)

    def jumpback(self):
        self.page.destroy()
        M.M_GUI(self.root)


class SetFee(object):
    def __init__(self, master=None):
        self.root = master  # 定义内部变量
        self.root.geometry('620x350+200+20')  # 设置窗口大小、位置
        self.root.title('设定费率')
        self.varNF = StringVar()  # 上网费率
        self.back = Menu(self.root)  # 创建返回栏
        self.back.add_command(label='返回系统', command=self.jumpback)
        self.root['menu'] = self.back  # 设置返回菜单
        self.createpage()

    def createpage(self):
        self.page = Frame(self.root)
        self.page.pack()
        self.blank()

    def blank(self):
        cur.execute('select netfee from rate')
        self.varNF.set(cur.fetchall()[0][0])
        Label(self.page, text='费率').grid(row=0, column=0)  # 标签 .place(x=20, y=10)
        Entry(self.page, width=24, textvariable=self.varNF).grid(row=0, column=1)  # 文本框（id_c）
        Button(self.page, text='设定', width=4, height=2, command=self.getmsg).grid(row=0, column=50)

    def getmsg(self):
        try:
            if float(self.varNF.get()) <= 0:
                showinfo(title='错误', message='请输入正确的费率！')
            else:
                cur.execute("update rate set netfee =%s", self.varNF.get())
                # con.commit() # ***************************************************************************************
                showinfo(title='提示', message=self.varNF.get() + '元/分钟')
                self.jumpback()
        except ValueError:
            showinfo(title='错误', message='请输入正确的格式！')

    def jumpback(self):
        self.page.destroy()
        M.M_GUI(self.root)
