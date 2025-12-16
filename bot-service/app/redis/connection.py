import asyncio
import redis.asyncio as redis
import os
from dotenv import load_dotenv
from config import REDIS_CFG as RCFG


async def redis_init():

    redis_connection = redis.Redis(host=RCFG["host"], port=RCFG["port"], db=RCFG["db"])

    # Connection Test
    try:
        await redis_connection.ping()
        print("Redis connected")

        return redis_client

    except Exception as e:
        print(e)

redis_client = redis_init()
