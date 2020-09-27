from selenium import webdriver
from win10toast import ToastNotifier
from selenium.webdriver.common.keys import  Keys
import  time
import random

def login(username,passw,people):
	bot = webdriver.Chrome(executable_path=r"C:\Users\main\Downloads\chromedriver_win32\chromedriver")	
	bot.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
	time.sleep(random.randint(2,4))
	bot.find_element_by_name('username').send_keys(f'{username}')
	print('entered username')
	bot.find_element_by_name('password').send_keys(f'{passw}')
	print('Enter passsword')
	time.sleep(random.randint(5,6))
	bot.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div/div[3]/button').send_keys(Keys.ENTER)
												# /html/body/div[1]/section/main/div/article/div/div[1]/div/form/div/div[3]/button
	time.sleep(random.randint(8,10))

# def follow(person):
	for person in people:
		bot.get(f'https://www.instagram.com/{person}/')
		time.sleep(random.randint(2,3))
		posts = bot.find_elements_by_class_name('_9AhH0')
		post2 = posts[0].click()
		time.sleep(random.randint(10,12))
		try:
			bot.find_element_by_xpath('/html/body/div[3]/div[2]/div/article/div[3]/section[2]/div/div[2]/button').click()  ###liked list
		except:
			bot.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[3]/section[2]/div/div/button').click()  ###liked list
								   # /html/body/div[4]/div[2]/div/article/div[3]/section[2]/div/div/button
								   ## /html/body/div[4]/div[2]/div/article/div[3]/section[2]/div/div/button
								   # /html/body/div[3]/div[2]/div/article/div[3]/section[2]/div/div[2]/button
								   # /html/body/div[4]/div[2]/div/article/div[3]/section[2]/div/div[2]/button
		                           #/html/body/div[4]/div[2]/div/article/div[3]/section[2]/div/div/button
		                           #/html/body/div[4]/div[2]/div/article/div/div[3]/section[2]/div/div/button
		finally:
			time.sleep(8)
			scroll_box=bot.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/div')
			# /html/body/div[4]/div/div/div[2]/div
			follow=[]
			z=350
			time.sleep(5)
			for x in range(1,12):
				q=bot.find_element_by_xpath(f'/html/body/div[5]/div/div/div[2]/div/div/div[{x}]/div[2]/div[1]/div/span/a').text
											  #/html/body/div[5]/div/div/div[2]/div/div/div[{x}]/div[2]/div[1]/div/span/a
											  #/html/body/div[5]/div/div/div[2]/div/div/div[2]/div[2]/div[1]/div/span/a
				follow.append(q)
			for y in range(2,130):
				# print('in loop')
				z=z+60
				ht = bot.execute_script(f"""arguments[0].scrollTo(0,{z});return arguments[0].scrollHeight;""",
		                                        scroll_box)
				name=bot.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/div/div/div[11]/div[2]/div[1]/div/span/a').text
				follow.append(name)
			follow=list(dict.fromkeys(follow))
			print(follow)
			print(f'to follow {len(follow)}')
			for tofollow in follow :
				time.sleep(random.randint(10,18))
				bot.get(f'https://www.instagram.com/{tofollow}/')
				time.sleep(random.randint(2,5))
				print(tofollow)
				try:
					bot.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/div/div/span/span[1]/button').click()
											  #/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/span/span[1]/button
				except:
					try:
						bot.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/div/button').click()
												  #/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/button
					except:
						continue


# username='rehankhan12.21'
# passw='bhakti@123'
# person='humor.buzz'
# login(username='rehankhan12.21',passw='bhakti@123')
# follow(person='humor.buzz')


##############  commands to upload on git ############################
# git init 
# git status
# git add .
# git status
# git commit -m "first commit" .
# git remote add origin https://github.com/greatret/steve.git (from repository )
# git push -u origin master (from repository)
