import sqlalchemy


path = '/home/vectra/projects/raspberrypi/db/desk.db'

db = create_engine('sqlite:///%s' %path)

metadata = BoundMetaData(db)
