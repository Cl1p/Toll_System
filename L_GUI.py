# encoding: utf-8

from M_GUI import *
from tkinter.messagebox import *


class L_GUI(object):
    def __init__(self, master=None):
        self.root = master  # 定义一个内部变量root
        self.root.geometry()
        self.root.title('系统入口')
        self.varA = StringVar()
        self.varP = StringVar()
        self.ins = StringVar()
        self.createPage()

    def createPage(self):
        self.page = Frame(self.root)
        self.page.pack()
        Label(self.page, text='账号').grid(row=0, column=0)  # 标签 .place(x=20, y=10)
        Label(self.page, text='密码').grid(row=1, column=0)  # .place(x=20, y=40)
        self.AC = Entry(self.page, width=24, textvariable=self.varA).grid(row=0, column=1)  # 文本框（账号）
        self.PS = Entry(self.page, width=24, textvariable=self.varP, show='*').grid(row=1, column=1)  # 文本框（密码）
        Button(self.page, text='登录', width=4, height=2, command=self.loginCheck).grid(row=0, column=50, rowspan=4)

    def loginCheck(self):
        cur.execute("select psw from stu where sno = %s", self.varA.get())
        self.data_a = cur.fetchall()
        if str(self.data_a) != '()':
            if self.varP.get() == '':
                showinfo(title='错误', message='请填写密码!')  # M_method_1
            elif str(self.data_a[0][0]) == self.varP.get():
                self.page.destroy()
                self.page.destroy()
                M_GUI(self.root)
            else:
                showinfo(title='错误', message='密码错误！')
        else:
            if self.varA.get() == '':
                showinfo(title='错误', message='请填写账号!')  # M_method_1
            else:
                showinfo(title='错误', message='此账号不存在！')  # M_method_1
