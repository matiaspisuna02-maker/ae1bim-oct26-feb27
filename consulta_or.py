from sqlalchemy import or_
from sqlalchemy.orm import sessionmaker
from crear_base_entidades import engine, Veterinario

Session = sessionmaker(bind=engine)
session = Session()

veterinarios = (
    session.query(Veterinario)
    .filter(
        or_(
            Veterinario.numero_licencia == "VET-EC-1024",
            Veterinario.correo_electronico.like("%huellasvalle.ec"),
        )
    )
    .all()
)

print("=== Veterinarios con licencia VET-EC-1024 o correo de Huellas del Valle ===")
for v in veterinarios:
    print(f"- {v.nombres_apellidos} | Licencia: {v.numero_licencia} | Consultorio: {v.consultorio.nombre}")

session.close()