from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, DateTime, select
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
from datetime import datetime
import uuid

class PostgreSQLDataWriter:
    def __init__(self, db_url):
        self.engine = create_engine(db_url)
        self.metadata = MetaData(bind=self.engine)
        self.session = sessionmaker(bind=self.engine)()

    def table_exists(self, table_name):
        return table_name in self.metadata.tables

    def create_table(self, table_name):
        if not self.table_exists(table_name):
            table = Table(
                table_name,
                self.metadata,
                Column('account_id', Integer, primary_key=True),
                Column('platform', String),
                Column('account', String),
                Column('account_url', String),
                Column('name', String),
                Column('followers', Integer),
                Column('profile_image_url', String),
                Column('bio', String),
                Column('created_date_utc', DateTime),
                Column('updated_date_utc', DateTime),
            )
            table.create()

    def write_data(self, data):
        for entry in data:
            table_name = 'social_account_info'  # Replace with your table name
            self.create_table(table_name)
            table = self.metadata.tables[table_name]
            name = entry['name']
            updated_at = datetime.strptime(entry['updated_date_utc'], '%Y-%m-%d %H:%M:%S')

            # Check if the record already exists based on 'name'
            select_query = select([table.c.account_id]).where(table.c.name == name)
            result = self.session.execute(select_query)
            existing_record = result.fetchone()

            if existing_record:
                # Record exists, update 'updated_date_utc'
                update_query = table.update().where(table.c.account_id == existing_record[0]).values(updated_date_utc=updated_at)
                self.session.execute(update_query)
            else:
                # Record doesn't exist, insert a new one
                insert_query = table.insert().values(
                    platform=entry['platform'],
                    account=str(uuid.uuid4()),
                    account_url=entry['account_url'],
                    name=name,
                    followers=entry['followers'],
                    profile_image_url=entry['profile_image_url'],
                    bio=entry['bio'],
                    created_date_utc=datetime.strptime(entry['created_date_utc'], '%Y-%m-%d %H:%M:%S'),
                    updated_date_utc=updated_at
                )
                try:
                    self.session.execute(insert_query)
                except IntegrityError:
                    # Handle IntegrityError if there's a unique constraint violation (e.g., duplicate 'name')
                    pass

        self.session.commit()

    def close(self):
        self.session.close()