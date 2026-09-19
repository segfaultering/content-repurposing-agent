from pathlib import Path

from dotenv import find_dotenv
from pydantic import DirectoryPath, SecretStr
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    api_key: SecretStr
    root_dir: DirectoryPath
    model: str


settings = Settings(_env_file=find_dotenv())

DATA_DIR = Path(settings.root_dir / "data")
SYS_PROMPT = Path(DATA_DIR / "sys-prompt.md")

ENCODING = "utf-8"
