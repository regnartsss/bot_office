from aiogram import types
from aiogram import Router, F, Bot
import aiogram
from aiogram.filters import Command, CommandObject
router = Router()
router.my_chat_member.filter(F.chat.type == "supergroup")
router.message.filter(F.chat.type == "supergroup")


@router.message(Command('name'))
async def rename_admin(m: types.Message, command: CommandObject, bot: Bot):
    try:
        await bot.promote_chat_member(chat_id=m.chat.id, user_id=m.from_user.id, can_manage_chat=True)
    except aiogram.exceptions.TelegramBadRequest:
        pass
    temp = await bot.get_chat_administrators(chat_id=m.chat.id)
    print(temp[0].status)
    if temp[0].status == 'administrator':
        await bot.send_message(m.chat.id, text="Ваша роль в чате администратор, исправьте информацию о себе самостоятельно".format(command.args))
    else:
        await bot.set_chat_administrator_custom_title(chat_id=m.chat.id,user_id=m.from_user.id, custom_title=command.args)
        await bot.send_message(m.chat.id, text="Приветствую, {}".format(command.args))

