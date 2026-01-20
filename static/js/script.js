// 1. Typewriter Effect
const textElement = document.getElementById('typewriter');
const phrases = ["Full Stack Web Developer", "Java Enthusiast", "UI/UX Designer", "Problem Solver"];
let phraseIndex = 0;
let charIndex = 0;
let isDeleting = false;

function type() {
    const currentPhrase = phrases[phraseIndex];

    if (isDeleting) {
        textElement.textContent = currentPhrase.substring(0, charIndex - 1);
        charIndex--;
    } else {
        textElement.textContent = currentPhrase.substring(0, charIndex + 1);
        charIndex++;
    }

    if (!isDeleting && charIndex === currentPhrase.length) {
        isDeleting = true;
        setTimeout(type, 2000);
    } else if (isDeleting && charIndex === 0) {
        isDeleting = false;
        phraseIndex = (phraseIndex + 1) % phrases.length;
        setTimeout(type, 500);
    } else {
        setTimeout(type, isDeleting ? 50 : 100);
    }
}
document.addEventListener('DOMContentLoaded', type);

// 2. Active Scroll Link
const sections = document.querySelectorAll('section');
const navLinks = document.querySelectorAll('.nav-links a');

window.addEventListener('scroll', () => {
    let current = '';
    sections.forEach(section => {
        const sectionTop = section.offsetTop;
        const sectionHeight = section.clientHeight;
        if (pageYOffset >= (sectionTop - sectionHeight / 3)) {
            current = section.getAttribute('id');
        }
    });

    navLinks.forEach(a => {
        a.classList.remove('active');
        if (a.getAttribute('href').includes(current)) {
            a.classList.add('active');
        }
    });

    // Navbar Glass effect stronger on scroll
    const nav = document.querySelector('nav');
    if(window.scrollY > 50) {
        nav.style.boxShadow = "0 4px 6px -1px rgba(0,0,0,0.1)";
    } else {
        nav.style.boxShadow = "none";
    }
});

// 3. Mobile Menu
const menuToggle = document.querySelector('.menu-toggle');
const navUl = document.querySelector('.nav-links');

menuToggle.addEventListener('click', () => {
    if(navUl.style.display === 'flex') {
        navUl.style.display = 'none';
    } else {
        navUl.style.display = 'flex';
        navUl.style.flexDirection = 'column';
        navUl.style.position = 'absolute';
        navUl.style.top = '70px';
        navUl.style.right = '0';
        navUl.style.background = 'white';
        navUl.style.width = '100%';
        navUl.style.padding = '2rem';
        navUl.style.boxShadow = '0 10px 15px -3px rgba(0,0,0,0.1)';
    }
});

// 4. Theme Toggle
const themeToggle = document.getElementById('theme-toggle');
const body = document.body;

themeToggle.addEventListener('click', () => {
    const currentTheme = body.getAttribute('data-theme');
    if (currentTheme === 'dark') {
        body.removeAttribute('data-theme');
        themeToggle.textContent = '🌙';
        localStorage.setItem('theme', 'light');
    } else {
        body.setAttribute('data-theme', 'dark');
        themeToggle.textContent = '☀️';
        localStorage.setItem('theme', 'dark');
    }
});

// Load saved theme
const savedTheme = localStorage.getItem('theme');
if (savedTheme === 'dark') {
    body.setAttribute('data-theme', 'dark');
    themeToggle.textContent = '☀️';
} else {
    themeToggle.textContent = '🌙';
}

// 5. Moving Cursor Emoji
const cursorEmoji = document.createElement('div');
cursorEmoji.className = 'cursor-emoji';
cursorEmoji.textContent = '✨'; // Cute emoji
document.body.appendChild(cursorEmoji);

let mouseX = 0, mouseY = 0;
let emojiX = 0, emojiY = 0;

document.addEventListener('mousemove', (e) => {
    mouseX = e.clientX;
    mouseY = e.clientY;
});

function animateCursor() {
    emojiX += (mouseX - emojiX) * 0.1;
    emojiY += (mouseY - emojiY) * 0.1;
    cursorEmoji.style.left = emojiX + 'px';
    cursorEmoji.style.top = emojiY + 'px';
    requestAnimationFrame(animateCursor);
}
animateCursor();

// 6. Neon Effects
const nameElement = document.querySelector('.hero-text h1');
const profileImg = document.querySelector('.hero-img');

nameElement.classList.add('neon-text');
profileImg.classList.add('neon-img');

// 7. Scroll Reveal Animations
const observerOptions = { threshold: 0.15 };
const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
        }
    });
}, observerOptions);

const animatedElements = document.querySelectorAll('.skill-card, .project-card, .about-text, .about-img, .hero-text, .hero-img-box');

animatedElements.forEach(el => {
    el.style.opacity = '0';
    el.style.transform = 'translateY(40px)';
    el.style.transition = 'all 0.8s cubic-bezier(0.165, 0.84, 0.44, 1)';
    observer.observe(el);
});
