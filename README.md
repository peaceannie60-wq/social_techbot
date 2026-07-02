# BLAQSTRATEGY Telegram Bot

This bot redirects users to the [BLAQSTRATEGY](https://t.me/blaqmarqetnotify) channel which provides educational insights on digital advertising systems, campaign organization, and workflow optimization for marketers.

## Features

- Welcome message with channel information
- Inline keyboard to directly join the channel
- Commands: `/start`, `/help`, `/about`, `/channel`
- Educational content focus - compliant with Telegram Ads policies

## Deployment on Railway

1. Push this code to GitHub
2. Connect your repository to Railway
3. Add `BOT_TOKEN` as environment variable
4. Deploy!

## Environment Variables

| Variable | Description |
|----------|-------------|
| `BOT_TOKEN` | Your Telegram bot token from @BotFather |

## Local Development

```bash
# Install dependencies
pip install -r requirements.txt

# Run the bot
python bot.py
