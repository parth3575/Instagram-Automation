from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from random import randint

chromedriver_path = 'E:/setups/for_instagram_automation/chromedriver.exe' # Change this to your own chromedriver path!
webdriver = webdriver.Chrome(executable_path=chromedriver_path)
sleep(2)
webdriver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
sleep(3)

username = webdriver.find_element_by_name('username')
username.send_keys(' ') #enter your instagram username here
password = webdriver.find_element_by_name('password')
password.send_keys(' ') #enter your instagram password here
sleep(3)

button_login = webdriver.find_element_by_xpath("//button[@type='submit']")
button_login.click()
sleep(5)

hashtag_list = ['photography, travelling, pics'] #add hashtags separated by coma (,)
tag = -1
likes = 0
comments = 0
follows = 0
for hashtag in hashtag_list:
    tag += 1
    webdriver.get('https://www.instagram.com/explore/tags/'+ hashtag_list[tag] + '/')
    sleep(5)
    first_thumbnail = webdriver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div')
    
    first_thumbnail.click()
    sleep(randint(1,2))    
    try:        
        for x in range(1,210):#likes 200 pictures in a row
            if True:
                # Liking the picture
                button_like = webdriver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[3]/section[1]/span[1]/button')
                button_like.click()
                likes += 1
                sleep(randint(13,20))
                
                
                #adding a comment 
                random_no = randint(1,10)
                print('{}_{}: {}'.format(hashtag, x,random_no))
                sleep(2)
                if random_no:

                    if (random_no <= 5):
                        comment_box = webdriver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/textarea') 
                        comment_box.click()
                        sleep(3)
                        webdriver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/textarea').send_keys('Really cool!', Keys.ENTER)
                        sleep(1)
                    elif (random_no >= 6) and (comm_prob <= 8):
                        comment_box = webdriver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/textarea') 
                        comment_box.click()
                        webdriver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/textarea').send_keys('Nice work :)', Keys.Enter)
                        sleep(1)
                    elif random_no == 9:
                        comment_box = webdriver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/textarea') 
                        comment_box.click()
                        webdriver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/textarea').send_keys('Nice gallery!!', Keys.Enter)
                        sleep(1)
                    elif random_no == 10:
                        comment_box = webdriver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/textarea') 
                        comment_box.click()
                        webdriver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/textarea').send_keys('So cool! :)', Keys.Enter)
                        sleep(1)
                    
                    comments += 1
                    sleep(randint(12,18))
                else:
                    continue
                
				#Follow 
                if webdriver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[2]/button').text == 'Follow':
                    webdriver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[2]/button').click()
                    follows += 1
                    sleep(3)
                
               
               # Next picture
                webdriver.find_element_by_link_text('Next').click()
                sleep(randint(15,22))
            else:
                webdriver.find_element_by_link_text('Next').click()
                sleep(randint(10,17))
                # some hashtag stops refreshing photos (it may happen sometimes), it continues to the next
    except:
        continue
    
    finally:
        print('Liked {} photos.'.format(likes))
        print('Commented {} photos.'.format(comments))
        print('Followed {} photos.'.format(follows))



