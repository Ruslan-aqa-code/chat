from fastapi import FastAPI


def create_app():
    return FastAPI(
        title='Simple Kafka chat',
        docs_url="/api/docs",
        description="A simple Kafka + add example",
    )
