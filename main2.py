#导入wx模块
import wx
import wx.grid
from db import Sql_operation
import os
#import pymysql
import tkinter
import tkinter.messagebox
from  tkinter  import ttk
class UserLogin(wx.Frame):
	
	#初始化登录界面
	def __init__(self,*args,**kw):
		# ensure the parent's __init__ is called
		super(UserLogin,self).__init__(*args, **kw)
		#设置窗口屏幕居中
		self.Center()
		#创建窗口
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVECAPTION ) )
		self.pnl = wx.Panel(self)
		#调用登录界面函数
		self.LoginInterface()

	def LoginInterface(self):
		#创建垂直方向box布局管理器
		vbox = wx.BoxSizer(wx.VERTICAL)
		#################################################################################
		#创建logo静态文本，设置字体属性
		logo = wx.StaticText(self.pnl,label="桥梁管理系统")
		logo.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )
		font = logo.GetFont()
		font.PointSize += 30
		font = font.Bold()
		logo.SetFont(font)
		#添加logo静态文本到vbox布局管理器
		vbox.Add(logo,proportion=0,flag=wx.FIXED_MINSIZE | wx.TOP | wx.CENTER,border=180)
		#################################################################################
		#创建静态框
		sb_username = wx.StaticBox(self.pnl,label="用户名")
		sb_password = wx.StaticBox(self.pnl,label="密  码")		
		#创建水平方向box布局管理器
		hsbox_username = wx.StaticBoxSizer(sb_username,wx.HORIZONTAL)
		hsbox_password = wx.StaticBoxSizer(sb_password,wx.HORIZONTAL)
		#创建用户名、密码输入框
		self.user_name = wx.TextCtrl(self.pnl,size=(210,25))
		self.user_password = wx.TextCtrl(self.pnl,size=(210,25))
		#添加用户名和密码输入框到hsbox布局管理器
		hsbox_username.Add(self.user_name,0,wx.EXPAND | wx.BOTTOM,5)
		hsbox_password.Add(self.user_password,0,wx.EXPAND | wx.BOTTOM,5)
		#将水平box添加到垂直box
		vbox.Add(hsbox_username,proportion=0,flag=wx.CENTER)
		vbox.Add(hsbox_password,proportion=0,flag=wx.CENTER)
		#################################################################################
		#创建水平方向box布局管理器
		hbox = wx.BoxSizer()
		#创建登录按钮、绑定事件处理
		login_button = wx.Button(self.pnl,label="登录",size=(80,25))
		login_button.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVECAPTION ) )
		regis_button = wx.Button(self.pnl,label="注册",size=(80,25))
		regis_button.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVECAPTION ) )
		login_button.Bind(wx.EVT_BUTTON,self.LoginButton)
		regis_button.Bind(wx.EVT_BUTTON,self.RegisButton)
		#添加登录按钮到hbox布局管理器
		hbox.Add(login_button,0,flag=wx.EXPAND | wx.TOP,border=5)
		hbox.Add(regis_button,0,flag=wx.EXPAND | wx.TOP,border=5)
		
		#将水平box添加到垂直box
		vbox.Add(hbox,proportion=0,flag=wx.CENTER)
		#################################################################################
		#设置面板的布局管理器vbox		
		self.pnl.SetSizer(vbox)		

	def RegisButton(self,event):
		#连接bridge_db数据库
		op = Sql_operation("bridge_db")
		user_name = self.user_name.GetValue()
		user_password = self.user_password.GetValue()
		np = op.FindAll("users")
		regist=0
		for i in np:
                        if i[1] == self.user_name.GetValue():
                                regist=1
		if len(user_name)<=10 and regist==0:
			if len(user_password)<=12:
				np = op. InsertUser(user_name,user_password)
				tkinter.messagebox.showinfo('提示','注册成功')
		else:
			#if regist==1:
                                		#tkinter.messagebox.showinfo('提示','用户名重复')
			tkinter.messagebox.showinfo('提示','注册失败')
	
	def LoginButton(self,event):
		#连接student_db数据库
		op = Sql_operation("bridge_db")
		#获取users表中的用户名和密码信息，返回为二维元组
		np = op.FindAll("users")
		#匹配标记
		login_sign = 0
		print(np)
		#匹配用户名和密码
		for i in np:	
			if (i[1] == self.user_name.GetValue()) and (i[2] == self.user_password.GetValue() and i[0] == 1):
				login_sign = 1
				break
			elif (i[1] == self.user_name.GetValue()) and (i[2] == self.user_password.GetValue() and i[0] == 2):
				login_sign = 2
				break
		if login_sign == 0:
			print("用户名或密码错误！")
		elif (login_sign) == 1:
			print("登录成功！")			
			operation = UserOperation(None,title="桥梁管理系统(管理员)",size=(1024,668))
			operation.Show()
			self.Close(True)
		elif (login_sign) == 2:
			os.system(r"python C:\Users\葡萄\main3.py")

