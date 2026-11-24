# poblar_base.py
from datetime import date
from sqlalchemy.orm import sessionmaker
from crear_base_entidades import (
    engine,
    Clinica,
    Consultorio,
    Veterinario,
    HistoriaClinica,
)

Session = sessionmaker(bind=engine)
session = Session()

# 1. Clínicas
c1 = Clinica(
    nombre_comercial="VetVida Quito Norte",
    direccion="Av. Amazonas y Naciones Unidas, Quito",
    veterinario_responsable="Dra. Valeria Morales",
)
c2 = Clinica(
    nombre_comercial="Huellas del Valle",
    direccion="Av. Interoceánica km 14, Tumbaco",
    veterinario_responsable="Dr. Andrés Paredes",
)
c3 = Clinica(
    nombre_comercial="Patitas del Sur",
    direccion="Av. Maldonado y Morán Valverde, Quito",
    veterinario_responsable="Dra. Gabriela Rojas",
)

# 2. Consultorios
cons1 = Consultorio(nombre="Consultorio 101", especialidad="Medicina General", clinica=c1)
cons2 = Consultorio(nombre="Quirófano A", especialidad="Cirugía", clinica=c1)
cons3 = Consultorio(nombre="Consultorio 201", especialidad="Dermatología", clinica=c2)
cons4 = Consultorio(nombre="Consultorio 301", especialidad="Medicina General", clinica=c3)

# 3. Veterinarios
v1 = Veterinario(
    nombres_apellidos="Valeria Morales",
    correo_electronico="vmorales@vetvida.ec",
    numero_licencia="VET-EC-1024",
    consultorio=cons1,
)
v2 = Veterinario(
    nombres_apellidos="Carlos Herrera",
    correo_electronico="cherrera@vetvida.ec",
    numero_licencia="VET-EC-1088",
    consultorio=cons2,
)
v3 = Veterinario(
    nombres_apellidos="Andrés Paredes",
    correo_electronico="aparedes@huellasvalle.ec",
    numero_licencia="VET-EC-2041",
    consultorio=cons3,
)
v4 = Veterinario(
    nombres_apellidos="Gabriela Rojas",
    correo_electronico="grojas@patitassur.ec",
    numero_licencia="VET-EC-3015",
    consultorio=cons4,
)

# 4. Historias Clínicas
h1 = HistoriaClinica(
    fecha_atencion=date(2026, 10, 12),
    diagnostico_principal="Gastroenteritis leve",
    tratamiento_prescrito="Dieta blanda 3 días y probióticos",
    nombre_mascota="Max",
    veterinario=v1,
)
h2 = HistoriaClinica(
    fecha_atencion=date(2026, 10, 18),
    diagnostico_principal="Otitis externa",
    tratamiento_prescrito="Gotas óticas antibióticas cada 12h por 7 días",
    nombre_mascota="Luna",
    veterinario=v1,
)
h3 = HistoriaClinica(
    fecha_atencion=date(2026, 11, 2),
    diagnostico_principal="Fractura de radio",
    tratamiento_prescrito="Reducción quirúrgica y analgésicos",
    nombre_mascota="Rocky",
    veterinario=v2,
)
h4 = HistoriaClinica(
    fecha_atencion=date(2026, 11, 10),
    diagnostico_principal="Dermatitis alérgica",
    tratamiento_prescrito="Baño medicado con clorhexidina y antihistamínico",
    nombre_mascota="Milo",
    veterinario=v3,
)

session.add_all([c1, c2, c3, cons1, cons2, cons3, cons4, v1, v2, v3, v4, h1, h2, h3, h4])
session.commit()
session.close()
print("Datos insertados correctamente.")