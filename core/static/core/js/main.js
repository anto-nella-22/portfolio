const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

const iconUse = (id) => `
    <svg viewBox="0 0 24 24" aria-hidden="true">
        <use href="#${id}"></use>
    </svg>
`;

// Navbar scroll effect
window.addEventListener('scroll', function () {
    const navbar = document.querySelector('.navbar');
    if (!navbar) {
        return;
    }
    if (window.scrollY > 50) {
        navbar.classList.add('scrolled');
    } else {
        navbar.classList.remove('scrolled');
    }
});

// Smooth scrolling for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: prefersReducedMotion ? 'auto' : 'smooth',
                block: 'start'
            });
        }
    });
});

// Theme initialization and toggle
const setTheme = (theme) => {
    document.body.classList.remove('light-theme', 'dark-theme');
    document.body.classList.add(`${theme}-theme`);
    localStorage.setItem('theme', theme);

    const themeToggle = document.getElementById('theme-toggle');
    const icon = document.getElementById('theme-switch-icon');
    const text = document.getElementById('theme-switch-text');
    if (themeToggle) {
        themeToggle.classList.toggle('is-dark', theme === 'dark');
        themeToggle.classList.toggle('is-light', theme === 'light');
        themeToggle.setAttribute('aria-checked', theme === 'light' ? 'true' : 'false');
    }
    if (icon && text) {
        icon.innerHTML = theme === 'dark' ? iconUse('icon-sun') : iconUse('icon-moon');
        text.textContent = theme === 'dark' ? 'Light mode' : 'Dark mode';

        if (!prefersReducedMotion) {
            icon.classList.add('theme-icon-animate');
            setTimeout(() => icon.classList.remove('theme-icon-animate'), 400);
        }
    }
};

const savedTheme = localStorage.getItem('theme') || 'dark';
setTheme(savedTheme);

const themeToggleBtn = document.getElementById('theme-toggle');
if (themeToggleBtn) {
    themeToggleBtn.addEventListener('click', function () {
        const nextTheme = document.body.classList.contains('dark-theme') ? 'light' : 'dark';
        setTheme(nextTheme);
    });
}

// Remove loading state after full page load
window.addEventListener('load', function () {
    document.body.classList.remove('loading');
});

// Intersection Observer for animations
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};

if (!prefersReducedMotion) {
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, observerOptions);

    // Observe elements for animation
    document.querySelectorAll('.card, .skill-card, .testimonial-card').forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(30px)';
        el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        observer.observe(el);
    });
}

// Toast notification
function showToast(message, type = 'success') {
    const toastMeta = {
        success: { icon: iconUse('icon-check'), label: 'Success' },
        error: { icon: iconUse('icon-error'), label: 'Error' },
        warning: { icon: iconUse('icon-warning'), label: 'Warning' },
        info: { icon: iconUse('icon-info'), label: 'Info' }
    };
    const normalizedType = toastMeta[type] ? type : 'info';
    const { icon, label } = toastMeta[normalizedType];
    const toast = document.createElement('div');
    toast.className = `custom-toast custom-toast-${normalizedType}`;
    toast.setAttribute('role', 'status');
    toast.setAttribute('aria-live', 'polite');
    toast.innerHTML = `
        <div class="toast-content">
            <span class="toast-icon" aria-hidden="true">${icon}</span>
            <div class="toast-copy">
                <span class="toast-label">${label}</span>
                <span class="toast-message">${message}</span>
            </div>
            <button class="toast-close" type="button" aria-label="Dismiss notification">${iconUse('icon-close')}</button>
        </div>
    `;
    toast.querySelector('.toast-close').addEventListener('click', () => {
        toast.remove();
    });
    document.body.appendChild(toast);

    // Auto remove after 5 seconds
    setTimeout(() => {
        if (toast.parentElement) {
            toast.remove();
        }
    }, 5000);
}
