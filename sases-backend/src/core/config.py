import os

class Config:
    def __init__(self):
        self.environment = os.getenv("ENVIRONMENT", "development")
        self.debug = os.getenv("DEBUG", "true").lower() in ("true", "1", "t")
        self.port = int(os.getenv("PORT", 8000))
        self.host = os.getenv("HOST", "0.0.0.0")
        self.database_url = os.getenv("DATABASE_URL", "sqlite:///./test.db")
        self.secret_key = os.getenv("SECRET_KEY", "your_secret_key")
        self.allowed_hosts = os.getenv("ALLOWED_HOSTS", "*").split(",")

config = Config()