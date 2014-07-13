import sqlalchemy

path = '/home/vectra/projects/raspberrypi/db/desk.db'

db = sqlalchemy.create_engine('sqlite:///%s' %path)

metadata = sqlalchemy.BoundMetaData(db)

metrics = sqlalchemy.Table('os_metrics', metadata,
                Column('id', Integer, primary_key=True),
                Column('cpu_load', float),
                Column('cpu_percent' float),
                Column('swap_memory', float)
            )

specs = sqlalchemy.Table('OS', metadata,
              sqlalchemy.Column(id, Integer, primary_key=True),
              
)
