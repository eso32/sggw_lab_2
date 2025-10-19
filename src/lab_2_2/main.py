import random
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from lab_2_2.models import Base, Experiment, DataPoint


engine = create_engine("sqlite:///sqlalchemy_project.db", echo=True)
Base.metadata.create_all(engine)
print("Baza danych i tabele zostały utworzone.")

Session = sessionmaker(bind=engine)

# with Session() as session:
#     for i in range(2):
#         new_experiment = Experiment(
#             title=f"Random Experiment {i+1}",
#             experiment_type=random.randint(1, 5)
#         )
#         session.add(new_experiment)

#     for i in range(10):
#         new_experiment = DataPoint(
#             real_value=random.random(),
#             target_value=random.random()
#         )
#         session.add(new_experiment)
    
#     session.commit()

#     print("\n - - - - - - - - - ")

#     experiments = session.query(Experiment).all();
#     data_points = session.query(DataPoint).all();
#     for e in experiments:
#         print(f"id: {e.id} | finished: {e.finished}")
    
#     for dp in data_points:
#         print(f"id: {dp.id}")

#     print(f"Experiments: {len(experiments)}")
#     print(f"DataPoints: {len(data_points)}")
    
#     session.query(Experiment).update({Experiment.finished: True})
#     session.commit()

#     session.query(Experiment).delete()
#     session.query(DataPoint).delete()
#     session.commit()

#     print("KONIEC")