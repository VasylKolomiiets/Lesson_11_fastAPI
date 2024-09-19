from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    server_host: str = '127.0.0.1'
    server_port: int = 8000
    database_url: str = 'sqlite:///./db.sqlite3'

    class Config:
        env_prefix = 'LINKER_'
        env_file='.env'  
        env_file_encoding='utf-8'


settings = Settings()  # Settings(_env_file='.env', _env_file_encoding='utf-8')

if __name__ == '__main__':
    print(settings)