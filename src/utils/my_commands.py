from aiogram.types import BotCommand

def my_commands() -> list[BotCommand]:
    com = [
        BotCommand(command="/start", description="Start bot"),
        BotCommand(command="/help", description="Ja'rdem"),
        # BotCommand(command="/contact", description="Set my contact"),
        # BotCommand(command="/game", description="Start game"),
        # BotCommand(command="/removekb", description="Remove reply keyboard"),
        # BotCommand(command="/keyboard", description="Get Keyboard")
    ]
    return com