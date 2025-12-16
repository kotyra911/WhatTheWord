from app.redis.connection import redis_client


async def add_user_language(user_telegram_id, language):

    if check_user_language(user_telegram_id):  # return "1" if exists. "0" if not
        return False

    else:
        await redis_client.set(user_telegram_id, language)
        return True


async def check_user_language(user_telegram_id):

    return redis_client.exists(user_telegram_id)


async def get_user_language(user_telegram_id):

    if check_user_language(user_telegram_id):  # return "1" if exists. "0" if not
        value = await redis_client.get(user_telegram_id)
        return value.decode()

    else:
        return False