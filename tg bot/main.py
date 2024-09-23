from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, InputFile
from telegram.ext import ApplicationBuilder, CommandHandler
import requests

# /start komandasi bosilganda bajariladigan funksiya
async def start(update: Update, context):
    user = update.effective_user
    # Foydalanuvchining niki bilan salomlashish
    greeting = f"Salom, @{user.username}!"

    # Rasm yuklash
    photo_url = 'https://images.unsplash.com/photo-1516117172878-fd2c41f4a759?ixlib=rb-1.2.1&q=85&fm=jpg&crop=entropy&cs=srgb'  # Rasm URL manzili
    photo = requests.get(photo_url).content  # Rasmdan kontentni yuklash
    file = InputFile(photo, filename='image.jpg')  # Rasmni InputFile formatida olish

    # 3 ta inline tugma yaratish
    keyboard = [
        [InlineKeyboardButton("1-tugma", url='https://t.me/not_pixelworld')],
        [InlineKeyboardButton("2-tugma", url='https://example.com/link2')],
        [InlineKeyboardButton("3-tugma", url='https://example.com/link3')]
    ]

    # InlineKeyboardMarkup tugmalarni birlashtirish uchun ishlatiladi
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Foydalanuvchiga rasm, salomlashish va tugmalarni jo'natish
    await update.message.reply_photo(photo=file, caption=greeting, reply_markup=reply_markup)

# Asosiy qism - botni yaratish va handler o‘rnatish
if __name__ == '__main__':
    application = ApplicationBuilder().token('7106204360:AAEOL78xpqumT0zV2_1QetIFQc_9Rv35nX8').build()

    # /start komandasini ishlovchi handler
    application.add_handler(CommandHandler("start", start))

    # Botni ishga tushirish
    application.run_polling()
