#-*- coding:utf-8 -*-
import pygame
import time
from pygame.locals import *
import random
"""
搭建主界面
"""
#飞机类
class BasePlane(object):
	def __init__(self,screen_tem,x,y,image):
		self.x = x  #飞机初始坐标
		self.y = y  #飞机初始坐标
		self.screen = screen_tem  #保存游戏窗口对象
		self.image = pygame.image.load(image)  #飞机图片
		self.bullet_list = []  #保存子弹
		self.bullet_over_list =[] #保存越界的子弹

	#显示飞机和子弹
	def display(self):
		#显示飞机
		self.screen.blit(self.image,(self.x,self.y))  #显示主角飞机
		
		#删除越界子弹
		if len(self.bullet_over_list) > 0: 
			for over_bullet in self.bullet_over_list:  
				self.bullet_list.remove(over_bullet)

		self.bullet_over_list.clear()  #清空越界子弹列表
		
		for bullet in self.bullet_list:
			bullet.display()  #显示子弹
			#bullet.y -=10
			bullet.move()  #子弹移动
			if bullet.judge():  #判断子弹移动后是否越界
				self.bullet_over_list.append(bullet)  #添加到子弹越界列表		

	#移动模式
	def move_mode(self):
		if self.flag == 0:
			self.x += 5
			if self.x >=378:  #移动到右边边界后将标记更改
				self.flag = 1
		elif self.flag == 1:
			self.x -= 5
			if self.x <= 0:  #移动到到左边边界后将标记更改
				self.flag =0

	#飞机向左移动
	def move_left(self):
		self.x-=5
	#飞机向右移动
	def move_right(self):
		self.x+=5
	#飞机向上移动
	def move_up(self):
		self.y-=5
	#飞机向下移动
	def move_down(self):
		self.y+=5

	#开火
	def fire(self):
		print("开火")
		#添加子弹列表
		self.bullet_list.append(Bullet(self.screen,self.x,self.y))

#子弹基类
class BaseBullet(object):
	"""子弹基类"""
	def __init__(self,screen_tem,x,y,image):
		self.x = x
		self.y = y
		self.screen = screen_tem
		self.image = pygame.image.load(image)	

	#子弹显示
	def display(self):
		self.screen.blit(self.image,(self.x,self.y))


class HeroPlane(BasePlane):
	"""主角飞机"""
	def __init__(self,screen_tem):
		BasePlane.__init__(self,screen_tem,200,600,"./images/hero/hero.png")		
		#被击中后使用的属性
		self.hit = False  #是否被击中，默认False
		self.image_num = 0  #图片显示计数
		self.boom_image_list = [] #飞机爆炸图片的列表
		self.image_index =0  #当前爆照图片的序号
		self.crate_boom_image()

	def crate_boom_image(self):
		self.boom_image_list.append("./images/boom/boss_down1.png")
		self.boom_image_list.append("./images/boom/boss_down2.png")
		self.boom_image_list.append("./images/boom/boss_down4.png")
		self.boom_image_list.append("./images/boom/boss_down6.png")

	def display(self):
		#显示飞机
		if self.hit == True:
			self.screen.blit(self.boom_list[self.image_index],(self.x,self.y))  #显示主角飞机
			self.image_num +=1
			if self.image_num >=7:
				self.image_num =0
				self.image_index +=1
			if self.image_index >3:
				exit()
		else:
			self.screen.blit(self.image,(self.x,self.y))  #显示主角飞机
		
		#删除越界子弹
		if len(self.bullet_over_list) > 0: 
			for over_bullet in self.bullet_over_list:  
				self.bullet_list.remove(over_bullet)

		self.bullet_over_list.clear()  #清空越界子弹列表
		
		for bullet in self.bullet_list:
			bullet.display()  #显示子弹
			#bullet.y -=10
			bullet.move()  #子弹移动
			if bullet.judge():  #判断子弹移动后是否越界
				self.bullet_over_list.append(bullet)  #添加到子弹越界列表


#敌机
class EnemyPlane(BasePlane):
	"""敌人飞机"""
	def __init__(self,screen_tem):
		BasePlane.__init__(self,screen_tem,0,0,"./images/enemy/enemy.png")

		self.flag = 0  #左右移动方向标记，0向右移动，1向左移动

	#移动模式
	def move_mode(self):
		if self.flag == 0:
			self.x += 5
			if self.x >=378:  #移动到右边边界后将标记更改
				self.flag = 1
		elif self.flag == 1:
			self.x -= 5
			if self.x <= 0:  #移动到到左边边界后将标记更改
				self.flag =0
		
		#self.y += 1	

	#开火
	def fire(self):		
		#控制子弹频率
		random_num = random.randint(1,50)
		if random_num ==1 or random_num ==10:
			print("敌机开火")
			self.bullet_list.append(EnemyBullet(self.screen,self.x,self.y))


#玩家子弹
class Bullet(BaseBullet):
	def __init__(self,screen_tem,x,y):
		BaseBullet.__init__(self,screen_tem,x+28,y-30,"./images/bullet/hero_bullet4.png")

	def move(self):
		self.y-=10

	def judge(self):
		if self.y <0:
			return True
		else:
			return False


#敌机子弹
class EnemyBullet(BaseBullet):
	def __init__(self,screen_tem,x,y):
		BaseBullet.__init__(self,screen_tem,x+42,y+88,"./images/bullet/enemy_bullet.png")
        
	def move(self):
		self.y+=10

	def judge(self):
		if self.y >854:
			return True
		else:
			return False

def key_control(hero_tem):
	#获取操作时间
	for event in pygame.event.get():
		#检测是不是点击了关闭按钮
		if event.type == pygame.QUIT:
			print("exit")
			exit()

		#检测按键
		elif event.type == pygame.KEYDOWN:
			#检测左方向键
			if event.key == K_a or event.key == K_LEFT:
				print("left")
				if hero_tem.x >=0:
					hero_tem.move_left()
			#检测右方向键
			elif event.key == K_d or event.key == K_RIGHT:
				print("right")
				if hero_tem.x <=380:
					hero_tem.move_right()
			#检测上方向键
			elif event.key == K_w or event.key == K_UP:
				print("up")
				if hero_tem.y >=0:
					hero_tem.move_up()
			#检测下方向键
			elif event.key == K_s or event.key == K_DOWN:
				print("down")
				if hero_tem.y <=645:
					hero_tem.move_down()
					print(hero_tem.y)
			#检测空格
			elif event.key == K_SPACE:
				print("space")
				hero_tem.fire()


def main():
	#创建一个窗口，显示游戏内容
	screen = pygame.display.set_mode((480,854),0,32)

	#创建背景图
	background = pygame.image.load("./images/bg/主界面.jpg")
	#创建主角飞机对象
	hero = HeroPlane(screen)
	enemy = EnemyPlane(screen)

	while True:
		#将背景图放到窗口中显示
		screen.blit(background,(0,0))
		#显示主角飞机
		hero.display()
		#显示敌人飞机
		enemy.display()
		#敌机移动
		enemy.move_mode()
		enemy.fire()
		#更新显示内容
		pygame.display.update()
		#键盘操作事件处理-移动开火
		key_control(hero)
		#优化一下性能，减少cpu负担
		time.sleep(0.02)

if __name__ == '__main__':
	main()