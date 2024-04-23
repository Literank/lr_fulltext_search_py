from dataclasses import dataclass
import yaml


@dataclass
class SearchConfig:
    address: str
    index: str


@dataclass
class ApplicationConfig:
    page_size: int


@dataclass
class Config:
    app: ApplicationConfig
    search: SearchConfig


def parseConfig(filename: str) -> Config:
    with open(filename, 'r') as f:
        data = yaml.safe_load(f)
        return Config(
            ApplicationConfig(**data['app']),
            SearchConfig(**data['search'])
        )
