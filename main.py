from requests import *;import os,re,random,telebot,time;from user_agent import generate_user_agent
tk="6501362455:AAE7sMyB2m3-Q9l3hojkJv4u_PFVZrPyths"
bot = telebot.TeleBot(tk)
@bot.message_handler(commands=['start'])
def s(message):
      u = message.from_user.first_name
      t=f"Hello [{u}](tg://settings),\n\n*Welcome To Magic Viewer Bot*\n\n_If You Want To Use The Bot Then Just Send Any Mesage..._"
      bot.send_message(message.chat.id, text=t, parse_mode='markdown')
@bot.message_handler(func=lambda m: True)
def v(message):
    u = message.from_user.first_name
    w = bot.send_message(message.chat.id, text=f"Hey [{u}](tg://settings),\n_Wait We Are Sending A Magic Video In Few Seconds..._", parse_mode='markdown')    
    num_digits = random.randint(2, 6)
    num = ''.join(random.choice('0123456789') for _ in range(num_digits))
    s = get("https://tik.porn/video/" + num).text
    print(num)    
    m = re.search(r'"downloadLink":"(https://[^"]+)"', s)
    time.sleep(3)    
    if m:
        u= m.group(1)
        time.sleep(2)
        bot.delete_message(message.chat.id, w.message_id)
        bot.send_video(message.chat.id, u, caption="Dev: [SANCHIT](tg://settings)",parse_mode='markdown')
bot.polling(non_stop=True)
