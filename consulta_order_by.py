from sqlalchemy.orm import sessionmaker
from crear_base_entidades import engine, HistoriaClinica

Session = sessionmaker(bind=engine)
session = Session()

historias = (
    session.query(HistoriaClinica)
    .order_by(HistoriaClinica.fecha_atencion.desc())
    .all()
)

for h in historias:
    print(f"{h.fecha_atencion} | {h.nombre_mascota} | {h.diagnostico_principal}")

session.close()