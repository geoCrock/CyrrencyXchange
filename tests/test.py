from fastapi import FastAPI, Request, Response, HTTPException
import httpx
import uvicorn

app = FastAPI()

# Задаем адрес целевого сервера, на который будем перенаправлять запросы
TARGET_SERVER_URL = 'http://example.com'


@app.middleware("http")
async def reverse_proxy(request: Request, call_next):
    # Получаем URL запроса от клиента
    url = f"{TARGET_SERVER_URL}{request.url.path}"

    # Перенаправляем запрос на целевой сервер
    async with httpx.AsyncClient() as client:
        response = await client.request(
            method=request.method,
            url=url,
            headers={key: value for (key, value) in request.headers.items() if key != 'Host'},
            content=request.stream(),
            cookies=request.cookies
        )

        # Создаем ответ для клиента на основе ответа от целевого сервера
        return Response(
            content=response.content,
            status_code=response.status_code,
            headers=response.headers
        )


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)