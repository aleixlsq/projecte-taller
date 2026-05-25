[README.txt](https://github.com/user-attachments/files/28220744/README.txt)
- Taller Mecanico - 

Aplicación de gestión de citas para un taller mecanico

- Requisitos
Python 3.x
XAMPP (Apache + MySQL)

Instalación:

1. Clonar el repositorio:
```bash
git clone 
cd taller_mecanic
```
	
2. Crear el entorno virtual y instalar las dependencias:
```bash
python -m venv venv
source venv/Scripts/activate
pip install flask mysql-connector-python flask-cors
```
	
3. Base de datos:
Iniciar XAMPP y activar apache y MySQL
Importar 'backup.sql' desde phpMyAdmin

4.Executar la aplicación
```bash
python app.py
```
5. Acceder a los formularios:
Formulario de citas: http://localhost:5000
Panel de admin con todas las citas: http://localhost:5000/admin

Scripts:
Hay dos escripts que no se usan en la pagina pero están para poder ejecutar un backup y verificar que la api y la base de datos están activas:
`bash backup.sh`
`bash check_services.sh`

PD: si el Python "comando", no funciona usa py "comando" en mi caso es py.
Luego he usado Git GUI para ir ejecutando las comandas.
