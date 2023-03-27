// theme.js

const themeToggle = document.querySelector('#theme-toggle');
const themeStyle = document.querySelector('#theme-style');

themeToggle.addEventListener('click', () => {
    const isDark = document.documentElement.classList.toggle('dark');
    themeStyle.href = isDark ? '{% static "css/dark.css" %}' : '{% static "css/light.css" %}';
    localStorage.setItem('theme', isDark ? 'dark' : 'light');
});

const currentTheme = localStorage.getItem('theme');
if (currentTheme) {
    document.documentElement.classList.toggle('dark', currentTheme === 'dark');
    themeStyle.href = currentTheme === 'dark' ? '{% static "css/dark.css" %}' : '{% static "css/light.css" %}';
}
