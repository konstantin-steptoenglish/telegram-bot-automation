from telegram.ext import Application
from telegram import Bot
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from content_generator import ContentGenerator
from config import TELEGRAM_BOT_TOKEN, CHANNEL_ID, TIMEZONE
import logging
import asyncio
import pytz

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TelegramBot:
    def __init__(self):
        self.bot = Bot(token=TELEGRAM_BOT_TOKEN)
        self.channel_id = CHANNEL_ID
        self.generator = ContentGenerator()
        self.scheduler = AsyncIOScheduler(timezone=pytz.timezone(TIMEZONE))

    async def publish_scholarship_post(self):
        post = self.generator.generate_scholarship_post()
        if post:
            await self.bot.send_message(chat_id=self.channel_id, text=post, parse_mode='HTML')
            logger.info('Scholarship post published')
        else:
            logger.warning('Post rejected - red flags detected')

    async def publish_lifehack_post(self):
        post = self.generator.generate_lifehack_post()
        if post:
            await self.bot.send_message(chat_id=self.channel_id, text=post, parse_mode='HTML')
            logger.info('Lifehack post published')
        else:
            logger.warning('Post rejected - red flags detected')

    def start(self):
        self.scheduler.add_job(self.publish_scholarship_post, 'cron', hour=8, minute=0, timezone=TIMEZONE, id='scholarship_post')
        self.scheduler.add_job(self.publish_lifehack_post, 'cron', hour=14, minute=30, timezone=TIMEZONE, id='lifehack_post')
        self.scheduler.start()
        logger.info('Bot started and scheduler running')
        try:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            loop.run_forever()
        except KeyboardInterrupt:
            self.scheduler.shutdown()
            logger.info('Bot stopped')

if __name__ == '__main__':
    bot = TelegramBot()
    bot.start()