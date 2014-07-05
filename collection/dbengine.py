import sqlalchemy


path = '/home/vectra/projects/raspberrypi/db/desk.db'

db = create_engine('sqlite:///%s' %path)

metadata = BoundMetaData(db)


metrics = Table('os_metrics', metadata\
                Column('id', Integer, primary_key=True)
                Column('cpu_load', float),
                Column('cpu_percent' float),
                Column('swap_memory', float)
            )
