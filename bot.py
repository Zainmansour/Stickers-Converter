##############################################
######This bot was done by Zain Mansour#######
##############################################
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
import telegram.bot as bot
import telegram.botcommand as botcom
from telegram.ext.conversationhandler import ConversationHandler
from PIL import Image
import os
import re
import random
#from dotenv import load_dotenv
#load_dotenv()
token = "5474218345:AAESAHF9n9AF2Mpph8bnlAaVulYECUy0Qug"
print (token)
updater = Updater(token, use_context=True)
bo = bot.Bot(token)
PORT = 88

def start(update: Update, context: CallbackContext):
    update.message.reply_text("""
     Hi,
     use /use to start using the bot
     use /help for help
     """)


def unknown(update: Update, context: CallbackContext):
    update.message.reply_text('this isn\'t a photo')


def use(update: Update, context: CallbackContext):
    update.message.reply_text("Send me an image to resize it")


def help(update: Update, context: CallbackContext):
    msg = """
    This bot resize images to make them stickers
send /use to start sending images
    """
    update.message.reply_text(msg)


def photos(update: Update, context: CallbackContext):
    file_name = str(re.search(
        '\w+', update.message.chat.first_name).group())+"___"+str(update.message.chat.id)
    file = context.bot.getFile(update.message.photo[-1].file_id)
    abspath = os.getcwd()+f"\\users\\{file_name}.png"
    file.download(abspath)
    img = Image.open(abspath)
    img.show()
    #################
    basewidth = 512
    wpercent = (basewidth/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    if wpercent > 512 or hsize > 512:
        wpercent = 512
        hsize = 512
    out = img.resize((basewidth, hsize), Image.Resampling.LANCZOS)
    #################
    new = os.getcwd()+f"\\users\\{file_name}edited.png"
    out.save(new)
    os.remove(abspath)
    update.message.reply_document(open(new, 'rb'))
    update.message.reply_sticker(open(new, 'rb'))
    os.remove(new)
    update.message.reply_text('done')


command = [botcom.BotCommand('use', 'Start using this bot'), botcom.BotCommand(
    'help', 'More information about this bot')]
bo.set_my_commands(command)
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('use', use))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(Filters.photo, photos))
updater.start_webhook(listen="0.0.0.0", port=int(PORT), url_path=TOKEN)
updater.bot.setWebhook('https://api.render.com/deploy/srv-ced4ghsgqg4fe5a97vu0?key=AryKbVMp3YY/' + TOKEN)

updater.idle()
