from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    TOKEN:  str
    DB_USERNAME: str
    DB_PASSWORD: str
    DB_NAME: str

    @property
    def DB_URL(self):
        return f"postgresql+asyncpg://{self.DB_USERNAME}:{self.DB_PASSWORD}@localhost/{self.DB_NAME}"

    @property
    def DB_URL_2(self):
        return f"postgresql+psycopg2://{self.DB_USERNAME}:{self.DB_PASSWORD}@localhost/{self.DB_NAME}"

    model_config = SettingsConfigDict( 
        env_file=".env",
        extra="ignore"
    )

settings = Settings()