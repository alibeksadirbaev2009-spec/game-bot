from src.database.session import async_session
from sqlalchemy import select
from src.models import User, Game
from sqlalchemy import update

class UserStatResult:
    def __init__(self, point, tie, defeat, total):
        self.point = point
        self.tie = tie
        self.defeat = defeat
        self.total = total


class UserRepo:
    @staticmethod
    async def create(
                    *, 
                    telegram_id: int, 
                    first_name: str, 
                    lastname: str, 
                    age: int, 
                    phone: str, 
                    location: str) -> User | None:
        async with async_session() as session:
            try:
                user = User(
                    telegram_id = telegram_id,
                    first_name = first_name,
                    lastname = lastname,
                    age = age,
                    phone = phone,
                    location = location 
                )
                session.add(user)
                await session.commit()
                return user
            except Exception as err:
                print(err)
                await session.rollback()

    @staticmethod
    async def get_me(*, telegram_id: int) -> User | None:
        async with async_session() as session:
            user = (
                await session.execute(
                    select(User)
                    .where(User.telegram_id == telegram_id)
                )
            ).scalar_one_or_none()
            return user 

    @staticmethod
    async def update_points(
        *,
        telegram_id: int,
        point: int | None = None,
        tie: int | None = None,
        defeat: int | None = None,
        total: int = 1
        ) -> User | None:
        async with async_session() as session:
            try:
                user = (
                    await session.execute(
                        select(User)
                        .where(User.telegram_id == telegram_id)
                    )
                ).scalar_one_or_none()

                if user is None:
                    return

                game = (
                    await session.execute(
                        select(Game)
                        .where(Game.user_id == user.id)
                    )
                ).scalar_one_or_none()

                if game is None:
                    new_game = Game(
                        user_id = user.id,
                        point = point or 0,
                        tie = tie or 0,
                        defeat = defeat or 0,
                        total = total
                    )
                    session.add(new_game)
                    await session.commit()
                    return new_game

                if point is not None:
                    game.point += point

                if tie is not None:
                    game.tie += tie

                if defeat is not None:
                    game.defeat += defeat

                game.total += total
                await session.commit()
                return game
            except Exception:
                await session.rollback()

    @staticmethod
    async def is_exsisit(telegram_id: int) -> bool:
        async with async_session() as sesssion:
            user = (
                await sesssion.execute(
                    select(User.id)
                    .where(User.telegram_id == telegram_id)
                )
            ).scalar_one_or_none()
            return user is not None

    @staticmethod
    async def get_statas(telegram_id: int) -> UserStatResult:
        async with async_session() as session:
            game = (
                await session.execute(
                    select(Game.point, Game.tie, Game.defeat, Game.total)
                    .join(User, User.id == Game.user_id)
                    .where(User.telegram_id == telegram_id)
                )
            ).fetchone()
            if not game:
                return UserStatResult(point=0, tie=0, defeat=0, total=0)
            return UserStatResult(point=game[0], tie=game[1], defeat=game[2], total=game[3])

    @staticmethod
    async def get_user_by_telegram_id(telegram_id: int):
        async with async_session() as session:
            result = await session.execute(
                select(User)
                .where(User.telegram_id == telegram_id)
            )
            return result.scalar_one_or_none()

    @staticmethod
    async def update_profile(telegram_id, data:dict):
        async with async_session() as session:
            await session.execute(
                update(User)
                .where(User.telegram_id == telegram_id)
                .values(**data)
            )
            await session.commit()
            