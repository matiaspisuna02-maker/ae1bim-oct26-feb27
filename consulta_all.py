from sqlalchemy.orm import sessionmaker
from crear_base_entidades import engine, Clinica

Session = sessionmaker(bind=engine)
session = Session()

clinicas = session.query(Clinica).all()

print("=== Clínicas y número de Historias Clínicas asociadas ===")
for clinica in clinicas:
    total_historias = sum(
        len(vet.historias_clinicas)
        for cons in clinica.consultorios
        for vet in cons.veterinarios
    )
    print(f"- {clinica.nombre_comercial}: {total_historias} historia(s) clínica(s)")

session.close()