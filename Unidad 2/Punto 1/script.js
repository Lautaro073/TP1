
const saludoBtn = document.getElementById('saludo-btn');
const saludoText = document.getElementById('saludo-text');

saludoBtn.addEventListener('click', () => {
    saludoText.textContent = '¡Hola! Bienvenidos a nuestra página web';

    saludoText.classList.remove('hidden');
    
    setTimeout(() => {
        saludoText.classList.add('hidden');
    }, 3000);
});

