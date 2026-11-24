# crear_base_entidades.py
from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)
Base = declarative_base()


class Clinica(Base):
    __tablename__ = "clinica"

    id = Column(Integer, primary_key=True)
    nombre_comercial = Column(String(120), nullable=False)
    direccion = Column(String(200), nullable=False)
    veterinario_responsable = Column(String(120), nullable=False)

    consultorios = relationship("Consultorio", back_populates="clinica")

    def __repr__(self):
        return (
            f"Clinica(id={self.id}, nombre='{self.nombre_comercial}', "
            f"responsable='{self.veterinario_responsable}')"
        )


class Consultorio(Base):
    __tablename__ = "consultorio"

    id = Column(Integer, primary_key=True)
    nombre = Column(String(80), nullable=False)
    especialidad = Column(String(100), nullable=False)
    clinica_id = Column(Integer, ForeignKey("clinica.id"), nullable=False)

    clinica = relationship("Clinica", back_populates="consultorios")
    veterinarios = relationship("Veterinario", back_populates="consultorio")

    def __repr__(self):
        return (
            f"Consultorio(id={self.id}, nombre='{self.nombre}', "
            f"especialidad='{self.especialidad}')"
        )


class Veterinario(Base):
    __tablename__ = "veterinario"

    id = Column(Integer, primary_key=True)
    nombres_apellidos = Column(String(120), nullable=False)
    correo_electronico = Column(String(120), nullable=False, unique=True)
    numero_licencia = Column(String(50), nullable=False, unique=True)
    consultorio_id = Column(Integer, ForeignKey("consultorio.id"), nullable=False)

    consultorio = relationship("Consultorio", back_populates="veterinarios")
    historias_clinicas = relationship("HistoriaClinica", back_populates="veterinario")

    def __repr__(self):
        return (
            f"Veterinario(id={self.id}, nombre='{self.nombres_apellidos}', "
            f"licencia='{self.numero_licencia}')"
        )


class HistoriaClinica(Base):
    __tablename__ = "historia_clinica"

    id = Column(Integer, primary_key=True)
    fecha_atencion = Column(Date, nullable=False)
    diagnostico_principal = Column(String(200), nullable=False)
    tratamiento_prescrito = Column(String(250), nullable=False)
    nombre_mascota = Column(String(100), nullable=False)
    veterinario_id = Column(Integer, ForeignKey("veterinario.id"), nullable=False)

    veterinario = relationship("Veterinario", back_populates="historias_clinicas")

    def __repr__(self):
        return (
            f"HistoriaClinica(id={self.id}, fecha={self.fecha_atencion}, "
            f"mascota='{self.nombre_mascota}', diagnostico='{self.diagnostico_principal}')"
        )


if __name__ == "__main__":
    Base.metadata.create_all(engine)
    print("Base de datos y tablas creadas correctamente.")