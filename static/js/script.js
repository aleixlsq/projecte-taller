// Al cargar la página, pedimos los vehículos a la API y llenamos el desplegable
document.addEventListener('DOMContentLoaded', function() {
    fetch('http://localhost:5000/vehicles')
        .then(response => response.json())
        .then(vehicles => {
            const select = document.getElementById('vehicle_id');
            vehicles.forEach(vehicle => {
                const option = document.createElement('option');
                option.value = vehicle.id;
                option.textContent = vehicle.matricula + ' — ' + vehicle.model;
                select.appendChild(option);
            });
        });
});

// Al enviar el formulario, mandamos los datos a la API
document.getElementById('citaForm').addEventListener('submit', function(e) {
    e.preventDefault(); // Evita que la página se recargue

    const dades = {
        vehicle_id: document.getElementById('vehicle_id').value,
        data_cita: document.getElementById('data_cita').value,
        servei_sollicitat: document.getElementById('servei_sollicitat').value
    };

    fetch('http://localhost:5000/appointments', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(dades)
    })
    .then(response => response.json())
    .then(data => {
        alert('Cita creada correctament!');
        document.getElementById('citaForm').reset();
    });
});