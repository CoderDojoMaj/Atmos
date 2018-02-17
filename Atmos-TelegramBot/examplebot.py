#Other imports
import time

#Logging Config
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)
logger = logging.getLogger(__name__)

#Telegram Bot Code
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler

#Commands
kbds={
	"Principal": [[InlineKeyboardButton("Temperatura",
	callback_data='Temperatura'),
	InlineKeyboardButton("Humedad",
	callback_data='Humedad')],
	[InlineKeyboardButton("Luz",
	callback_data='Luz')]],
	
	"Temperatura": [[InlineKeyboardButton("Temp. Máx.",
	callback_data='TMax'),
	InlineKeyboardButton("Temp. Min",
	callback_data='TMin')],
	[InlineKeyboardButton("Temp. Media",
	callback_data='TMedia'),
	InlineKeyboardButton("Temp. Actual",
	callback_data='TActual')],
	[InlineKeyboardButton("Volver A Inicio", callback_data='@back')]],
	
	"Humedad": [[InlineKeyboardButton("Humedad Actual",
	callback_data='HActual'),
	InlineKeyboardButton("¿Llueve?",
	callback_data='HLluvia')],
	[InlineKeyboardButton("Volver A Inicio", callback_data='@back')]],
	
	"Luz": [[InlineKeyboardButton("Luminosidad Máx.",
	callback_data='LMax'),
	InlineKeyboardButton("Luminosidad Min.",
	callback_data='LMin')],
	[InlineKeyboardButton("Volver A Inicio", callback_data='@back')]]
}

def opt(bot, update):
    reply_markup = InlineKeyboardMarkup(kbds["Principal"])

    update.message.reply_text('Menú principal', reply_markup=reply_markup)

def updatemenu(bot, update, query, msgId, kbdId):    
    try:
        reply_markup = InlineKeyboardMarkup(kbds[kbdId])
        
        bot.edit_message_text(text="Menú %s" % kbdId,
                                  chat_id=query.message.chat_id,
                                  message_id=query.message.message_id,
                                  reply_markup=reply_markup)
    except KeyError:
        if(kbdId=='@back'):
            updatemenu(bot, update, query, msgId, "Principal")
            return
        invalidMsg = bot.send_message(chat_id=query.message.chat_id,
                         text="Id Inválida")
        time.sleep(3)
        bot.delete_message(chat_id=invalidMsg.chat_id,
                            message_id=invalidMsg.message_id)

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
