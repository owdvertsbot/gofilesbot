# ----------------------------------- https://github.com/m4mallu/gofilesbot ------------------------------------------ #

class Presets(object):
    CAPTION_TEXT_DOC = "\n\n<b>File Name:</b> {}\n\n<b>Format:</b> {}\n<b>Size:</b> {}"
    CAPTION_TEXT_VID = "\n\n<b>File Name:</b> {}\n\n<b>Size:</b> {}"
    ASK_PM_TEXT = "<b>Click the below button</b>"
    WELCOME_TEXT = "Hello.. <b>{}</b>\n<code>I can help you getting movies from</code> @OBMOVIEZALL. " \
                   "<code>Just Keep this message live Here</code>😉\n\n" \
                   "<b>My code can be seen: </b><a href='https://t.me/nokkiirunnoippokittum'> HERE</a>"
    CLEAN_CHAT_MSG = "⚠️ <b>Deleting all messages..</b>"
    MSG_FOR_PIN = "<b>For getting medias from here..</b>\n\n🔛 <code>Please start</code> @{} <code>in PM\n\n♻️ " \
                  "Send the exact Movie name in Manglish.\n\n🔊 I'll reply the file in PM if available in our " \
                  "Database !</code>\n\n<b>ഇവിടെനിന്നും മൂവീസ് ലഭിക്കാൻ ...</b>\n\n🔛 @{} <code> എന്ന ബോട്ട് " \
                  "സ്റ്റാർട്ട് ചെയ്തതിനു ശേഷം :\n\n♻️ ഈ ഗ്രൂപ്പിൽ നിങ്ങൾക്ക് ആവശ്യമായ മൂവിയുടെ യഥാർഥ സ്പെല്ലിങ് " \
                  "മംഗ്ലീഷിൽ പോസ്റ്റ് ചെയ്യുക .\n\n🔊 ഞങ്ങളുടെ ഡാറ്റാബേസിൽ ഉണ്ടെങ്കിൽ ബോട്ട് നിങ്ങൾക്ക് " \
                  "PM ആയി നൽകുന്നതാണ് .\n\n⚠️ മൂവീസ് ഒരിക്കലും ഈ ഗ്രൂപ്പിൽ നിന്നും ലഭിക്കില്ല !</code>"

    BOT_PM_TEXT = "<b>Sorry.. 😢</b>\n\n<code>Bot won't work in PM, Ask in ma Group. I'll reply the file in PM if " \
                  "available in our DB !</code>"
    PM_ERROR = "<b>Unable to send medias</b> ⛔️\n<code>As you have Blocked or Deleted the Bot chat !\nKeep unblock " \
               "or Start the bot, then ask here for movies !</code>"
    MEDIA_SEND_TEXT = "<code>Media dispatched as PM 🥳</code>"
    NO_MEDIA = "Requested movie: <b>{}</b>\n\n<b>Not available " \
               "Right Now</b>\n<code>Possible Causes : 🤔\n\n⭕️ Not " \
               "released yet</code>\n⭕️ <a href='https://www.google.com/search?q={}'> Spelled incorrectly</a>\n" \
               "<code>⭕️ Unwanted texts in Msgs\n⭕ Asking theatre prints\n⭕ Not in ma Database</code>"
    BLOCK_LIST = ['http://', 'https://', '@', '#', 'bit.ly', 't.me', '/']
