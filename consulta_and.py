from datetime import date
from sqlalchemy import and_
from sqlalchemy.orm import sessionmaker
from crear_base_entidades import engine, HistoriaClinica

Session = sessionmaker(bind=engine)
session = Session()

historias = (
    session.query(HistoriaClinica)
    .filter(
        and_(
            HistoriaClinica.fecha_atencion >= date(2026, 11, 1),
            HistoriaClinica.diagnostico_principal.like("%Dermatitis%"),
        )
    )
    .all()
)

for h in historias:
    print(f"{h.fecha_atencion} | Mascota: {h.nombre_mascota} | Vet: {h.veterinario.nombres_apellidos}")

session.close()