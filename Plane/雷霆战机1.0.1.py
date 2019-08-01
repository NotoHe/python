#-*- coding:utf-8 -*-
import pygame
import time
from pygame.locals import *
"""
搭建主界面
"""

#飞机
class HeroPlane(object):
	"""docstring for HeroPlane"""
	def __init__(self,screen_tem):
		self.x = 200
		self.y = 600
		self.screen = screen_tem
		self.image = pygame.image.load("./images/hero/hero.png")
		self.bullet_list = []
	#显示主角飞机
	def display(self):
		self.screen.blit(self.image,(self.x,self.y))
		for bullet in self.bullet_list:
			bullet.display()
			#bullet.y -=10
			bullet.move()

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
	hero =HeroPlane(screen)

	while True:
		#将背景图放到窗口中显示
		screen.blit(background,(0,0))
		#显示主角飞机
		hero.display()
		#键盘操作事件处理-移动开火
		key_control(hero)
		#更新显示内容
		pygame.display.update()
		#优化一下性能，减少cpu负担
		time.sleep(0.02)

if __name__ == '__main__':
	main()
