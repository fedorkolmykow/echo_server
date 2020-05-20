import asyncio
from datetime import datetime
import sys
COMMANDS = ['echo', 'calendar', 'stop', ]


def process_message(message):
    if message[0:4] == 'echo':
        data = message[5:]
    elif message == 'calendar':
        data = datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M")
    elif message == 'stop':
        data = "Server stopped"
    else:
        data = f'Доступны следующие команды: {",".join(COMMANDS)}'
    return data


async def handle_echo(reader, writer):
    data = await reader.read(100)
    message = str(data.decode())
    addr = writer.get_extra_info('peername')

    print(f"Received {message} from {addr}")

    data = process_message(message)

    print(f"Send: {data}")
    writer.write(data.encode())
    await writer.drain()

    print("Close the connection")
    writer.close()

    if data == 'Server stopped':
        sys.exit(0)


async def main():
    server = await asyncio.start_server(
        handle_echo, '127.0.0.1', 8888)

    addr = server.sockets[0].getsockname()
    print(f'Serving on {addr}')

    async with server:
        await server.serve_forever()

if __name__ == '__main__':
    asyncio.run(main())


