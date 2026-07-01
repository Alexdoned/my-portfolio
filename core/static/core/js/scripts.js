const themeToggle = document.getElementById('theme-toggle');
const themeLabel = document.getElementById('theme-label');
const htmlTag = document.documentElement;

function setTheme(theme) {
    htmlTag.setAttribute('data-theme', theme);
    localStorage.setItem('portfolio-theme', theme);
    themeToggle.innerHTML = theme === 'dark' ? '<i class="fas fa-sun"></i>' : '<i class="fas fa-moon"></i>';

    if (themeLabel) {
        themeLabel.textContent = theme === 'dark' ? 'Dark' : 'Light';
        if (theme === 'light') {
            themeLabel.classList.add('active');
            themeLabel.setAttribute('aria-pressed', 'true');
        } else {
            themeLabel.classList.remove('active');
            themeLabel.setAttribute('aria-pressed', 'false');
        }
    }
}

const savedTheme = localStorage.getItem('portfolio-theme') || 'light';
setTheme(savedTheme);

themeToggle.addEventListener('click', () => {
    const currentTheme = htmlTag.getAttribute('data-theme');
    const nextTheme = currentTheme === 'dark' ? 'light' : 'dark';
    setTheme(nextTheme);
});

document.addEventListener('DOMContentLoaded', () => {
    if (!localStorage.getItem('portfolio-theme')) {
        setTheme('light');
    }
});
