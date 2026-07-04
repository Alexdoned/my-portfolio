
const themeToggle = document.getElementById('theme-toggle');
const themeLabel = document.getElementById('theme-label');
const htmlTag = document.documentElement;

/**
 * Handles layout engine property transformations and state saving processes
 * @param {string} theme - Set theme state value to either 'light' or 'dark'
 */
function setTheme(theme) {
    htmlTag.setAttribute('data-theme', theme);
    localStorage.setItem('portfolio-theme', theme);

    
    const toggleIcon = themeToggle ? themeToggle.querySelector('i') : null;
    if (toggleIcon) {
        if (theme === 'dark') {
            toggleIcon.className = 'fas fa-sun';
        } else {
            toggleIcon.className = 'fas fa-moon';
        }
    }

    
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


if (themeToggle) {
    themeToggle.addEventListener('click', () => {
        const currentTheme = htmlTag.getAttribute('data-theme');
        const nextTheme = currentTheme === 'dark' ? 'light' : 'dark';
        setTheme(nextTheme);
    });
}


document.addEventListener('DOMContentLoaded', () => {
    if (!localStorage.getItem('portfolio-theme')) {
        setTheme('light');
    }
});
