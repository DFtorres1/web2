from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    DATABASE_URI_FORMAT: str = "{db_engine}://{user}:{password}@{host}:{port}/{database}"
    DB_HOST: str
    DB_USER: str
    DB_PASSWORD: str
    DB_PORT: int
    DB_ENGINE: str
    DB_NAME: str

    model_config = SettingsConfigDict(env_file='.env')

    @property
    def DATABASE_URL(self) -> str:
        print(self.DB_ENGINE)
        print(self.DB_NAME)
        return self.DATABASE_URI_FORMAT.format(
            db_engine=self.DB_ENGINE,
            user=self.DB_USER,
            password=self.DB_PASSWORD,
            host=self.DB_HOST,
            port=self.DB_PORT,
            database=self.DB_NAME,
        )
    

settings = Settings()