import asyncio

from app.services.accelpix_service import (
    api,
    on_trade,
    connection_started,
    connection_stopped
)

from app.config.settings import (
    ACCELPIX_API_KEY,
    ACCELPIX_HOST
)


async def main():

    api.on_connection_started(connection_started)
    api.on_connection_stopped(connection_stopped)

    api.on_trade_update(on_trade)

    await api.initialize(
        ACCELPIX_API_KEY,
        ACCELPIX_HOST
    )

    print("Subscribing to NIFTY...")

    await api.subscribeTrade(
        ["NIFTY-1"]
    )

    print("Subscription Successful")

    while True:
        await asyncio.sleep(1)


asyncio.run(main())