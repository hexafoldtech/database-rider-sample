from typing import Optional

import ormar

from core.database import Base


class User(Base):
    class Meta(MainMeta):
        tablename = "account_region"

    id: Optional[int] = ormar.Integer(primary_key=True)
    name: str = ormar.String(max_length=100)
    url: str = ormar.String(max_length=50)
    rtype: str = ormar.String(max_length=10, nullable=True)
    platform_id: str = ormar.String(max_length=50)
