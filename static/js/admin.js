document.addEventListener('DOMContentLoaded', function() {
    fetch('http://localhost:5000/appointments')
        .then(response => response.json())
        .then(cites => {
            const tbody = document.querySelector('#taulaCites tbody');
            cites.forEach(cita => {
                const fila = document.createElement('tr');
                fila.innerHTML = `
                    <td>${cita.id}</td>
                    <td>${cita.matricula}</td>
                    <td>${cita.model}</td>
                    <td>${cita.data_cita}</td>
                    <td>${cita.servei_sollicitat}</td>
                `;
                tbody.appendChild(fila);
            });
        });
});