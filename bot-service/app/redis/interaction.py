from app.redis.connection import redis_client

class RedisInteraction:

    @staticmethod
    async def add_user_language(user_telegram_id: int, language: str):
        try:
            if await RedisInteraction.check_user_language(user_telegram_id):  # return "1" if exists. "0" if not
                return False

            else:
                await redis_client.set(user_telegram_id, language)
                return True

        except Exception as e:
            print(e)



    @staticmethod
    async def check_user_language(user_telegram_id):

        return await redis_client.exists(user_telegram_id)


    @staticmethod
    async def get_user_language(user_telegram_id):

        if await RedisInteraction.check_user_language(user_telegram_id):   # return "1" if exists. "0" if not
            value = await redis_client.get(user_telegram_id)
            return value.decode()

        else:
            return False