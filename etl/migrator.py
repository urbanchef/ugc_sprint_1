"""Migration tool for Clickhouse."""
import asyncio
import os
from typing import Optional

from aiochclient import ChClient
from aiohttp import ClientSession
from pydantic import BaseSettings


class ClickhouseSettings(BaseSettings):
    """Represents Clickhouse settings."""

    class Config:
        env_prefix = "CLICKHOUSE_"

    url: str = "http://localhost:8123/"
    user: Optional[str] = None
    password: Optional[str] = None
    database: str = "default"


async def make_migrations(client: ChClient):
    """Make migrations."""
    dir_list = os.listdir("./migrations")
    for file in dir_list:
        if file.endswith(".sql"):
            with open(f"./migrations/{file}", "r") as f:
                sql = f.read()
                await make_migration(client, sql)

    print("Migrations done")


async def make_migration(client: ChClient, sql: str):
    """Make a single migration."""
    for query in sql.split(";"):
        if query.strip():
            await client.execute(query)


async def main():
    async with ClientSession() as session:
        cfg = ClickhouseSettings()
        client = ChClient(session, **cfg.dict(exclude_none=True))
        await make_migrations(client)


if __name__ == "__main__":
    asyncio.run(main())
