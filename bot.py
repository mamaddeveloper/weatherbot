# -*- coding: utf-8 -*-
import config
import telebot
import time
from time import gmtime, strftime
import random

import subprocess
from lxml import etree
# Конфигурационный параметр.
# Идентификатор города в Яндекс.Погода
# Москва.
city_id = 27612
ns = {'ya': 'http://weather.yandex.ru/forecast'}
tree = etree.parse(r'http://export.yandex.ru/weather-ng/forecasts/{}.xml'.format(city_id))
temp = tree.xpath('ya:fact/ya:temperature', namespaces = ns)[0].text

dic_hi = {
0: 'Добрый день',
1:'Здравствуйте',
2:'Добрый вечер',
3:'Доброе утро'
}

dic_gagarin = {
'about': 'Компания GAGARIN MEDIA активно развивается на российском рынке с октября 2012 года. Основным направлением деятельности нашей компании является видеомаркетинг и развитие рынка Digital Signage технологий в России, создание indoor TV телеканалов, производство и размещение в их эфире видеопродукции премиального качества, продажа рекламы в сетях indoor TV.',
'contacts':'Адрес офиса: Киевское шоссе, дом 1, бизнес парк Румянцево, корпус Г, офис 407 Тел.: +7 (985) 600 5 111',             
'opportunities':'На данный момент для наших партнёров доступно множество маркетинговых инструментов, с которыми можно ознакомиться подробнее по ссылке: http://gagarinmedia.ru/predlozhenie-dlya-deystvuyushchih-klientov'
}

def listener(messages):
    for m in messages:
        if m.content_type == 'text':
            if (m.text==u'привет'):
            	i = random.randint(0, 3)
            	bot.send_message(m.chat.id, dic_hi[i])
            if (m.text==u'/about'):
            	bot.send_message(m.chat.id, dic_gagarin['about'])
            if (m.text==u'/contacts'):
            	bot.send_message(m.chat.id, dic_gagarin['contacts'])
            if (m.text==u'/opportunities'):
            	bot.send_message(m.chat.id, dic_gagarin['opportunities'])
            if (m.text==u'/date'):
            	bot.send_message(m.chat.id, strftime("%d-%m-%Y", gmtime()))
            if (m.text==u'/weather'):
            	bot.send_message(m.chat.id, temp)


if __name__ == '__main__':
     bot = telebot.TeleBot(config.token)
     bot.set_update_listener(listener)
     bot.polling(none_stop=True)
