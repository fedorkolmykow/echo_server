import asyncio


async def tcp_echo_client(message):
    reader, writer = await asyncio.open_connection(
        '127.0.0.1', 8888)

    writer.write(message.encode())
    await writer.drain()

    data = await reader.read(100)
    print(str(data.decode()))

    writer.close()
    await writer.wait_closed()

if __name__ == '__main__':
    while True:
        command = input()
        asyncio.run(tcp_echo_client(command))
