from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, update, create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

Base = declarative_base()

class Command(Base):
    __tablename__ = "Command"
    id = Column('id', Integer, primary_key=True)
    command_name = Column('command_name', String, unique=True, nullable=False)
    token = Column('token', String, nullable=False, unique=True)
    hash = Column('hash', String, nullable=False)
    filepath = Column('filepath', String, nullable=False, unique=True)


    def __repr__(self):
        return f"<command_file:{self.command_name} on {self.filepath}>"





def create_table_command(engine):
    Base.metadata.create_all(engine)
    return

def add_command(session,command_name, token, hash, filepath):
    #if session.query(Command).filter_by(token=token).first() is None:
    tk = Command(command_name=command_name, token=token, hash=hash, filepath=filepath)
    session.add(tk)
    try:
        session.commit()
    except:
        session.rollback()
    #else:
    #    print('command already exists')


def get_command(session, command_name):
    if check_command_exists(session, command_name):
        return session.query(Command).filter_by(command_name=command_name).first()
    else:
        raise ValueError('command not found')

def check_command_exists(session, command_name):
    if session.query(Command).filter_by(command_name=command_name).first() is None:
        return False
    else:
        return True

def verify_command_hash(session, command_name, hash_file):
    if check_command_exists(session, command_name):
        hash_saved = get_command(session, command_name).hash
        if hash_saved == hash_file:
            return True
        else :
            return False

def update_command_hash(session, command_name, old_hash, new_hash):
    if verify_command_hash(session, command_name, old_hash):
        id = get_command(session, command_name).id
        session.query(Command).get(id).hash = new_hash
        try:
            session.commit()
        except:
            session.rollback()


def remove_command(session, token):
    if session.query(Command).filter_by(token=token).first() is not None:
        session.delete(session.query(Command).filter_by(token=token).first())
    else:
        print("token don't exist!")

def init_db():
    engine = create_engine("sqlite:///command.db", echo=False)
    Session = sessionmaker(bind=engine)
    ses = Session()
    create_table_command(engine)
    return engine, ses

if __name__ == '__main__':
    engine, ses = init_db()
    add_command(ses, 'command_test', '123soleil', 'hashloltest', 'test/path/lol/xd')
    print(f"test get_command: returning: {get_command(ses, 'command_test')}")
    print(f"test check_command_exists: returning: {check_command_exists(ses, 'command_test')}")
    print(f"test verify_command_hash: returning: { verify_command_hash(ses, 'command_test','hashloltest')}")
    print(f"test update_command_hash: returning: { update_command_hash(ses, 'command_test','hashloltest','new_hash_baby')}")
    print(f"test get_command_hash: returning: {get_command(ses, 'command_test').hash}")
    print(f"test remove_command: returning: {remove_command(ses, '123soleil')}")
    print(f"test check_command_exists: returning: {check_command_exists(ses, 'command_test')}")