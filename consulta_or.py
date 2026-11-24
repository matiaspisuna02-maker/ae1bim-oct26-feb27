from sqlalchemy import or_
from sqlalchemy.orm import sessionmaker
from crear_base_entidades import engine, Consultorio

Session = sessionmaker(bind=engine)
session = Session()

consultorios = (
    session.query(Consultorio)
    .filter(
        or_(
            Consultorio.especialidad == "Cirugía",
            Consultorio.especialidad == "Dermatología",
        )
    )
    .all()
)

for c in consultorios:
    print(f"{c.nombre} - {c.especialidad} ({c.clinica.nombre_comercial})")

session.close()