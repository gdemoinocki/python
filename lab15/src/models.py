from sqlalchemy import Column, ForeignKey, Integer, String, Date, Float, create_engine, Table
from sqlalchemy.orm import relationship, backref, Session, declarative_base

Base = declarative_base()
engine = create_engine('sqlite:///sqlite3.db')
department_teacher = Table(
    "association_table",
    Base.metadata,
    Column("departmnent_id", ForeignKey("department.id")),
    Column("teacher_id", ForeignKey("teacher.id")),
)

class Department(Base):
    __tablename__ = "department"

    id = Column(Integer, primary_key=True, unique=True)
    name = Column(String(10))
    institute = Column(String(10))
    count_teachers = relationship('Teacher', secondary = department_teacher,)

class Teacher(Base):
    __tablename__ = "teacher"

    id = Column(Integer, primary_key=True, unique=True)
    FIO = Column(String(25))
    Date_of_br = Column(Date)
    post_id = Column(Integer, ForeignKey("post.id"))
    department_id = Column(Integer, ForeignKey("department.id"))


class Post(Base):
    __tablename__ = "post"

    id = Column(Integer, primary_key=True, unique=True)
    name = Column(String(15))

Base.metadata.create_all(bind=engine)
