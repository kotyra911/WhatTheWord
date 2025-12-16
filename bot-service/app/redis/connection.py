import asyncio
import redis.asyncio as redis
import os
from dotenv import load_dotenv
from config import REDIS_CFG as RCFG


redis_client = redis.Redis(host=RCFG["host"], port=RCFG["port"], db=RCFG["db"])

