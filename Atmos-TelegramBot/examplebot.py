# coding: utf8
#Other imports
import time, parseData
from functools import partial

#Logging Config
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)
logger = logging.getLogger(__name__)

#Telegram Bot Code
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

import MySQL
# Use this instead of print so that the output can be seen in a server environment
from Utils import sprint

#Commands

lang="EN"
db_connection = MySQL.getConnection('root', 'root', 'Atmos')
txtIds=[]

kbds={

	"Principal": [[InlineKeyboardButton(MySQL.getTranslation(db_connection, 'tmp', lang),
	callback_data='Temperatura'),
	InlineKeyboardButton(MySQL.getTranslation(db_connection, 'hum', lang),
	callback_data='Humedad')],
	[InlineKeyboardButton(MySQL.getTranslation(db_connection, 'lig', lang),
	callback_data='Luz'),
        InlineKeyboardButton(MySQL.getTranslation(db_connection, 'prs', lang),
	callback_data='Presion')]],

    "Temperatura": [[InlineKeyboardButton(MySQL.getTranslation(db_connection, 'max_tmp', lang),
	callback_data='TMax'),
	InlineKeyboardButton(MySQL.getTranslation(db_connection, 'min_tmp', lang),
	callback_data='TMin')],
	[InlineKeyboardButton(MySQL.getTranslation(db_connection, 'avg_tmp', lang),
	callback_data='TMedia'),
	InlineKeyboardButton(MySQL.getTranslation(db_connection, 'cur_tmp', lang),
	callback_data='TActual')],
	[InlineKeyboardButton(MySQL.getTranslation(db_connection, 'back', lang), callback_data='@back')]],

	"Humedad": [[InlineKeyboardButton(MySQL.getTranslation(db_connection, 'max_hum', lang),
	callback_data='HMax'),
	InlineKeyboardButton(MySQL.getTranslation(db_connection, 'min_hum', lang),
	callback_data='HMin')]
	[InlineKeyboardButton(MySQL.getTranslation(db_connection, 'avg_hum', lang),
	callback_data='HMedia'),
	InlineKeyboardButton(MySQL.getTranslation(db_connection, 'cur_hum', lang),
	callback_data='HActual')]
	[InlineKeyboardButton(MySQL.getTranslation(db_connection, 'back', lang), callback_data='@back')]],

	"Luz": [[InlineKeyboardButton(MySQL.getTranslation(db_connection, 'max_lig', lang),
	callback_data='LMax'),
	InlineKeyboardButton(MySQL.getTranslation(db_connection, 'min_lig', lang),
	callback_data='LMin')],
    [InlineKeyboardButton(MySQL.getTranslation(db_connection, 'avg_lig', lang),
	callback_data='LMedia'),
	InlineKeyboardButton(MySQL.getTranslation(db_connection, 'cur_lig', lang),
	callback_data='LActual')],
	[InlineKeyboardButton(MySQL.getTranslation(db_connection, 'back', lang), callback_data='@back')]],

    "Presion": [[InlineKeyboardButton(MySQL.getTranslation(db_connection, 'max_prs', lang),
	callback_data='PMax'),
	InlineKeyboardButton(MySQL.getTranslation(db_connection, 'min_prs', lang),
	callback_data='PMin')],
    [InlineKeyboardButton(MySQL.getTranslation(db_connection, 'avg_prs', lang),
	callback_data='PMedia'),
	InlineKeyboardButton(MySQL.getTranslation(db_connection, 'cur_prs', lang),
	callback_data='PActual')],
	[InlineKeyboardButton(MySQL.getTranslation(db_connection, 'back', lang), callback_data='@back')]],
}

def opt(bot, update):
    reply_markup = InlineKeyboardMarkup(kbds["Principal"])
    update.message.reply_text(MySQL.getTranslation(db_connection, 'main_menu', lang), reply_markup=reply_markup)

def updatemenu(bot, update, query, msgId, kbdId):
    try:
        reply_markup = InlineKeyboardMarkup(kbds[kbdId])

        localized_manu_name = "ERROR"
        if kbdId == 'Principal':
            localized_manu_name = MySQL.getTranslation(db_connection, 'main_menu', lang)
        elif kbdId == 'Temperatura':
	        localized_manu_name = MySQL.getTranslation(db_connection, 'tmp_menu', lang)
        elif kbdId == 'Humedad':
	        localized_manu_name = MySQL.getTranslation(db_connection, 'hum_menu', lang)
        elif kbdId == 'Presion':
	        localized_manu_name = MySQL.getTranslation(db_connection, 'prs_menu', lang)
        bot.edit_message_text(text=localized_manu_name,
                                  chat_id=query.message.chat_id,
                                  message_id=query.message.message_id,
                                  reply_markup=reply_markup)
    except KeyError:
		# TODO: Update for translation support
        data = parseData.readArduino([])
        if(kbdId=='@back'):
            updatemenu(bot, update, query, msgId, "Principal")
            return data
        elif (kbdId=='TActual'):
            bot.send_message(chat_id=query.message.chat_id, text=MySQL.getTranslation(db_connection, 'cur_tmp', lang)+": "+parseData.readTHWL(data)[0])
            return
        elif (kbdId=='HActual'):
            bot.send_message(chat_id=query.message.chat_id, text=MySQL.getTranslation(db_connection, 'cur_hum', lang)+parseData.readTHWL(data)[1])
            return
        elif (kbdId=='LActual'):
            bot.send_message(chat_id=query.message.chat_id, text=MySQL.getTranslation(db_connection, 'cur_lig', lang)+parseData.readTHWL(data)[2])
            return
        elif (kbdId=="PActual"):
            bot.send_message(chat_id=query.message.chat_id, text=MySQL.getTranslation(db_connection, 'cur_prs', lang)+parseData.readTHWL(data)[3])
            return
        else:
            invalidMsg = bot.send_message(chat_id=query.message.chat_id, text=MySQL.getTranslation(db_connection, 'invalid_id', lang))
            time.sleep(3) # porque esta esto aqui?  ~Juan
            bot.delete_message(chat_id=invalidMsg.chat_id, message_id=invalidMsg.message_id)
    query.answer()

def button(bot, update):
    query = update.callback_query

    updatemenu(bot, update, query, query.message.message_id, query.data)

def changeLang(toLang):
    global lang
    lang = toLang

def main():
	updater = Updater(token='500779322:AAHmBMF_nV48qNet4IMfgNmcOW5tuQ7ojdI')
	dispatcher = updater.dispatcher

	#Handlers
	start_handler = CommandHandler('start',opt)
	opt_handler = CommandHandler('options',opt)
	es_handler = CommandHandler('spanish',partial(changeLang,"ES")) #Partial is for putting parameters to the call ~ Víctor
	en_handler = CommandHandler('english',partial(changeLang,"EN"))
	btn_handler = CallbackQueryHandler(button)

	#Register handlers
	dispatcher.add_handler(start_handler)
	dispatcher.add_handler(opt_handler)
	dispatcher.add_handler(es_handler)
	dispatcher.add_handler(en_handler)
	dispatcher.add_handler(btn_handler)

	#Start & run until Ctrl+C
	updater.start_polling()
	updater.idle()

if __name__ == '__main__':
	main()
