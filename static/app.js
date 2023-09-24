// Cambiar el color de fondo del encabezado al hacer clic en él
const header = document.querySelector('header');

header.addEventListener('click', () => {
    header.style.backgroundColor = '#FF5733';
});

// Hacer que la barra de navegación sea responsiva en pantallas pequeñas
const navToggle = document.querySelector('.nav-toggle');
const navUl = document.querySelector('nav ul');

navToggle.addEventListener('click', () => {
    navUl.classList.toggle('active');
});
