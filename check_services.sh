#!/bin/bash
curl -s http://localhost:5000/vehicles && echo "API OK" || echo "API KO"
"/c/xampp/mysql/bin/mysqladmin.exe" -u root ping && echo "DB OK" || echo "DB KO"