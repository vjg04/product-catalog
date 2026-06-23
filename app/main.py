from fastapi import FastAPI
from sqlalchemy import text
from database import engine

app = FastAPI()

@app.get("/")
def health():
    return {"status":"running"}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/products")
def get_products():

    with engine.connect() as conn:

        result = conn.execute(
            text("select * from products")
        )

        rows = result.fetchall()

        return [
            {
                "product_id": r[0],
                "product_name": r[1],
                "price": float(r[2])
            }
            for r in rows
        ]