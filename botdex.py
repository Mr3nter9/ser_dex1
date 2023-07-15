import telebot
from pytube import  YouTube
import requests
from time import sleep
import re
token ='5965699318:AAHbRpWVpVZo2wZS1xcw1tsO9IfwydlHsIw'
s='5750341465'
bot = telebot.TeleBot(token)

def B3KKK(id: int) -> str:
    if str(id)[0] == '6' and str(id)[1] == '2':
        return '06/2023'
    if str(id)[0] == '6':
        return '04/2023'
    if str(id)[0] == '5' and str(id)[1] == '9':
        return '01/2023'
    if len(str(id)) == 10:
        if str(id)[0] == '5':
            if not str(id)[1] == '0':
                return '0{}/2022'.format(str(id).replace("0", "")[2])
            else:
                return '0{}/2022'.format(str(id)[2])
        elif str(id)[0] == '1' and str(id)[1] == '0':
            if '11' in str(id):
                return '11/2020'
            if '12' in str(id):
                return '12/2020'
            else:
                return '0{}/2020'.format(str(id).replace("0", "")[2])
        else:
            if '11' in str(id):
                return '11/2021'
            if '12' in str(id):
                return '12/2021'
            if '10' in str(id):
                return '10/2021'
            else:
                return '0{}/2021'.format(str(id).replace("0", "")[1])
    if len(str(id)) == 9:
        if str(id)[0] == '9':
            return '0{}/2020'.format(str(id).replace("0", "")[0])
        else:
            return B3KKK(id)[1]
    else:
        return B3KKK(id)[1]



@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,'''
مرحبا
لفحص اليوزر اذا كان مزاد ام لا ارسل user/ + اليوزر ..مثال
 (/user @T_4_6)
 ولمعرفة ايدي حسابك وتاريخ انشائه (غير دقيق)ارسل /iam''')

@bot.message_handler(commands=['iam'])
def TexTMsg(message):
    idd = message.from_user.id
    ch = 'd2_ff'
    me = 'لازم تشترك بالقناة اول شي'
    url = f'https://api.telegram.org/bot{token}/getchatmember?chat_id=@{ch}&user_id={idd}'
    req = requests.get(url)
    if idd == s or 'member' in req.text or 'creator' in req.text or 'administartor' in req.text:
        id = message.from_user.id
        date = B3KKK(id)
        bot.reply_to(message,text=f"You id is :{message.from_user.id}\nYou username is :@{message.from_user.username}\n{date}")
    else:
        bot.reply_to(message, "{} : @{}".format(me,ch))


@bot.message_handler(commands=['user'])
def TexTMsg(message):
    idd = message.from_user.id
    ch = 'd2_ff'
    me = 'لازم تشترك بالقناة اول شي'
    url = f'https://api.telegram.org/bot{token}/getchatmember?chat_id=@{ch}&user_id={idd}'
    req = requests.get(url)
    if idd == s or 'member' in req.text or 'creator' in req.text or 'administartor' in req.text:
        use = (message.text[5:])
        user = re.sub(r'@', '', use)
        p = requests.get(f"https://fragment.com/username/{user}").text
        sleep(1)
        if "On auction" in p or 'Available' in p:
            bot.reply_to(message,' مرفوع مزاد✅ ')
        else:
            bot.reply_to(message,' ما مرفوع مزاد❎ ')
    else:
        bot.reply_to(message,"{} : @{}".format(me, ch))



bot.polling()
