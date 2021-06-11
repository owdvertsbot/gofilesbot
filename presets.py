# ----------------------------------- https://github.com/m4mallu/gofilesbot ------------------------------------------ #

class Presets(object):
    CAPTION_TEXT_DOC = "\n\n<b>File Name:</b> {}\n\n<b>Format:</b> {}\n<b>Size:</b> {}"
    CAPTION_TEXT_VID = "\n\n<b>File Name:</b> {}\n\n<b>Size:</b> {}"
    ASK_PM_TEXT = "<b>താഴെ ഉള്ള ബട്ടണിൽ ക്ലിക്ക് ചെയ്യുക</b>"
    WELCOME_TEXT = "Hello.. <b>{}</b>\n<code>I can help you getting movies from</code> @OB_MOVIESGROUP. " \
                   "<code>എന്നെ ഉണ്ടാക്കിയത് <a> href='t.me/Owdver_bot'ഇദ്ദേഹം</b> ആണ്</code>😉\n\n" \
                   "<b>Main Channel: @OB_MOVIES
    CLEAN_CHAT_MSG = "⚠️ <b>Deleting all messages..</b>"
    MSG_FOR_PIN = "<b>For getting medias from here..</b>\n\n🔛 <code>Please start</code> @{} <code>in PM\n\n" \
                  "Send the exact Movie name.\n\n🔊 I'll reply the file in PM if available in our channel !</code>"

    BOT_PM_TEXT = "<b>Sorry.. 😢</b>\n\n<code>ബോട്ട് pm ൽ വർക്ക് ചെയ്യില്ല, എൻ്റെ ഗ്രൂപ്പിൽ ചോദിക്കൂ. ഞാൻ ആ ഫയൽ Reply ആയി pm ൽ അയക്കുന്നതാണ്" \
                  "എൻ്റെ DB യിൽ ലഭ്യമാണെങ്കിൽ !</code>"
    PM_ERROR = "<b>ഫയൽ അയക്കാൻ പറ്റുന്നില്ല</b> ⛔️\n<code>താഴെ ഉള്ള ബട്ടണിൽ ക്ലിക്ക് ചെയ്യുക\nഎന്നിട്ട് ഒന്നൂടെ ആ മൂവി ഇവിടെ ചോദിക്കുക!</code>"
    MEDIA_SEND_TEXT = "<code>നിങ്ങൾ ചോദിച്ച {} എന്ന മൂവിയുടെ ഫയലുകൾ നിങ്ങളുടെ pm ൽ അയച്ചിട്ടുണ്ട്</code>"
    NO_MEDIA = "നിങ്ങൾ ചോദിച്ച: <b>{}</b>\n\n<b>മൂവി ഇപ്പോൾ " \
               "ലഭ്യമല്ല</b>\n<code>സാധ്യതയുള്ള കാരണങ്ങൾ : 🤔\n\n⭕️ റീലീസ് " \
               "ആയിട്ടില്ല</code>\n⭕️ <a href='https://www.google.com/search?q={}'>Spelling തെറ്റാണ്</a>\n" \
               "<code>⭕️Unwanted texts in Msgs\n⭕ തീയേറ്റർ പ്രിൻ്റ് ചോദിച്ചു\n⭕ എൻ്റെ ഡാറ്റാബേസിൽ ഇല്ല</code>"
    BLOCK_LIST = ['http://', 'https://', '@', '#', 'bit.ly', 't.me', '/']
