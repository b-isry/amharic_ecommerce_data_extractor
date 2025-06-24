# scraper.py
from telethon import TelegramClient
import csv
import os
from dotenv import load_dotenv
from preprocessor import preprocess_amharic_text

# Load environment variables
load_dotenv('.env')
api_id = os.getenv('TG_API_ID')
api_hash = os.getenv('TG_API_HASH')
phone = os.getenv('phone')

# Scraper function
async def scrape_channel(client, channel_username, writer, media_dir):
    entity = await client.get_entity(channel_username)
    channel_title = entity.title
    async for message in client.iter_messages(entity, limit=700):
        media_path = None
        if message.media and hasattr(message.media, 'photo'):
            filename = f"{channel_username}_{message.id}.jpg"
            media_path = os.path.join(media_dir, filename)
            await client.download_media(message.media, media_path)

        cleaned_text, tokens = preprocess_amharic_text(message.message)

        writer.writerow([
            channel_title,
            channel_username,
            message.id,
            message.message,
            cleaned_text,
            ' '.join(tokens),
            message.date,
            media_path
        ])

# Main script
async def main():
    client = TelegramClient('scraping_session', api_id, api_hash)
    await client.start()
    media_dir = 'photos'
    os.makedirs(media_dir, exist_ok=True)

    with open('preprocessed_telegram_data.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([
            'Channel Title',
            'Channel Username',
            'ID',
            'Original Message',
            'Cleaned Message',
            'Tokens',
            'Date',
            'Media Path'
        ])
        channels = [
            '@AwasMart','@Leyueqa','@ethio_brand_collection',
            '@meneshayeofficial','@nevacomputer'
        ]
        for channel in channels:
            await scrape_channel(client, channel, writer, media_dir)
            print(f"Scraped data from {channel}")

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
