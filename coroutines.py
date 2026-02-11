import asyncio
import time


#синхронный подход
def brew_coffe_sync():
    print("Начал варить кофе....")
    time.sleep(2) #Блокируется весь поток
    print("Кофе готов")

def toast_bread_sync():
    print("Начал жарить тост....")
    time.sleep(2) #Блокируется весь поток
    print("тост готов")

def run_sync():
    print("Синхронный завтрак")
    start = time.time()
    brew_coffe_sync()
    toast_bread_sync()
    print(f"Итог: {time.time() - start:.2f} сек. \n")


async def brew_coffe_async():
    print("[Async] Начал варить кофе....")
    #await говорит: "Я усну на 2 сек"
    await asyncio.sleep(2)
    print("[Async] Кофе готов")
    return "Капучино"

async def toast_bread_async():
    print("[Async] Начал жарить тост....")
    await asyncio.sleep(2)
    print("[Async] тост готов")
    return "Тост с сыром"



async def run_async():
    print("...............Асинхронный завтрак.............")
    start = time.time()

    #Мы создаем задачи (Tasks)
    #Они начинают работать одновременно
    task1 = asyncio.create_task(brew_coffe_async())
    task2 = asyncio.create_task(toast_bread_async())

    await task1
    await task2

    print(f"Итог: {time.time() - start:.2f} сек. \n")


if __name__ == "__main__":
    run_sync()

    asyncio.run(run_async())