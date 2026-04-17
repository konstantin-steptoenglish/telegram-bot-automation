import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
CHANNEL_ID = os.getenv('CHANNEL_ID')
TIMEZONE = 'Asia/Almaty'

RED_FLAGS = {
    'politics': ['выбор', 'партия', 'политик', 'война', 'конфликт', 'геополитик'],
    'lgbtq': ['лгбт', 'гей', 'лесбиянка', 'трансгендер'],
    'race': ['раса', 'национальность', 'этнос', 'стереотип'],
    'war': ['война', 'конфликт', 'беженец', 'боевик']
}
