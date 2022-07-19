from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


btnTopUp = InlineKeyboardButton(text="TopUP", callback_data='top_up')
topUpMenu = InlineKeyboardMarkup(row_width=1)
topUpMenu.insert(btnTopUp)

def buy_menu(isUrl=True, url="", bill=""):
    qiwiMenu = InlineKeyboardMarkup(row_width=1)
    if isUrl:
        btnUrlQIWI = InlineKeyboardButton(text='Link for payment', url=url)
        qiwiMenu.insert(btnUrlQIWI)

    btnCheckQiwi = InlineKeyboardButton(text="Check Payment", callback_data="check_"+bill)
    qiwiMenu.insert(btnCheckQiwi)
    return qiwiMenu
