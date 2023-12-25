from aiogram import Bot, Dispatcher, types
import asyncio
import logging

BOT_TOKEN = "6220347577:AAFaM7ve2IPpbMNpe1yvZo6KfelDNzhYo_s"
import handler


def register_all_handlers(dp):
    dp.include_router(handler.router)


async def main():
    logging.basicConfig(level=logging.INFO,
                        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s', )

    bot = Bot(token=BOT_TOKEN, parse_mode="HTML")
    dp = Dispatcher()
    register_all_handlers(dp)

    try:
        await bot.send_message(765333440, "Бот Запущен")
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    finally:
        await bot.session.close()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.error("Bot stopped!")
