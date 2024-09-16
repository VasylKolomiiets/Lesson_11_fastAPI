import uvicorn

uvicorn.run(
    "links_bank.app:app",
    reload=True,
)