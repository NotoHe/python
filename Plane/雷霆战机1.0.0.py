#-*- coding:utf-8 -*-
import pygame
import time
"""
搭建主界面
"""
def main():
	#创建一个窗口，显示游戏内容
	screen = pygame.display.set_mode((480,854),0,32)

	#创建背景图
	background = pygame.image.load("./images/bg/主界面.jpg")

	hero = pygame.image.load("./images/hero/hero.png")

	#飞机初始坐标
	x = 200
	y = 600
	#将背景图放到窗口中显示
	while True:
		#显示背景图片
		screen.blit(background,(0,0))
		screen.blit(hero,(x,y))

		#获取操作时间
		for event in pygame.event.get():
			#检测是不是点击了关闭按钮
			if event.type == pygame.QUIT:
				print("exit")
				exit()

			#检测按键
			elif event.type == pygame.KEYDOWN:
				#检测左方向键
				if event.key == pygame.K_a or event.key == pygame.K_LEFT:
					print("left")
					if x >=0:
						x -=10
				#检测右方向键
				elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
					print("right")
					if x <=380:
						x +=10
				#检测上方向键
				elif event.key == pygame.K_w or event.key ==pygame.K_UP:
					print("up")
					y -=10
				#检测下方向键
				elif event.key == pygame.K_s or event.key ==pygame.K_DOWN:
					print("down")
					y +=10
			#检测空格
			elif event.type == pygame.K_SPACE:
				print("space")

		#更新显示内容
		pygame.display.update()

		#飞机移动
		#x+=1
		#y+=1
		time.sleep(0.02)
if __name__ == '__main__':
	main()
