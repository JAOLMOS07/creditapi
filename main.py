# app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from interfaces.api.routes import router as product_router

app = FastAPI(
    title="Product API",
    version="1.0.0",
    description="API para gestionar productos con FastAPI"
)

# CORS config
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(product_router, prefix="/products", tags=["Products"])
