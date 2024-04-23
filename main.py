from fastapi import FastAPI

from books.adapter import make_router
from books.application import WireHelper
from books.infrastructure.config import parseConfig

CONFIG_FILENAME = "config.yml"

c = parseConfig(CONFIG_FILENAME)
wire_helper = WireHelper.new(c)
app = FastAPI()
make_router(app, wire_helper)
