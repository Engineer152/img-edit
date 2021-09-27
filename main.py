from keep_alive import keep_alive
import asyncio

def get_or_create_eventloop():
    try:
        return asyncio.get_event_loop()
    except RuntimeError as ex:
        if "There is no current event loop in thread" in str(ex):
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            return asyncio.get_event_loop()

async def main():
  print('Running...')
  keep_alive()
  get_or_create_eventloop()

if __name__ == '__main__':
  asyncio.run(main())