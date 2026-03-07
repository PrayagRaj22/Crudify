from fastapi import FastAPI
from routes import user_routes, item_routes

app = FastAPI()

# Include router from sub-module
app.include_router(user_routes)
app.include_router(item_routes)


# ROOT

@app.get("/")
def root_point():
    return {
        "message": "Hello World"
    }
