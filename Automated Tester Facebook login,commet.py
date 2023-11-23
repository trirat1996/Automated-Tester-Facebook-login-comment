import openpyxl 
from selenium import webdriver

from selenium.webdriver.common.by import By
import geckodriver_autoinstaller
import time 
import random2 as rd

def read_master():

    workbook = openpyxl.load_workbook("user.xlsx") 

    sheet0 = workbook.worksheets[0]
    sheet1 = workbook.worksheets[1]
    sheet2 = workbook.worksheets[2]
    sheet3 = workbook.worksheets[3] 
    global email_f
    global pass_f
    global post_fx
    global p_fset
    global post_link_f

    email_f = [] 
    pass_f = []  
    post_fx = []
    p_fset = []
    post_link_f = []
    for row0 in sheet0: 

        name = row0[0].value 
        namee = row0[1].value
        
        email_f.append(name)
        pass_f.append(namee)
        
    for row1 in sheet1:     
        seti = row1[1].value
        p_fset.append(seti)
        
    for row2 in sheet2:     
        post_link = row2[0].value
        post_link_f.append(post_link)  
        
    for row3 in sheet3:     
        postx = row3[0].value
        post_fx.append(postx) 
    
    # Print the list of names 

read_master()
e_len = len(email_f)
link_len = len(post_link_f)
post_lan = len(post_fx)
print(e_len)  
print(email_f[3]) 
print(pass_f[3])
print(post_fx) 
print(post_lan) 
print(post_link_f)
   
        
        
def facebook_login(email_f_log,pass_f_log):
    try:

        driver.get('https://mbasic.facebook.com/')
        email_input = driver.find_element(By.XPATH, '//*[@id="m_login_email"]')
        email_input.send_keys(email_f_log)
        time.sleep(1)
        password_input = driver.find_element(By.XPATH, '//*[@id="password_input_with_placeholder"]/input')
        password_input.send_keys(pass_f_log)
        time.sleep(1)
        submit = driver.find_element(By.XPATH, '//*[@id="login_form"]/ul/li[3]/input')
        submit.click()
        time.sleep(3)
        submit2 = driver.find_element(By.XPATH, '//*[@id="root"]/table/tbody/tr/td/div/div[3]/a')
        submit2.click()
        time.sleep(3)
        
        #driver.get('https://mbasic.facebook.com/')
        #time.sleep(3)
        #driver.find_element(By.NAME, 'xc_message').click()
        
        driver.get('https://mbasic.facebook.com/friends/center/mbasic')
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="friends_center_search_box"]/div/div/table/tbody/tr/td[1]/div/label/input').click() 
        print(email_f_log +"-----login pass")

    except:

        print(email_f_log +"-----login error")
    
        
def add_friend() :
    driver.get('https://mbasic.facebook.com/friends/center/mbasic')
    fan = 1
    while fan < 5:
            try:
                
                time.sleep(3)
                fan_cl = driver.find_element(By.XPATH, '//*[@id="friends_center_main"]/div[2]/div[1]/table/tbody/tr/td[2]/div[2]/table/tbody/tr/td/div[1]/a')
                fan_cl.click()
                print(fan)
                print("pass add_friend")
                time.sleep(3)
                
            except:
                driver.get('https://mbasic.facebook.com/friends/center/mbasic')
                print("error add_friend") 
            fan += 1 
           
#facebook_login(email_f[3],pass_f[3])

def f_like(linkk) :
    link_spi = linkk.split('?')
    #print( link_spi[1] )
    link_spid = str(link_spi[1])
    print(link_spid)

    try:

        driver.get('https://www.facebook.com/story.php?'+link_spid)
        time.sleep(10)
        driver.find_element(By.XPATH, '//*[@id="facebook"]').click()
        time.sleep(2)
        p_like = driver.find_element(By.XPATH, '//div[@aria-label="ถูกใจ"]')
        time.sleep(2)
        p_like.click()
        time.sleep(2)
        
        print("pass like")
    except:
        print("error like") 
        
        
def f_comment(linkk) :
    link_spi = linkk.split('?')
    #print( link_spi[1] )
    link_spid = str(link_spi[1])
    print(link_spid)        
    try: 
        random_com = int(rd.randrange(1, post_lan))
        print(random_com)
        ran_com = str(post_fx[random_com])
        print(ran_com)
        driver.get('https://mbasic.facebook.com/permalink.php?'+link_spid)
        driver.find_element(By.NAME, 'comment_text').send_keys(ran_com)
        time.sleep(2)
        sennd_p = driver.find_element(By.XPATH, '//input[@type="submit"]')
        sennd_p.click() 

        print("pass comment")
    except:
        print("error comment")


           
def f_lang() :

    try:
        driver.get('https://mbasic.facebook.com/language/?')
        time.sleep(5)
        driver.find_element(By.XPATH, '//input[@value="ภาษาไทย"]').click()
        time.sleep(2)
        print("pass language thai")
    except:
        print("error language") 


def log_out_f():
        driver.get('https://mbasic.facebook.com/menu/bookmarks')
        driver.find_element(By.ID, 'mbasic_logout_button').click()
        time.sleep(2)
        driver.find_element(By.XPATH, '//*[@id="root"]/table/tbody/tr/td/div/form[2]/input[3]').click()
        time.sleep(5) 
        print('log_out-------') 


def loop_start(add_f_s,f_lik,f_comm,f_lang_thai):
    i_loop = 19
    print(add_f_s)
    print(f_comm)
    while i_loop <= e_len :
    #while i_loop <= 19 :
            print(i_loop)
            global driver
            global geckodriver
            geckodriver = geckodriver_autoinstaller.install() 
            driver = webdriver.Chrome()  
            facebook_login(email_f[i_loop],pass_f[i_loop])
            
            if f_lang_thai == 1:
                print("f_lang === ON") 
                f_lang()
            else :  
                print("f_lang === OFF")
                
            if add_f_s == 1: 
                print("add_friend === ON")
                add_friend()  
            else :  
                print("add_friend === OFF")
                
            if f_lik == 1: 
                print("f_like === ON")
                link_loop = 1
                while link_loop <= link_len:
                    try:
                        f_like(post_link_f[link_loop])
                        link_loop += 1
                    except:
                        link_loop = int(link_len + 2 )  

            else :  
                print("f_like === OFF")

            if f_comm == 1:
                link_loop2 = 1 
                print("f_comment === ON")
                while link_loop2 <= link_len:
                    try:
                        f_comment(post_link_f[link_loop2])
                        link_loop2 += 1
                    except:
                        link_loop2 = int(link_len + 2 ) 
            else :  
                print("f_comment === OFF")
            
            try:    
                log_out_f()
                print("log_out_f----- pass")
            except:
                print("log_out_f----- error")    
            driver.quit()
            time.sleep(10)
            i_loop += 1

        
     

        
        
def loop_start_1():

        global driver
        global geckodriver
        geckodriver = geckodriver_autoinstaller.install() 
        driver = webdriver.Chrome() 
        facebook_login(email_f[26],pass_f[26])
        time.sleep(10000)
        driver.quit()
 
      
f_lang_t = 0  
add_f = 0
f_lik = 0
f_com = 1
       
loop_start(add_f,f_lik,f_com,f_lang_t)
#loop_start()
#loop_start_1()