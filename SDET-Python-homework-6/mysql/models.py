from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Top4xx(Base):
    __tablename__ = 'top4xx'
    __table_args__ = {'mysql_charset': 'utf8'}

    def __repr__(self):
        return f"<top4xx(" \
               f"id='{self.id}'," \
               f"url='{self.url}', " \
               f"statuscode='{self.statuscode}', " \
               f"requestsize='{self.requestsize}', " \
               f"ipadress='{self.ipadress}'" \
               f")>"

    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(String(500), nullable=False)
    statuscode = Column(String(50), nullable=False)
    requestsize = Column(Integer, nullable=False)
    ipadress = Column(String(50), nullable=False)


class Top5xx(Base):
    __tablename__ = 'top5xx'
    __table_args__ = {'mysql_charset': 'utf8'}

    def __repr__(self):
        return f"<top5xx(" \
               f"id='{self.id}'," \
               f"ipadress='{self.ipadress}', " \
               f"reqestsize='{self.reqestsize}'" \
               f")>"

    id = Column(Integer, primary_key=True, autoincrement=True)
    ipadress = Column(String(100), nullable=False)
    reqestsize = Column(Integer, nullable=False)


class Top10Urls(Base):
    __tablename__ = 'top10urls'
    __table_args__ = {'mysql_charset': 'utf8'}

    def __repr__(self):
        return f"<top10urls(" \
               f"id='{self.id}'," \
               f"url='{self.url}', " \
               f"count='{self.count}'" \
               f")>"

    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(String(200), nullable=False)
    count = Column(Integer, nullable=False)


class MethodCounts(Base):
    __tablename__ = 'methodcounts'
    __table_args__ = {'mysql_charset': 'utf8'}

    def __repr__(self):
        return f"<methodcounts(" \
               f"id='{self.id}'," \
               f"method='{self.method}', " \
               f"count='{self.count}'" \
               f")>"

    id = Column(Integer, primary_key=True, autoincrement=True)
    method = Column(String(200), nullable=False)

    count = Column(Integer, nullable=False)


class NumberOfRequests(Base):
    __tablename__ = 'number_of_requests'
    __table_args__ = {'mysql_charset': 'utf8'}

    def __repr__(self):
        return f"<number_of_requests(" \
               f"id='{self.id}'," \
               f"count='{self.count}'" \
               f")>"

    id = Column(Integer, primary_key=True, autoincrement=True)
    count = Column(String(50), nullable=False)
