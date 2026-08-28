// =========================
// TYPING EFFECT
// =========================

const roles = [
    "Bioinformatics Developer",
    "AI Builder",
    "Full-Stack Learner",
    "Computational Biology Explorer"
];

let roleIndex = 0;
const typingText = document.getElementById("typing-text");
const reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

function changeRole() {
    if(!typingText) return;

    typingText.textContent = roles[roleIndex];
    roleIndex++;

    if(roleIndex >= roles.length){
        roleIndex = 0;
    }
}

changeRole();

if(!reducedMotion){
    setInterval(changeRole, 2000);
}

// =========================
// ACTIVE NAVBAR
// =========================

const sections = document.querySelectorAll("section");
const navLinks = document.querySelectorAll(".nav-link");

window.addEventListener("scroll", () => {
    let current = "";

    sections.forEach(section => {
        const sectionTop = section.offsetTop - 150;

        if(window.scrollY >= sectionTop){
            current = section.getAttribute("id");
        }
    });

    navLinks.forEach(link => {
        link.classList.remove("active");

        if(link.getAttribute("href") === `#${current}`){
            link.classList.add("active");
        }
    });
});
