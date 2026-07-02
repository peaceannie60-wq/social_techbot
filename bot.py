import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

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

# Channel configuration
CHANNEL_LINK = "https://t.me/blaqmarqetnotify"
CHANNEL_USERNAME = "@blaqmarqetnotify"

# Welcome message (NO LINK IN TEXT)
WELCOME_MESSAGE = """Welcome to BLAQSTRATEGY! 👋

We're glad to have you here. This channel is dedicated to providing **educational insights** for marketers who want to master the technical side of digital advertising.

**What you'll learn:**
• **Advertising Systems:** A deep dive into how platforms really work, from auction dynamics to algorithmic nuances.
• **Campaign Organization:** Proven structures for account setup, audience segmentation, and scalable campaign architecture.
• **Workflow Optimization:** Practical strategies to streamline your processes, reduce wasted spend, and improve team efficiency.

Our content is focused on **knowledge and methodology**—not quick fixes or guaranteed results. We believe in equipping you with the systems and understanding to make better, data-driven decisions.

**To get started:**
1. Turn on notifications so you don't miss an insight.
2. Feel free to browse the previous posts in the channel.
3. If you have a specific topic you'd like us to cover, let us know!

Thank you for joining. Let's build better campaigns, together."""

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send welcome message when /start is issued."""
    user = update.effective_user
    logger.info(f"User {user.first_name} (ID: {user.id}) started the bot")
    
    # Create inline keyboard with ONLY the channel link in button
    keyboard = [
        [InlineKeyboardButton("📢 Join BLAQSTRATEGY Channel", url=CHANNEL_LINK)],
        [InlineKeyboardButton("📚 View Channel Content", url=CHANNEL_LINK)]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    # Send welcome message (text without link)
    await update.message.reply_text(
        WELCOME_MESSAGE,
        reply_markup=reply_markup,
        parse_mode='Markdown',
        disable_web_page_preview=True
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send help message when /help is issued."""
    help_text = f"""📖 **BLAQSTRATEGY Bot Help**

This bot helps you discover educational content about digital advertising.

**Commands:**
/start - Show welcome message
/help - Show this help message
/about - Learn more about BLAQSTRATEGY
/channel - Get the channel link

**Channel:** {CHANNEL_USERNAME}

For any issues, contact the channel admin."""
    
    await update.message.reply_text(help_text, parse_mode='Markdown')

async def about_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send about message when /about is issued."""
    about_text = f"""📊 **About BLAQSTRATEGY**

BLAQSTRATEGY provides **educational insights** on:

✅ Digital advertising systems
✅ Campaign organization  
✅ Workflow optimization for marketers

We focus on methodology, systems thinking, and data-driven approaches to help you build better campaigns.

**Join us:** {CHANNEL_USERNAME}

*No guarantees, just knowledge.*"""
    
    keyboard = [[InlineKeyboardButton("🔗 Visit Channel", url=CHANNEL_LINK)]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        about_text,
        reply_markup=reply_markup,
        parse_mode='Markdown'
    )

async def channel_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send channel link when /channel is issued."""
    keyboard = [
        [InlineKeyboardButton("📢 Join Channel", url=CHANNEL_LINK)],
        [InlineKeyboardButton("📋 Copy Channel Link", url=CHANNEL_LINK)]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        f"📢 **Join BLAQSTRATEGY**\n\n"
        f"Click the button below to join our channel for educational insights on digital advertising.\n\n"
        f"**Channel:** {CHANNEL_USERNAME}",
        reply_markup=reply_markup,
        parse_mode='Markdown'
    )

async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Log errors."""
    logger.warning(f"Update {update} caused error {context.error}")

def main():
    """Start the bot."""
    # Create application
    application = Application.builder().token(TOKEN).build()
    
    # Add command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("about", about_command))
    application.add_handler(CommandHandler("channel", channel_command))
    
    # Add error handler
    application.add_error_handler(error_handler)
    
    # Start the bot
    logger.info("Starting BLAQSTRATEGY bot...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
