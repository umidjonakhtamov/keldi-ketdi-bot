import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)
from datetime import datetime

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton("Keldim", callback_data="came"),
            InlineKeyboardButton("Ketdim", callback_data="left"),
            InlineKeyboardButton("Bugungi holat", callback_data="status"),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Davomatni belgilang:", reply_markup=reply_markup)

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user = query.from_user.first_name
    time_now = datetime.now().strftime("%H:%M")
    if query.data == "came":
        await query.edit_message_text(f"{user}, siz soat {time_now} da keldingiz. Ishingizga omad!")
    elif query.data == "left":
        await query.edit_message_text(f"{user}, siz soat {time_now} da ketdingiz. Yaxshi dam oling!")
    elif query.data == "status":
        await query.edit_message_text("Bugungi holat: [statistika bu yerda bo‘ladi]")

if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))
    app.run_polling()
