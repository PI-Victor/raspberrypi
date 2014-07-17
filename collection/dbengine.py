import sqlalchemy
import os

#this should also got into the config later
#path = '/home/vectra/projects/raspberrypi/db/rpimon.db'
path = '/'.join([os.dirname(os.dirname(os.path.realpath(__file__))),'db','rpimon.db' ])
db = sqlalchemy.create_engine('sqlite:///%s' %path, echo=True)
metadata = sqlalchemy.BoundMetaData(db)
Base = sqlalchemy.declarative_base()



class Metrics(Base):
    __tablename__ = 'os_metrics'
    id = sqlalchemy.Column(sqlalchemy.integer, sqlalchemy.primary_key=True)
    cpu_load = sqlalchemy.Column(sqlalchemy.Float)
    cpu_percent = sqlalchemy.Column(sqlalchemy.Float)
    swap_memory = sqlalchemy.Column(sqlalchemy.Float)
    network_load = sqlalchemy.Column(sqlalchemy.Float)

specs = sqlalchemy.Table('OS', metadata,
                sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.primary_key=True),
              
)
