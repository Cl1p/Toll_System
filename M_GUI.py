# encoding: utf-8
from InfoPage import *


class M_GUI(object):
    def __init__(self, master=None):
        self.root = master  # 定义内部变量
        self.root.geometry('620x350+200+20')  # 设置窗口大小、位置
        self.root.title('机房管理系统')
        self.ChoosePage()

    def ChoosePage(self):
        self.page = Frame(self.root)
        Label(self.page, text='请根据需要选择菜单项').grid(row=1, column=5)  # 标签
        self.createMenu()
        self.page.pack()

    def createMenu(self):
        self.bar = Menu(self.root)  # 创建主菜单
        self.menuUser = Menu(self.bar, tearoff=0)  # 创建用户子菜单
        self.menuUser.add_command(label='查看', command=self.jump1_1)
        self.menuUser.add_command(label='注册', command=self.jump1_2)
        self.menuUser.add_command(label='删除', command=self.jump1_3)
        self.menuUser.add_command(label='修改', command=self.jump1_4)
        self.bar.add_cascade(label='用户', menu=self.menuUser)  #
        self.menuCptr = Menu(self.bar, tearoff=0)  # 创建机位子菜单
        self.menuCptr_show = Menu(self.menuCptr, tearoff=0)  # 创建查看二级子菜单
        self.menuCptr_show.add_command(label='空闲', command=self.jump2_1_2)
        self.menuCptr_show.add_command(label='已占', command=self.jump2_1_1)
        self.menuCptr.add_cascade(label='查看', menu=self.menuCptr_show)  #
        self.menuCptr.add_separator()  # 分隔线
        self.menuCptr.add_command(label='上机', command=self.jump2_2)
        self.menuCptr.add_command(label='下机', command=self.jump2_3)
        self.menuCptr.add_separator()  # 分隔线
        self.menuCptr.add_command(label='新增', command=self.jump2_4)
        self.menuCptr.add_command(label='移除', command=self.jump2_5)
        self.bar.add_cascade(label='机位', menu=self.menuCptr)  #
        self.menuIncm = Menu(self.bar, tearoff=0)  # 创建收入子菜单
        self.menuIncm.add_command(label='求和', command=self.jump4_1)
        self.menuIncm.add_separator()  # 分隔线
        self.menuIncm.add_command(label='分时', command=self.jump3_1)
        self.menuIncm.add_command(label='机位', command=self.jump3_2)
        self.menuIncm.add_separator()  # 分隔线
        self.menuIncm.add_command(label='费率', command=self.jump4_2)
        self.bar.add_cascade(label='收入', menu=self.menuIncm)
        self.bar.add_command(label='退出', command=self.jump5)
        self.root['menu'] = self.bar        # 将主菜单设置为root窗口的菜单

    def jump1_1(self):
        self.page.destroy()
        ShowUser(self.root)

    def jump1_2(self):
        self.page.destroy()
        AddUser(self.root)

    def jump1_3(self):
        self.page.destroy()
        DelUser(self.root)

    def jump1_4(self):
        self.page.destroy()
        MdfyUser(self.root)

    def jump2_1_1(self):
        self.page.destroy()
        showCptr_E(self.root)  # employ

    def jump2_1_2(self):
        self.page.destroy()
        showCptr_L(self.root)  # leisure

    def jump2_2(self):
        self.page.destroy()
        OnLine(self.root)

    def jump2_3(self):
        self.page.destroy()
        OffLine(self.root)

    def jump2_4(self):
        self.page.destroy()
        AddCptr(self.root)

    def jump2_5(self):
        self.page.destroy()
        DelCptr(self.root)

    def jump3_1(self):
        self.page.destroy()
        ShowIncm(self.root)

    def jump3_2(self):
        self.page.destroy()
        showIncm_i(self.root)

    def jump4_1(self):
        self.page.destroy()
        showIncm_s(self.root)

    def jump4_2(self):
        self.page.destroy()
        SetFee(self.root)

    def jump5(self):
        exit()
