#!/bin/bash
FECHA=$(date +%Y-%m-%d_%H-%M-%S)
"/c/xampp/mysql/bin/mysqldump.exe" -u root taller > "/c/Users/Usuario/taller_mecanic/backup_$FECHA.sql"
echo "Backup completado: backup_$FECHA.sql"