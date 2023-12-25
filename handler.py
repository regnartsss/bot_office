from aiogram import types
from aiogram import Router, F, Bot
import aiogram
from aiogram.filters import Command, CommandObject
router = Router()
router.my_chat_member.filter(F.chat.type == "supergroup")
router.message.filter(F.chat.type == "supergroup")


@router.message(Command('name'))
async def rename_admin(m: types.Message, command: CommandObject, bot: Bot):
    await bot.send_message(m.chat.id, text="Hi, {}".format(command.args))
    try:
        await bot.promote_chat_member(chat_id=m.chat.id, user_id=m.from_user.id, can_manage_chat=True)
    except aiogram.exceptions.TelegramBadRequest:
        pass
    try:
        await bot.set_chat_administrator_custom_title(chat_id=m.chat.id,user_id=m.from_user.id, custom_title=command.args)
    except aiogram.exceptions.TelegramBadRequest:
        pass


