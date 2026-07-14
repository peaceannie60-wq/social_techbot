import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Get token from environment variable
TOKEN = os.environ.get('BOT_TOKEN')
if not TOKEN:
    raise ValueError("BOT_TOKEN environment variable not set!")

# Channel configuration (hidden for now)
CHANNEL_LINK = "https://t.me/blaqmarqetnotify"
CHANNEL_USERNAME = "@blaqmarqetnotify"

# NEUTRAL welcome message - NO promotional language
WELCOME_MESSAGE = """Welcome to BLAQSTRATEGY.

This bot provides information about digital advertising education.

Current features:
- Educational content about advertising systems
- Campaign organization insights
- Workflow optimization information

Type /help to see available commands."""

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send neutral welcome message."""
    user = update.effective_user
    logger.info(f"User {user.first_name} (ID: {user.id}) started the bot")
    
    # Simple, non-promotional keyboard
    keyboard = [
        [InlineKeyboardButton("About This Bot", callback_data="about")],
        [InlineKeyboardButton("Help", callback_data="help")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        WELCOME_MESSAGE,
        reply_markup=reply_markup,
        parse_mode='Markdown'
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send help message."""
    help_text = """Available commands:

/start - Show welcome message
/help - Show this help
/about - Information about this bot
/education - Educational resources

This bot provides information about digital advertising education."""
    
    await update.message.reply_text(help_text, parse_mode='Markdown')

async def about_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send about message."""
    about_text = """About BLAQSTRATEGY

This bot shares educational information about:
- Digital advertising systems
- Campaign organization
- Workflow optimization for marketers

Content is educational and informational only."""
    
    keyboard = [[InlineKeyboardButton("Learn More", callback_data="learn_more")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        about_text,
        reply_markup=reply_markup,
        parse_mode='Markdown'
    )

async def education_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send educational resources."""
    edu_text = """Educational Resources

Digital advertising education includes:
1. Platform mechanics and algorithms
2. Campaign structure and organization
3. Workflow optimization techniques

These topics help marketers understand advertising systems better."""
    
    await update.message.reply_text(edu_text, parse_mode='Markdown')

async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle button callbacks."""
    query = update.callback_query
    await query.answer()
    
    if query.data == "about":
        await query.edit_message_text(
            "This bot provides educational information about digital advertising.\n\n"
            "For more details, visit the official Telegram channel.",
            parse_mode='Markdown'
        )
    elif query.data == "help":
        await query.edit_message_text(
            "Type /help to see available commands.\n\n"
            "For educational content, type /education.",
            parse_mode='Markdown'
        )
    elif query.data == "learn_more":
        await query.edit_message_text(
            "For comprehensive educational content on digital advertising, "
            "visit the BLAQSTRATEGY channel on Telegram.\n\n"
            "Search for BLAQSTRATEGY in Telegram.",
            parse_mode='Markdown'
        )

async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Log errors."""
    logger.warning(f"Update {update} caused error {context.error}")

def main():
    """Start the bot."""
    application = Application.builder().token(TOKEN).build()
    
    # Add command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("about", about_command))
    application.add_handler(CommandHandler("education", education_command))
    
    # Add callback handler for buttons
    application.add_handler(CallbackQueryHandler(button_callback))
    
    # Add error handler
    application.add_error_handler(error_handler)
    
    logger.info("Starting BLAQSTRATEGY bot (approval version)...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
