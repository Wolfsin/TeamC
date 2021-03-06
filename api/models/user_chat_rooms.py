# Author:  Reika Kosuda
import sqlalchemy
from db import metadata, engine

user_chat_rooms = sqlalchemy.Table(
    "user_chat_rooms",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, index=True),
    sqlalchemy.Column("user_id", sqlalchemy.Integer, default=True),
    sqlalchemy.Column("chat_room_id", sqlalchemy.Integer, default=True),
    sqlalchemy.Column("valid", sqlalchemy.Integer, default=True),
)

metadata.create_all(bind=engine)
