from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes import predict

app = FastAPI(title="Student Performance Prediction API")

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for development; adjust in production
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)

# Include the predict router
app.include_router(predict.router, prefix="/predict", tags=["predict"])