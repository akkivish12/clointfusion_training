import ClointFusion as cf
cf.browser_navigate_h("https://www.gmail.com")
#user_name = cf.browser_locate_element_h("//*[@id='identifierId']")

#put your email id here
email = "example@gmail.com"
cf.browser_write_h(email,"Email or Phone") 
cf.browser_mouse_click_h("Next")

#password in txt file for encryption
#create txt file.
#add your password in it
f = open("password.txt", "r")
password = f.read()
cf.browser_write_h(password,"Enter your password")
cf.browser_mouse_click_h("Next")

cf.browser_wait_until_h("loading gmail")

#process for email writing starts here
cf.browser_mouse_click_h("Compose")
cf.browser_write_h("akkivish12@gmail.com","To")
cf.browser_write_h("test" ,"Subject")
cf.key_press('tab')
message = "hi this is test" 
cf.key_write_enter(message)
cf.browser_mouse_click_h("Send")
cf.browser_wait_until_h("Message sent.")

cf.browser_quit_h()
