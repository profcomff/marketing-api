from sqlalchemy.orm import Session
from marketing_api.settings import get_settings
from marketing_api.models.db import ActionsInfo
from datetime import datetime, timedelta


def count_users_in_daterange(session: Session, start_ts: datetime, end_ts: datetime) -> int:
    """
    Counts ActionsInfo rows with distinct user_id in daterange [from,to)
    :param start_ts: start date
    :param end_ts: end date
    :param session: sqlalchemy.orm.Session
    :return: int number of distinct users
    """
    res = session.query(ActionsInfo). \
        filter(
        start_ts <= ActionsInfo.create_ts,
        ActionsInfo.create_ts < end_ts,
    ). \
        distinct(ActionsInfo.user_id). \
        count()
    session.flush()
    return res


def count_dau(session: Session, start_ts: datetime = datetime(2022, 9, 1), end_ts=datetime.utcnow()) -> dict[str, int]:
    res = dict()
    curr = start_ts
    while end_ts >= curr:
        res[
            (curr + timedelta(days=1)).date().isoformat()
        ] = count_users_in_daterange(session, start_ts=curr, end_ts=(curr + timedelta(days=1)))
        curr += timedelta(days=1)
    return res


def count_wau(session: Session, start_ts: datetime = datetime(2022, 9, 1), end_ts=datetime.utcnow()) -> dict[str, int]:
    res = dict()
    curr = start_ts - timedelta(days=abs(start_ts.weekday() - (end_ts.weekday() - 6)))
    while end_ts >= curr + timedelta(days=6):
        res[
            f"{curr.date().isoformat()} - {(curr + timedelta(days=7)).date().isoformat()}"
        ] = count_users_in_daterange(session, start_ts=curr, end_ts=(curr + timedelta(days=7)))
        curr += timedelta(days=7)
    return res


def count_mau(session: Session, start_ts: datetime = datetime(2022, 9, 1), end_ts=datetime.utcnow()) -> dict[str, int]:
    res = dict()
    curr = start_ts - timedelta(days=30 - (end_ts.day - start_ts.day) % 30)
    while end_ts >= curr + timedelta(days=29):
        res[
            f"{curr.date().isoformat()} - {(curr + timedelta(days=30)).date().isoformat()}"
        ] = count_users_in_daterange(session, start_ts=curr, end_ts=(curr + timedelta(days=30)))
        curr += timedelta(days=30)
    return res
