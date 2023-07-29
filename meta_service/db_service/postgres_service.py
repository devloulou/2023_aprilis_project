from sqlalchemy import create_engine, text, inspect

class PostgresService:

    def __init__(self, url):
        self.engine = create_engine(url)
        self.insp = inspect(self.engine)

    def run_query(self, query, is_select=False):
        with self.engine.connect() as conn:
            try:
                result = None
                if not is_select:
                    conn.execute(text(query))
                else:
                    result = conn.execute(text(query))
                conn.commit()
            except Exception as e:            
                print(f"Error occured: {str(e)}")
                conn.rollback() # amennyi idejig futott a tranzakció, annyi ideig fog futni a rollback

        if result:
            return result
        

    def insert_data(self, query, data):
        with self.engine.connect() as conn:
            try:
                conn.execute(text(query), data)
                conn.commit()
            except Exception as e:            
                print(f"Error occured: {str(e)}")
                conn.rollback()

    def initialize_objects(self, obj):        
        for table, create in obj.items():
            if self.insp.has_table(table):
                continue
            
            self.run_query(create)


if __name__ == '__main__':
    from sql_helper import db_objects, select_meta
    url = "postgresql://postgres:postgres@localhost:5465/postgres"

    sql = PostgresService(url)

    # sql.initialize_objects(db_objects['tables'])

    sol = sql.run_query(select_meta, True)

    print([item[0] for item in sol.fetchall()])