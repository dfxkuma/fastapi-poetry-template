import uvicorn
from app.core.config import settings

if __name__ == "__main__":
    uvicorn.run(
        "app.main:server",
        host="0.0.0.0",
        port=settings.SERVER_PORT,
        reload_dirs=["app"],
        reload_includes=[".env"],
        reload=settings.ENVIRONMENT == "local",
    )
