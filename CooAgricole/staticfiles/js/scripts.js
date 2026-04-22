// scripts.js

// Fonction pour afficher une alerte lorsque l'utilisateur clique sur un bouton
function showAlert() {
    alert('Bienvenue sur CooAgricole !');
}

// Fonction pour afficher un message de bienvenue
function showWelcomeMessage() {
    const welcomeMessage = document.createElement('div');
    welcomeMessage.className = 'alert alert-success';
    welcomeMessage.role = 'alert';
    welcomeMessage.innerText = 'Bienvenue sur CooAgricole ! Explorez nos fonctionnalités.';
    
    // Ajoute le message à la page
    const container = document.querySelector('.container');
    if (container) {
        container.prepend(welcomeMessage); // Ajoute le message en haut du conteneur
    }

    // Supprime le message après 5 secondes
    setTimeout(() => {
        welcomeMessage.remove();
    }, 5000);
}

// Attacher un événement au chargement de la page
document.addEventListener('DOMContentLoaded', (event) => {
    // Ajouter un événement à un bouton avec l'ID 'alert-button'
    const alertButton = document.getElementById('alert-button');
    if (alertButton) {
        alertButton.addEventListener('click', showAlert);
    }

    // Afficher le message de bienvenue
    showWelcomeMessage();
});
const text = document.getElementById("dynamic-text");
let i = 0;
const messages = [
    "Découvrez les avantages de la coopération agricole.",
    "35 % du PIB et 82 % de la population active impliqués.",
    "Rejoignez une coopérative et améliorez vos rendements agricoles !",
];

setInterval(() => {
    text.innerText = messages[i];
    i = (i + 1) % messages.length;
}, 5000);
