import validators
import requests
import telebot

bot = telebot.TeleBot("Token")

@bot.message_handler(commands=["start","ابدا","ابدأ", "Start"])
def rs(mes):
     bot.send_message(mes.from_user.id,f" مرحبا {mes.from_user.first_name} نورت البوت 😊\n  الرجاء ادخال اسم المستخدم او الرابط الخاص بالحساب")
     bot.send_message(mes.from_user.id,f"للتواصل مع صاحب البوت\n https://mobile.twitter.com/_ii404")


def userURL(mes): #Pass URL
   if("?" in mes): # if URL contain (?) that mean the URL are copied from mobile phone
    list=mes.split("/"and"?")
    print(list)
    list=list[0]
    username= list.split("/")

    return username[-1]
   else:
       print("Second")
       list=mes.split("/")

       if(list[-1]==""):
        return list[-2]
       else:
        return list[-1]


def findUserName(mes,id,name):

    try:
        req = requests.session()
        head = { 'cookie':'',}
        req = req.get(f"API",headers=head)
        m=req.json()
        flag = 0
        for i in range(len(m['users'])):
            if(m['users'][i]['user']['username'].lower()== mes.lower()):
                flag+=1
                if(m['users'][i]['user']['full_name']!=""):
                 bot.send_message(id,m['users'][i]['user']['full_name'])
                bot.send_photo(id,m['users'][i]['user']['profile_pic_url'])

                break

        if(flag==0):
            raise Exception
    except:
       bot.send_message(id,"الرجاء التحقق من اسم المستخدم")

@bot.message_handler(content_types="text")
def rs(mes):
        id=mes.from_user.id
        if(validators.url(mes.text)):
            username=userURL(mes.text)


            findUserName(username,id,mes.from_user.first_name)
        else:
            findUserName(mes.text,id,mes.from_user.first_name)
bot.infinity_polling()
