from sqlalchemy.orm import sessionmaker
from crear_base_entidades import engine, Consultorio

Session = sessionmaker(bind=engine)
session = Session()

consultorios = (
    session.query(Consultorio)
    .filter(Consultorio.especialidad == "Medicina General")
    .all()
)

for c in consultorios:
    print(f"{c.nombre} ({c.especialidad}) - Clínica: {c.clinica.nombre_comercial}")

session.close()