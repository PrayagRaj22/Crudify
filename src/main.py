from fastapi import FastAPI
from .routes import api_routes, item_routes

app = FastAPI()

# Include router from sub-module
app.include_router(api_routes)
app.include_router(item_routes)


# ROOT


@app.get("/")
def root_point():
    return {"message": "Hello World"}


@app.get("/health")
def health_check():
    return {"status": "OK"}
