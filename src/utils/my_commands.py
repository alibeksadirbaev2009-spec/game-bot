from aiogram.types import BotCommand

def my_commands() -> list[BotCommand]:
    com = [
        BotCommand(command="/start", description="Start bot"),
        BotCommand(command="/game", description="Game start"),
        BotCommand(command="/help", description="Ja'rdem"),
        BotCommand(command="/register", description="Dizimnen o'tiw"),
        BotCommand(command="/stats", description="Statistika"),
        BotCommand(command="/profile", description="Sizdin' mag'liwmatlarin'iz"),
        BotCommand(command="/change_profile", description="Mag'liwmatlardi almastiriw")
        # BotCommand(command="/contact", description="Set my contact"),
        # BotCommand(command="/game", description="Start game"),
        # BotCommand(command="/removekb", description="Remove reply keyboard"),
        # BotCommand(command="/keyboard", description="Get Keyboard")
    ]
    return com