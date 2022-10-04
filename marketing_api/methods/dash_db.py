from sqlalchemy.orm import Session
from marketing_api.settings import get_settings
from marketing_api.models.db import User
from datetime import datetime, timedelta


def count_users_in_daterange(start_ts: datetime, end_ts: datetime, session: Session) -> int:
    res = session.query(User).filter(start_ts <= User.modify_ts < end_ts).all()
    session.flush()
    return res
