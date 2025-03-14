from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to Real-Time Financial Data Processing API"}

@app.get("/status")
def status():
    return {"status": "API is running"}

# Add more endpoints here based on your requirements

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)