class UserOperation(wx.Frame):
	'''
	操作界面
	'''
	def __init__(self,*args,**kw):
		# ensure the parent's __init__ is called
		super(UserOperation,self).__init__(*args, **kw)
		#设置窗口屏幕居中
		self.Center()
		#创建窗口
		self.pnl = wx.Panel(self)
		#调用操作界面函数
		self.OperationInterface()

	def OperationInterface(self):
		#创建垂直方向box布局管理器
		self.vbox = wx.BoxSizer(wx.VERTICAL)		
		#################################################################################
		#创建logo静态文本，设置字体属性
		logo = wx.StaticText(self.pnl,label="桥梁管理系统(管理员)")
		logo.SetForegroundColour(wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		font = logo.GetFont()
		font.PointSize += 30
		font = font.Bold()
		logo.SetFont(font)
		#添加logo静态文本到vbox布局管理器
		self.vbox.Add(logo,proportion=0,flag=wx.FIXED_MINSIZE | wx.TOP | wx.CENTER,border=5)
		#################################################################################
		#创建静态框
		sb_button = wx.StaticBox(self.pnl,label="选择操作")
		#创建垂直方向box布局管理器
		vsbox_button = wx.StaticBoxSizer(sb_button,wx.VERTICAL)
		#创建操作按钮、绑定事件处理
		check_button = wx.Button(self.pnl,id=10,label="查看桥梁信息",size=(150,50))
		add_button = wx.Button(self.pnl,id=11,label="添加桥梁信息",size=(150,50))
		delete_button = wx.Button(self.pnl,id=12,label="删除桥梁信息",size=(150,50))
		update_button = wx.Button(self.pnl,id=13,label="修改桥梁信息",size=(150,50))
		quit_button = wx.Button(self.pnl,id=14,label="查询地址",size=(150,50))
		dizhi_button = wx.Button(self.pnl,id=15,label="退出系统",size=(150,50))
		self.Bind(wx.EVT_BUTTON,self.ClickButton,id=10,id2=15)
		#添加操作按钮到vsbox布局管理器
		vsbox_button.Add(check_button,0,wx.EXPAND | wx.BOTTOM,20)
		vsbox_button.Add(add_button,0,wx.EXPAND | wx.BOTTOM,20)
		vsbox_button.Add(delete_button,0,wx.EXPAND | wx.BOTTOM,20)
		vsbox_button.Add(update_button,0,wx.EXPAND | wx.BOTTOM,20)
		vsbox_button.Add(quit_button,0,wx.EXPAND | wx.BOTTOM,20)
		vsbox_button.Add(dizhi_button,0,wx.EXPAND | wx.BOTTOM,20)		
		#创建静态框
		sb_show_operation = wx.StaticBox(self.pnl,label="显示/操作窗口",size=(800,1000))
		#创建垂直方向box布局管理器
		self.vsbox_show_operation = wx.StaticBoxSizer(sb_show_operation,wx.VERTICAL)
		#创建水平方向box布局管理器
		hbox = wx.BoxSizer()
		hbox.Add(vsbox_button,0,wx.EXPAND | wx.BOTTOM,5)
		hbox.Add(self.vsbox_show_operation,0,wx.EXPAND | wx.BOTTOM,5)
		#将hbox添加到垂直box		
		self.vbox.Add(hbox,proportion=0,flag=wx.CENTER)		
		#################################################################################
		self.pnl.SetSizer(self.vbox)

	def ClickButton(self,event):
		source_id = event.GetId()
		if source_id == 10:
			print("查询操作！")
			inquire_button = InquireOp(None,title="桥梁管理系统(管理员)",size=(1024,668))
			inquire_button.Show()
			self.Close(True)			
		elif source_id == 11:
			print("添加操作！")
			add_button = AddOp(None,title="桥梁管理系统(管理员)",size=(1024,668))
			add_button.Show()
			self.Close(True)						
		elif source_id == 12:
			print("删除操作！")
			del_button = DelOp(None,title="桥梁管理系统(管理员)",size=(1024,668))
			del_button.Show()
			self.Close(True)	
		elif source_id == 13:
			print("修改操作！")
			del_button = UpdOp(None,title="桥梁管理系统(管理员)",size=(1024,668))
			del_button.Show()
			self.Close(True)
		elif source_id == 14:
			print("查询地址操作！")
			del_button=os.system(r"python C:\Users\葡萄\Panel_Seleninum.py")
		elif source_id == 15:
			self.Close(True)

#继承UserOperation类，实现初始化操作界面
class InquireOp(UserOperation):
#class InquireOp(InquireOp):
	def __init__(self,*args,**kw):
		# ensure the parent's __init__ is called
		super(InquireOp,self).__init__(*args, **kw)
		#创建桥梁列表信息网格
		self.stu_grid = self.CreateGrid()
		self.stu_grid.Bind(wx.grid.EVT_GRID_LABEL_LEFT_CLICK,self.OnLabelleftClick)
		#添加到vsbox_show_operation布局管理器
		self.vsbox_show_operation.Add(self.stu_grid,0,wx.CENTER | wx.TOP | wx.FIXED_MINSIZE,30)		

	def ClickButton(self,event):
		source_id = event.GetId()
		if source_id == 10:
			pass						
		elif source_id == 11:
			print("添加操作！")
			add_button = AddOp(None,title="桥梁管理系统(管理员)",size=(1024,668))
			add_button.Show()
			self.Close(True)						
		elif source_id == 12:
			print("删除操作！")
			del_button = DelOp(None,title="桥梁管理系统(管理员)",size=(1024,668))
			del_button.Show()
			self.Close(True)
		elif source_id == 13:
			print("修改操作！")
			del_button = UpdOp(None,title="桥梁管理系统(管理员)",size=(1024,668))
			del_button.Show()
			self.Close(True)
		elif source_id == 14:
			print("查询地址操作！")
			del_button=os.system(r"python C:\Users\葡萄\Panel_Seleninum.py")
		elif source_id == 15:
			self.Close(True)

	def CreateGrid(self):
		#连接student_db数据库
		op = Sql_operation("bridge_db")
		#获取Paper表中的桥梁信息，返回为二维元组
		np = op.FindAll("paper")
		column_names = ("bridgename","detecttime","bridgerate","mainbroken","askmoney","reason4askmoney")
		stu_grid = wx.grid.Grid(self.pnl)
		stu_grid.CreateGrid(len(np),len(np[0])-1)
		for row in range(len(np)):
			stu_grid.SetRowLabelValue(row,str(np[row][0]))#确保网格序列号与数据库id保持一致
			for col in range(1,len(np[row])):
				stu_grid.SetColLabelValue(col-1,column_names[col-1])
				stu_grid.SetCellValue(row,col-1,str(np[row][col]))				
		stu_grid.AutoSize()
		return stu_grid

	def OnLabelleftClick(self,event):
		#连接student_db数据库
		op = Sql_operation("bridge_db")
		#获取users表中的用户名和密码信息，返回为二维元组
		np = op.FindAll("users")
		print("RowIdx: {0}".format(event.GetRow()))
		print("ColIdx: {0}".format(event.GetRow()))
		print(np[event.GetRow()])
		event.Skip()

#继承UserOperation类，实现初始化操作界面
class AddOp(UserOperation):
#class AddOp(InquireOp):
	def __init__(self,*args,**kw):
		# ensure the parent's __init__ is called
		super(AddOp,self).__init__(*args, **kw)
		#创建添加桥梁息输入框、添加按钮
		self.id = wx.TextCtrl(self.pnl,size = (210,25))
		self.bridgename = wx.TextCtrl(self.pnl,size = (210,25))
		self.detecttime = wx.TextCtrl(self.pnl,size = (210,25))
		self.bridgerate = wx.TextCtrl(self.pnl,size = (210,25))
		self.mainbroken = wx.TextCtrl(self.pnl,size = (210,25))
		self.askmoney = wx.TextCtrl(self.pnl,size = (210,25))
		self.reason4askmoney = wx.TextCtrl(self.pnl,size = (210,25))
		self.add_affirm = wx.Button(self.pnl,label="添加",size=(80,25))
		#为添加按钮组件绑定事件处理
		self.add_affirm.Bind(wx.EVT_BUTTON,self.AddAffirm)
		#################################################################################
		#创建静态框
		sb_id = wx.StaticBox(self.pnl,label="id")
		sb_name = wx.StaticBox(self.pnl,label="桥名")
		sb_gender = wx.StaticBox(self.pnl,label="检测时间")
		sb_age = wx.StaticBox(self.pnl,label="项目评级")
		sb_cid = wx.StaticBox(self.pnl,label="主要问题")
		sb_classid = wx.StaticBox(self.pnl,label="申报费用")
		sb_phone = wx.StaticBox(self.pnl,label="申报陈述")		
		#创建水平方向box布局管理器
		hsbox_id = wx.StaticBoxSizer(sb_id,wx.HORIZONTAL)
		hsbox_name = wx.StaticBoxSizer(sb_name,wx.HORIZONTAL)
		hsbox_gender = wx.StaticBoxSizer(sb_gender,wx.HORIZONTAL)
		hsbox_age = wx.StaticBoxSizer(sb_age,wx.HORIZONTAL)
		hsbox_cid = wx.StaticBoxSizer(sb_cid,wx.HORIZONTAL)
		hsbox_classid = wx.StaticBoxSizer(sb_classid,wx.HORIZONTAL)
		hsbox_phone = wx.StaticBoxSizer(sb_phone,wx.HORIZONTAL)
		#添加到hsbox布局管理器
		hsbox_id.Add(self.id,0,wx.EXPAND | wx.BOTTOM,5)
		hsbox_name.Add(self.bridgename,0,wx.EXPAND | wx.BOTTOM,5)
		hsbox_gender.Add(self.detecttime,0,wx.EXPAND | wx.BOTTOM,5)
		hsbox_age.Add(self.bridgerate,0,wx.EXPAND | wx.BOTTOM,5)
		hsbox_cid.Add(self.mainbroken,0,wx.EXPAND | wx.BOTTOM,5)
		hsbox_classid.Add(self.askmoney,0,wx.EXPAND | wx.BOTTOM,5)
		hsbox_phone.Add(self.reason4askmoney,0,wx.EXPAND | wx.BOTTOM,5)
		#################################################################################
		#添加到vsbox_show_operation布局管理器
		self.vsbox_show_operation.Add(hsbox_id,0,wx.CENTER | wx.TOP | wx.FIXED_MINSIZE,5)
		self.vsbox_show_operation.Add(hsbox_name,0,wx.CENTER | wx.TOP | wx.FIXED_MINSIZE,5)
		self.vsbox_show_operation.Add(hsbox_gender,0,wx.CENTER | wx.TOP | wx.FIXED_MINSIZE,5)
		self.vsbox_show_operation.Add(hsbox_age,0,wx.CENTER | wx.TOP | wx.FIXED_MINSIZE,5)
		self.vsbox_show_operation.Add(hsbox_cid,0,wx.CENTER | wx.TOP | wx.FIXED_MINSIZE,5)
		self.vsbox_show_operation.Add(hsbox_classid,0,wx.CENTER | wx.TOP | wx.FIXED_MINSIZE,5)
		self.vsbox_show_operation.Add(hsbox_phone,0,wx.CENTER | wx.TOP | wx.FIXED_MINSIZE,5)
		self.vsbox_show_operation.Add(self.add_affirm,0,wx.CENTER | wx.TOP | wx.FIXED_MINSIZE,5)

	def ClickButton(self,event):
		source_id = event.GetId()
		if source_id == 10:
			print("查询操作！")
			inquire_button = InquireOp(None,title="桥梁管理系统(管理员)",size=(1024,668))
			inquire_button.Show()
			self.Close(True)			
		elif source_id == 11:
			pass						
		elif source_id == 12:
			print("删除操作！")
			del_button = DelOp(None,title="桥梁管理系统(管理员)",size=(1024,668))
			del_button.Show()
			self.Close(True)
		elif source_id == 13:
			print("修改操作！")
			del_button = UpdOp(None,title="桥梁管理系统(管理员)",size=(1024,668))
			del_button.Show()
			self.Close(True)
		elif source_id == 14:
			print("查询地址操作！")
			del_button=os.system(r"python C:\Users\葡萄\Panel_Seleninum.py")
		elif source_id == 15:
			self.Close(True)

	def AddAffirm(self,event):
		#连接bridge_db数据库
		op = Sql_operation("bridge_db")
		#向Paper表添加桥梁信息
		bridgename = self.bridgename.GetValue()
		print(bridgename)
		detecttime = self.detecttime.GetValue()
		print(detecttime)
		bridgerate = self.bridgerate.GetValue()
		print(bridgerate)
		mainbroken = self.mainbroken.GetValue()
		print(mainbroken)
		askmoney = self.askmoney.GetValue()
		print(askmoney)
		reason4askmoney = self.reason4askmoney.GetValue()
		print(reason4askmoney)
		#np = op.Insert(bridgename,detecttime,bridgerate,mainbroken,askmoney,reason4askmoney)
		id = self.id.GetValue()
		print(id)
		np = op.Insert(bridgename,detecttime,bridgerate,mainbroken,askmoney,reason4askmoney,id)

#继承InquireOp类，实现初始化操作界面
class DelOp(InquireOp):
	def __init__(self,*args,**kw):
		# ensure the parent's __init__ is called
		super(DelOp,self).__init__(*args, **kw)
		#创建删除桥梁信息输入框、删除按钮
		self.del_id = wx.TextCtrl(self.pnl,pos = (407,78),size = (210,25))
		self.del_affirm = wx.Button(self.pnl,label="删除",pos=(625,78),size=(80,25))
		#为删除按钮组件绑定事件处理
		self.del_affirm.Bind(wx.EVT_BUTTON,self.DelAffirm)
		#################################################################################
		#创建静态框
		sb_del = wx.StaticBox(self.pnl,label="请输入需要删除的桥梁的ID")
		#创建水平方向box布局管理器
		hsbox_del = wx.StaticBoxSizer(sb_del,wx.HORIZONTAL)
		#添加到hsbox_name布局管理器
		hsbox_del.Add(self.del_id,0,wx.EXPAND | wx.BOTTOM,5)
		#添加到vsbox_show_operation布局管理器
		self.vsbox_show_operation.Add(hsbox_del,0,wx.CENTER | wx.TOP | wx.FIXED_MINSIZE,5)
		self.vsbox_show_operation.Add(self.del_affirm,0,wx.CENTER | wx.TOP | wx.FIXED_MINSIZE,5)

	def ClickButton(self,event):
		source_id = event.GetId()
		if source_id == 10:
			print("查询操作！")
			inquire_button = InquireOp(None,title="桥梁管理系统",size=(1024,668))
			inquire_button.Show()
			self.Close(True)			
		elif source_id == 11:
			print("添加操作！")
			add_button = AddOp(None,title="桥梁管理系统",size=(1024,668))
			add_button.Show()
			self.Close(True)						
		elif source_id == 12:
			pass
		elif source_id == 13:
			print("修改操作！")
			del_button = UpdOp(None,title="桥梁管理系统",size=(1024,668))
			del_button.Show()
			self.Close(True)
		elif source_id == 14:
			print("查询地址操作！")
			del_button=os.system(r"python C:\Users\葡萄\Panel_Seleninum.py")
		elif source_id == 15:
			self.Close(True)

	def DelAffirm(self,event):
		#连接bridge_db数据库
		op = Sql_operation("bridge_db")

		del_id = self.del_id.GetValue()
		print(del_id)
		np = op.Del(int(del_id))
		
		del_button = DelOp(None,title="桥梁管理系统",size=(1024,668))
		del_button.Show()
		self.Close(True)

class UpdOp(InquireOp):
	def __init__(self,*args,**kw):
		# ensure the parent's __init__ is called
		super(UpdOp,self).__init__(*args, **kw)
		#创建添加桥梁息输入框、添加按钮
		self.id = wx.TextCtrl(self.pnl,size = (210,25))
		self.update_name = wx.StaticText(self.pnl,label='选择你要修改的信息',size = (210,25))
		self.update_acc = wx.TextCtrl(self.pnl,size = (210,25))
		self.add_affirm = wx.Button(self.pnl,label="确认更新",pos=(550,520),size=(80,25))
		#为添加按钮组件绑定事件处理
		self.add_affirm.Bind(wx.EVT_BUTTON,self.UpdateAffirm)

		#################################################################################
                               #创建静态框
		list=['askmoney','bridgename','detecttime','bridgerate','mainbrokrn','reason4askmoney']
		ch2=wx.Choice(self.pnl,-1,choices=list)

		sb_id = wx.StaticBox(self.pnl,label="需要更新的桥梁id")
		sb_name = wx.StaticBox(self.pnl,label="需要更新的桥梁信息")
		sb_acc = wx.StaticBox(self.pnl,label="更新的内容")		
		#创建水平方向box布局管理器
		hsbox_id  = wx.StaticBoxSizer(sb_id,wx.HORIZONTAL)
		hsbox_name = wx.StaticBoxSizer(sb_name,wx.VERTICAL)
		hsbox_acc = wx.StaticBoxSizer(sb_acc,wx.HORIZONTAL)
		self.Bind(wx.EVT_CHOICE,self.on_choice,ch2)
		#添加到hsbox布局管理器
		hsbox_id .Add(self.id,0,wx.EXPAND | wx.BOTTOM,5)
		hsbox_name.Add(self.update_name,1,flag=wx.LEFT |wx.RIGHT|wx.FIXED_MINSIZE,border=5)
		hsbox_name.Add(ch2,1,flag=wx.LEFT |wx.RIGHT|wx.FIXED_MINSIZE,border=5)
		hsbox_acc.Add(self.update_acc,0,wx.EXPAND | wx.BOTTOM,5)
		
		#################################################################################
		#添加到vsbox_show_operation布局管理器
		self.vsbox_show_operation.Add(hsbox_id,0,wx.CENTER | wx.TOP | wx.FIXED_MINSIZE,5)
		self.vsbox_show_operation.Add(hsbox_name,0,wx.CENTER | wx.TOP | wx.FIXED_MINSIZE,5)
		self.vsbox_show_operation.Add(hsbox_acc,0,wx.CENTER | wx.TOP | wx.FIXED_MINSIZE,5)
		
	def on_choice(self,event):
		self.h=event.GetString()
	def ClickButton(self,event):
		source_id = event.GetId()
		if source_id == 10:
			print("查询操作！")
			inquire_button = InquireOp(None,title="桥梁管理系统(管理员)",size=(1024,668))
			inquire_button.Show()
			self.Close(True)			
		elif source_id == 11:
			pass						
		elif source_id == 12:
			print("删除操作！")
			del_button = DelOp(None,title="桥梁管理系统(管理员)",size=(1024,668))
			del_button.Show()
			self.Close(True)
		elif source_id == 13:
			pass
		elif source_id == 14:
			print("查询地址操作！")
			del_button=os.system(r"python C:\Users\葡萄\Panel_Seleninum.py")
		elif source_id == 15:
			self.Close(True)

	def UpdateAffirm(self,event):
		#连接bridge_db数据库
		op = Sql_operation("bridge_db")
		update_name = self.h
		print(update_name)
		update_acc = self.update_acc.GetValue()
		print(update_acc)
		id = self.id.GetValue()
		print(id)
		op = op.Update(id,update_name,update_acc)
		
if __name__ == '__main__':
	app = wx.App()
	login = UserLogin(None,title="桥梁管理系统(管理员)",size=(1024,668))
	login.Show()
	app.MainLoop()
