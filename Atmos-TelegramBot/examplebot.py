# coding: utf8
#Other imports
import time, parseData

#Logging Config
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)
logger = logging.getLogger(__name__)

#Telegram Bot Code
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

from Utils import sprint

#Commands

kbds={
	# TODO: Update for translation support

	"Principal": [[InlineKeyboardButton("Temperatura",
	callback_data='Temperatura'),
	InlineKeyboardButton("Humedad",
	callback_data='Humedad')],
	[InlineKeyboardButton("Luz",
	callback_data='Luz'),
        InlineKeyboardButton("Presion",
	callback_data='Presion')]],

        "Temperatura": [[InlineKeyboardButton("Temp. Max.",
	callback_data='TMax'),
	InlineKeyboardButton("Temp. Min",
	callback_data='TMin')],
	[InlineKeyboardButton("Temp. Media",
	callback_data='TMedia'),
	InlineKeyboardButton("Temp. Actual",
	callback_data='TActual')],
	[InlineKeyboardButton("Volver A Inicio", callback_data='@back')]],

	"Humedad": [[InlineKeyboardButton("Humedad Actual",
	callback_data='HActual')],
	[InlineKeyboardButton("Volver A Inicio", callback_data='@back')]],

	"Luz": [[InlineKeyboardButton("Luminosidad Max.",
	callback_data='LMax'),
	InlineKeyboardButton("Luminosidad Min.",
	callback_data='LMin'),
        InlineKeyboardButton("Luminosidad Actual",
	callback_data='LActual')],
	[InlineKeyboardButton("Volver A Inicio", callback_data='@back')]],

        "Presion": [[InlineKeyboardButton("Presion Max.",
	callback_data='PMax'),
	InlineKeyboardButton("Presion Min.",
	callback_data='PMin'),
        InlineKeyboardButton("Presion Actual",
	callback_data='PActual'),
        InlineKeyboardButton("Presion Media",
	callback_data='PMedia')],
	[InlineKeyboardButton("Volver A Inicio", callback_data='@back')]],
}

def opt(bot, update):
	# TODO: Update for translation support
    reply_markup = InlineKeyboardMarkup(kbds["Principal"])
    update.message.reply_text('Menu principal', reply_markup=reply_markup)

def updatemenu(bot, update, query, msgId, kbdId):
    try:
        reply_markup = InlineKeyboardMarkup(kbds[kbdId])

		# TODO: Update for translation support
        bot.edit_message_text(text="Menu %s" % kbdId,
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
            bot.send_message(chat_id=query.message.chat_id, text="Temperatura Actual: "+parseData.readTHWL(data)[0])
            return
        elif (kbdId=='HActual'):
            bot.send_message(chat_id=query.message.chat_id, text="Humedad Actual: "+parseData.readTHWL(data)[1])
            return
        elif (kbdId=='LActual'):
            bot.send_message(chat_id=query.message.chat_id, text="Luminosidad Actual: "+parseData.readTHWL(data)[3])
            return
        elif (kbdId=="PActual"):
            bot.send_message(chat_id=query.message.chat_id, text="Presion Actual: "+parseData.readTHWL(data)[4])
            return
        else:
            invalidMsg = bot.send_message(chat_id=query.message.chat_id,
                             text="Id Invalida")
            time.sleep(3)
            bot.delete_message(chat_id=invalidMsg.chat_id,
                                message_id=invalidMsg.message_id)
    query.answer()
    #bot.answer_callback_query(callback_query_id=msgId)

def button(bot, update):
    query = update.callback_query

    updatemenu(bot, update, query, query.message.message_id, query.data)

def main():
	updater = Updater(token='500779322:AAHmBMF_nV48qNet4IMfgNmcOW5tuQ7ojdI')
	dispatcher = updater.dispatcher

	#Handlers
	start_handler = CommandHandler('start',opt)
	opt_handler = CommandHandler('options',opt)
	btn_handler = CallbackQueryHandler(button)

	#Register handlers
	dispatcher.add_handler(start_handler)
	dispatcher.add_handler(opt_handler)
	dispatcher.add_handler(btn_handler)

	#Start & run until Ctrl+C
	updater.start_polling()
	updater.idle()

if __name__ == '__main__':
	main()
