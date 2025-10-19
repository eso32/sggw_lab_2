from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, ForeignKey, Table
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime

Base = declarative_base()

experiment_subject = Table(
    "experiment_subject",
    Base.metadata,
    Column("experiment_id", Integer, ForeignKey("experiment.id"), primary_key=True),
    Column("subject_id", Integer, ForeignKey("subject.id"), primary_key=True)
)

class Experiment(Base):
    __tablename__ = "experiment"
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    experiment_type = Column(Integer, nullable=False)
    finished = Column(Boolean, default=False)
    data_points = relationship("DataPoint", back_populates="experiment", uselist=True)
    subjects = relationship("Subject", secondary=experiment_subject, back_populates="experiments")

class DataPoint(Base):
    __tablename__ = "datapoint"
    id = Column(Integer, primary_key=True)
    real_value = Column(Float, nullable=False)
    target_value = Column(Float, nullable=False)
    experiment_id = Column(Integer, ForeignKey("experiment.id"))
    experiment = relationship("Experiment", back_populates="data_points")

class Subject(Base):
    __tablename__ = "subject"
    id = Column(Integer, primary_key=True)
    gdpr_accepted = Column(Boolean, default=False)
    experiments = relationship("Experiment", secondary=experiment_subject, back_populates="subjects")