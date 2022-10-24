##Antes de empezar el proyecto instalamos la libreria para SQL 
##teniendo el entorno virtual colocamos "pip install sqlalchemy"  es la libreria mas popular

##pára que al momento de crear una clase estemos creasndo una tabla de base de datos
#el sessionmaker sirve para el inicio de sesion en la base de datos sqlite

from sqlalchemy.orm import declarative_base, sessionmaker
##Para conectar a base de datos importamos el create_engine
#para hacer actualizaciones completas en la base de datos importamos el update y para eliminar el delete
#para relacionar tablas se importa el ForeignKey
from sqlalchemy import Column, String,Integer, create_engine, update, delete, ForeignKey
#para agregar propiedades hibridas
from sqlalchemy.ext.hybrid import hybrid_property


#Base de datos
Base = declarative_base()

#sqlalchemy se conecta a cualquier base de datos y adivina a que tecnologia
#engine representa la conexion de la base de datos
#sqlite: es una base de datos que trabaja en memoria y cuando se termina la ejecucion se destruye
#sirve para hacer ejemplos 
engine= create_engine("sqlite:///:memory:")

#Clase que al mismo tiempo es una columna de la base de datos
class Alumno(Base):
    #debe de tener el nombre de la tabla a la que se esta refiriendo de esta forma: 
    #esta diciendo que la clase alumnos hace referencia a la columna de la base de datos alumnos
    __tablename__ = 'alumnos'

    #Guardaremos un id en una columna de tipo Integer, la cual es la llave primaria. 
    #esta columna sera autoincrementable
    id= Column(Integer,primary_key=True)
    #para poner campo obligatorio se le agrega el nullable
    nombre= Column(String, nullable=False)
    #podemos ponerle un limite de caracteres en este 256
    #apellidos= Column(String(256))
    apellidos= Column(String(256))
    carnet = Column(Integer)
    
    #tambien puede tener metodos directamente de la tabla
    #y si quiero que sea hibrida le agrego el atributo @hybrid_property
    #lo que hace es que cambia la estructura de manera que no sea una funcion sino un atributo 
    #el cual el valor es lo que se define dentro.   
    @hybrid_property
    def nombre_completo(self):
        return f"{self.nombre} {self.apellidos}"


#para convertir y trasladar toda la informacion a la base de datos
#con este comando decimos que agarre todas las clases que hereden de Base y que cree todas las 
#tablas y columnas que necesita en la base de datos
Base.metadata.create_all(engine)

#Creando una sesión
 #para que se conecte a la base de datos
Session= sessionmaker(bind=engine)
#la sesion como tal al instanciar la clase
session= Session()

#INSTANCIAR UN ELEMENTO DE LA TABLA
#vamos a crear nuestro primer alumno
alumno= Alumno(
    nombre="Daniel",
    apellidos= "Coti",
    carnet=123
)
print(alumno.nombre)
#aqui aun no tiene una asignacion de id porque aun no se a agregado a la base de datos como tal 
print(alumno.id)

#INSERTAR ELEMENTO EN LA BASE DE DATOS
#Agregar alumno a la base de datos
session.add(alumno)
session.commit()



##OTRO ALUMNO
#INSTANCIAR UN ELEMENTO DE LA TABLA
#vamos a crear nuestro primer alumno
alumno= Alumno(
    nombre="MELISSA",
    apellidos= "Coti",
    carnet=5678
)
print(alumno.nombre)
#aqui aun no tiene una asignacion de id porque aun no se a agregado a la base de datos como tal 
print(alumno.id)

#INSERTAR ELEMENTO EN LA BASE DE DATOS
#Agregar alumno a la base de datos
session.add(alumno)
session.commit()





#otra forma de obtener los valores de la base de datos sin hacer una consulta como tal: 
session.refresh(alumno)
print(alumno.id)


#CONSULTA DE ALGUN DATO
#Hacer una consulta con ORM, estoy pidiendo que en la tabla alumno buseque en la columna nombre
#a una persona que se llame Daniel, y que devuelva el primero. 
alumno_db=session.query(Alumno).where(Alumno.nombre=="Daniel").first()
print(alumno_db.id)
#print(alumno.nombre_completo())
#para llamar la funcion como atributo 
print(alumno.nombre_completo)

#CONSULTA DE OBTENER TODOS LOS ALUMNOS
alumnos= session.query(Alumno).all()
print(alumnos)

#COMO DEVUELVE UN ARREGLO SE MANEJA COMO ARRAY
print(alumnos[1].nombre_completo)

#Cantidad de datos en la tabla

cantidad_alumnos= session.query(Alumno).count()
print(cantidad_alumnos)


#UPDATE, ACTUALIZACION DE DATOS pero solo para una cosa
melissa= session.query(Alumno).where(Alumno.id==2).first()
melissa.apellidos= "melissa"
session.add(melissa)
session.commit()

#ACTUALIZACION DE VARIOS. 
actualizacion=update(Alumno).values(carnet=9999)
session.execute(actualizacion)


alumno1= session.query(Alumno).first()
print(alumno1.carnet)

#ELIMINAR
borrado=delete(Alumno).where(Alumno.id==1)
session.execute(borrado)

alumno1= session.query(Alumno).where(Alumno.id==1).first()
print(alumno1)

#RELACIONES ENTRE TABLAS
#vamos a crear otra tabla
class Nota(Base):
    __tablename__="notas"
    id= Column(Integer, primary_key=True)
    curso= Column(String)
    #Relacion nota con alumnos
    #para relacionar tienen que ser el mismo tipo de dato
    alumno_id=Column(Integer,ForeignKey('alumnos.id'))





