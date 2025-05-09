from fastapi import FastAPI
from app.api.routes import router as api_router
from fastapi.responses import HTMLResponse

app = FastAPI()
app.include_router(api_router)

@app.get("/", response_class=HTMLResponse)
async def read_root():
    return """
    <html>
        <head>
            <title>FastAPI Python Backend</title>
        </head>
        <body>
            <h1>FastAPI Python Backend</h1>
        </body>
    </html>
    """