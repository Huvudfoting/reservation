import uuid
from dataclasses import dataclass
from datetime import datetime


@dataclass
class NameReservation:
    name: str
    secret: str = str(uuid.uuid4())
    timestamp: str = datetime.utcnow().isoformat()
    confirmed: bool = False
