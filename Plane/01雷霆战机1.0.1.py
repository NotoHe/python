#-*- coding:utf-8 -*-
import pygame
import time
from pygame.locals import *
import random
"""
搭建主界面
"""

class HeroPlane(object):
	"""主角飞机"""
	def __init__(self,screen_tem):
		self.x = 200  #飞机初始坐标
		self.y = 600  #飞机初始坐标
		self.screen = screen_tem  #保存游戏窗口对象
		self.image = pygame.image.load("./images/hero/hero.png")  #飞机图片
		self.bullet_list = []  #保存子弹
		self.bullet_over_list =[] #保存越界的子弹
	#显示主角飞机
	def display(self):
		self.screen.blit(self.image,(self.x,self.y))  #显示主角飞机
		
		#删除越界子弹
		if len(self.bullet_over_list) > 0: 
			for over_bullet in self.bullet_over_list:  
				self.bullet_list.remove(over_bullet)

		self.bullet_over_list.clear()  #清空越界子弹列表
		
		for bullet in self.bullet_list:
			bullet.display()  #显示子弹
			#bullet.y -=10
			bullet.move()
			if bullet.judge():  #判断子弹移动后是否越界
				self.bullet_over_list.append(bullet)  #添加到越界子弹列表			

	#向左移动
	def move_left(self):
		self.x-=5
	#向右移动
	def move_right(self):
		self.x+=5
	#向上移动
	def move_up(self):
		self.y-=5
	#向下移动
	def move_down(self):
		self.y+=5

	#开火
	def fire(self):
		print("开火")
		self.bullet_list.append(Bullet(self.screen,self.x,self.y))

#敌机
class EnemyPlane(object):
	"""敌人飞机"""
	def __init__(self,screen_tem):
		self.x = 0
		self.y = 0
		self.screen = screen_tem
		self.image = pygame.image.load("./images/enemy/enemy.png")
		self.enemy_list = []
		self.bullet_list = []
		self.flag = 0  #左右移动方向标记，0向右移动，1向左移动

	#显示敌人飞机
	def display(self):
		self.screen.blit(self.image,(self.x,self.y))
		for bullet in self.bullet_list:
			bullet.display()
			#bullet.y -=10
			bullet.move()
			if bullet.judge():  #判断子弹是否越界
				self.bullet_list.remove(bullet)

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

	#向左移动
	def move_left(self):
		self.x-=5
	#向右移动
	def move_right(self):
		self.x+=5
	#向上移动
	def move_up(self):
		self.y-=5
	#向下移动
	def move_down(self):
		self.y+=5

	#开火
	def fire(self):		
		#控制子弹频率
		random_num = random.randint(1,50)
		if random_num ==1 or random_num ==10:
			print("敌机开火")
			self.bullet_list.append(EnemyBullet(self.screen,self.x,self.y))  #添加到子弹列表



#子弹
class Bullet(object):
	def __init__(self,screen_tem,x,y):
		self.x = x+28
		self.y = y-30
		self.screen = screen_tem
		self.image = pygame.image.load("./images/bullet/hero_bullet4.png")

	#子弹显示
	def display(self):
		self.screen.blit(self.image,(self.x,self.y))


	def move(self):
		self.y-=10

	def judge(self):
		if self.y <0:
			return True
		else:
			return False


#敌机子弹
class EnemyBullet(object):
	def __init__(self,screen_tem,x,y):
		self.x = x+42
		self.y = y+88
		self.screen = screen_tem
		self.image = pygame.image.load("./images/bullet/enemy_bullet.png")

	#子弹显示
	def display(self):
		self.screen.blit(self.image,(self.x,self.y))


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
