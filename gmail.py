import names
import lib.rndm as rndm
import wb
import logging
from lib.ip_addr import get_ip
from time import perf_counter as counter

log_file=r'Y:\python\logs\gmail.txt'
logging.basicConfig(filename=log_file, level=logging.INFO,
                    format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

addr = r'https://www.google.com'

name=names.get_first_name().lower()
surname=names.get_last_name().lower()
username=name+rndm.str_generator(5,10,include_punc=False,include_upper=False, min_digit=True)
pw = rndm.str_generator(8,16,include_punc=False,min_upper=True, min_punc=True, min_digit=True)
#ip = get_ip()

logging.info(f'ip is {get_ip()}')
logging.info(f'{name}, {surname}, {username}, {pw}')
status = ''

start = counter()
try:
    w = wb.site(addr) #go to site

    try:
        w.click_elem('xpath',"//*[text()='I agree']")
    except:
        pass
    
    w.click_elem('link text','Gmail') #gmail link

    w.click_elem('xpath',"//span[text()='Create an account']") #create acnt btn

    w.send_text_('id','firstName',name)
    #w.wait(rndm.rand_no('int',5,10))
    w.send_text('id','lastName',surname)
    #w.wait(rndm.rand_no('int',5,10))
    w.send_text('id','username',username)
    #w.wait(rndm.rand_no(_type='int',lower_bound=7,upper_bound=12))
    w.send_text('name','Passwd',pw)
    #w.wait(rndm.rand_no(_type='int',lower_bound=8,upper_bound=15))
    w.send_text('name','ConfirmPasswd',pw)
    #w.wait(rndm.rand_no(_type='int',lower_bound=6,upper_bound=10))

    try:
        w.click_elem('xpath',"//input[@type='checkbox']") #show pwd button
    finally:
        #w.wait(rndm.rand_no(_type='int',lower_bound=3,upper_bound=7))
        w.click_elem('xpath',"//*[text()='Next']") #next button

    try:
        if w.get_elem('xpath',"//*[text()='Verifying your phone number' or @id='phoneNumberId']"):
            status='Failed, requires phone number!'
            logging.warning(status)
            print(status)
    except Exception as e:
        print(e)

except Exception as e:
    logging.error(f'Exception in program. {e}')
    

finally:
    end= counter()
    time_taken = end-start
    logging.info(f'Total time taken: {time_taken} \n')
    print('End of iteration')
    w.quit()
    
