'''Gets temp email address
then forwards any emails'''

_website = r'https://generator.email/inbox8/'

import wb as _wb
from tkinter import Tk as _Tk #using to get clipboard data
import lib.metalib as _meta

_w = None

def temp_email_get():
    '''Get initial new temp email addy'''
    global _w
    if not _w: #store website info if empty
        _w = _wb.site(_website, headless=False)
    _w.click_elem('id','copbtn')
    root = _Tk()
    root.withdraw()
    addr = root.clipboard_get()
    return addr

def temp_email_refresh():
    '''Refresh temp email'''
    _w.click_elem('id','refresh')

def temp_email_new():
    '''Discard previous temp email and get new'''
    _w.click_elem('link text', 'Generate new e-mail')
    temp_email_get()

def temp_email_check_mail(repeat=0):
    '''Check temp email
    can specify to keep checking'''
    pass

def temp_email_close():
    '''Close temp email session'''
    _w.close()
    print("Temp email session Finished")

exec(_meta.print_funcs('_meta'))
