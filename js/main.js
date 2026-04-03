// === LOAD MORE ===
function loadMore() {
  const hidden = document.getElementById('hidden-posts');
  const btn = document.getElementById('load-more-btn');
  if (!hidden) return;
  hidden.style.removeProperty('display');
  hidden.style.display = 'grid';
  hidden.querySelectorAll('.blog-card').forEach((card, i) => {
    card.style.opacity = '0';
    card.style.transform = 'translateY(20px)';
    card.style.transition = 'all 0.5s cubic-bezier(0.16,1,0.3,1)';
    setTimeout(() => { card.style.opacity = '1'; card.style.transform = 'translateY(0)'; }, i * 100);
  });
  btn.style.display = 'none';
}


window.addEventListener('scroll', () => {
  const scrollTop = document.documentElement.scrollTop;
  const scrollHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight;
  const progress = (scrollTop / scrollHeight) * 100;
  document.getElementById('scroll-progress').style.setProperty('--scroll-width', progress + '%');
});

// === THEME TOGGLE ===
function toggleTheme() {
  const html = document.documentElement;
  const isDark = html.classList.contains('dark');
  html.classList.toggle('dark');
  localStorage.setItem('theme', isDark ? 'light' : 'dark');
  updateThemeIcon(!isDark);
}

function updateThemeIcon(isDark) {
  document.querySelector('.dark-icon').classList.toggle('hidden', !isDark);
  document.querySelector('.light-icon').classList.toggle('hidden', isDark);
}

(function () {
  const saved = localStorage.getItem('theme');
  if (saved === 'light') {
    document.documentElement.classList.remove('dark');
    updateThemeIcon(false);
  } else {
    updateThemeIcon(true);
  }
})();

// === SEARCH ===
function toggleSearch() {
  const overlay = document.getElementById('search-overlay');
  overlay.classList.toggle('active');
  if (overlay.classList.contains('active')) {
    setTimeout(() => document.getElementById('search-input').focus(), 100);
  }
}

document.addEventListener('keydown', (e) => {
  if ((e.metaKey || e.ctrlKey) && e.key === 'k') { e.preventDefault(); toggleSearch(); }
  if (e.key === 'Escape') {
    const overlay = document.getElementById('search-overlay');
    if (overlay && overlay.classList.contains('active')) toggleSearch();
  }
});

function filterSearch(query) {
  const q = query.toLowerCase();
  document.querySelectorAll('.search-result').forEach(r => {
    r.style.display = r.textContent.toLowerCase().includes(q) ? '' : 'none';
  });
}

// === MOBILE MENU ===
function toggleMobileMenu() {
  const menu = document.getElementById('mobile-menu');
  const overlay = document.getElementById('mobile-menu-overlay');
  if (!menu || !overlay) return;
  const isClosed = menu.classList.contains('translate-x-full');
  
  if (isClosed) {
    // Open menu
    menu.classList.remove('translate-x-full');
    overlay.classList.remove('opacity-0', 'pointer-events-none');
    overlay.classList.add('opacity-100', 'pointer-events-auto');
    document.body.style.overflow = 'hidden';
  } else {
    // Close menu
    menu.classList.add('translate-x-full');
    overlay.classList.remove('opacity-100', 'pointer-events-auto');
    overlay.classList.add('opacity-0', 'pointer-events-none');
    document.body.style.overflow = '';
  }
}

// === CATEGORY FILTER ===
function filterCategory(category, btn) {
  document.querySelectorAll('#category-filters button').forEach(b => b.classList.remove('cat-active'));
  btn.classList.add('cat-active');
  document.querySelectorAll('.blog-card').forEach(card => {
    if (category === 'all' || card.dataset.category === category) {
      card.style.display = '';
      card.style.opacity = '0';
      card.style.transform = 'translateY(10px)';
      setTimeout(() => {
        card.style.transition = 'all 0.3s ease';
        card.style.opacity = '1';
        card.style.transform = 'translateY(0)';
      }, 50);
    } else {
      card.style.display = 'none';
    }
  });
}

// === NEWSLETTER (EmailJS) ===
(function () {
  document.addEventListener('DOMContentLoaded', function () {
    var form = document.getElementById('newsletter-form');
    if (!form) return;
    var btn = document.getElementById('newsletter-btn');
    var originalText = btn.innerHTML;

    form.addEventListener('submit', function (e) {
      e.preventDefault();
      btn.innerHTML = 'Gonderiliyor...';
      btn.disabled = true;

      emailjs.sendForm('gucluyumhe', 'template_96kbyil', form)
        .then(function () {
          btn.innerHTML = 'Abone Olundu!';
          showToast('Bultene basariyla kaydoldun!');
          form.reset();
          setTimeout(function () { btn.innerHTML = originalText; btn.disabled = false; }, 3000);
        }, function (err) {
          btn.innerHTML = 'Hata!';
          showToast('Bir sorun cikti, tekrar dene.');
          console.error('EmailJS error:', err);
          setTimeout(function () { btn.innerHTML = originalText; btn.disabled = false; }, 3000);
        });
    });
  });
})();

// === CONTACT FORM (EmailJS) ===
(function () {
  document.addEventListener('DOMContentLoaded', function () {
    var form = document.getElementById('contact-form');
    if (!form) return;
    var btn = document.getElementById('contact-btn');
    var originalText = btn.innerHTML;

    form.addEventListener('submit', function (e) {
      e.preventDefault();
      btn.innerHTML = 'Gonderiliyor...';
      btn.disabled = true;

      emailjs.sendForm('gucluyumhe', 'template_96kbyil', form)
        .then(function () {
          btn.innerHTML = 'Gonderildi!';
          showToast('Mesajin basariyla gonderildi!');
          form.reset();
          setTimeout(function () { btn.innerHTML = originalText; btn.disabled = false; }, 3000);
        }, function (err) {
          btn.innerHTML = 'Hata!';
          showToast('Bir sorun cikti, tekrar dene.');
          console.error('EmailJS error:', err);
          setTimeout(function () { btn.innerHTML = originalText; btn.disabled = false; }, 3000);
        });
    });
  });
})();

// === COPY CODE ===
function copyCode() {
  navigator.clipboard.writeText(document.getElementById('code-block').innerText)
    .then(() => showToast('Kod panoya kopyalandı!'));
}

// === TOAST ===
function showToast(message) {
  const toast = document.getElementById('toast');
  document.getElementById('toast-message').textContent = message;
  toast.classList.add('show');
  setTimeout(() => toast.classList.remove('show'), 3000);
}

// === LIVE CLOCK & MINI CALENDAR ===
function initClock() {
  const clockEl = document.getElementById('live-clock');
  const secEl = document.getElementById('live-seconds');
  const dateEl = document.getElementById('live-date');
  if (!clockEl) return;

  const gunler = ['Pazar','Pazartesi','Sali','Carsamba','Persembe','Cuma','Cumartesi'];
  const aylar = ['Ocak','Subat','Mart','Nisan','Mayis','Haziran','Temmuz','Agustos','Eylul','Ekim','Kasim','Aralik'];

  function tick() {
    const now = new Date();
    const h = String(now.getHours()).padStart(2,'0');
    const m = String(now.getMinutes()).padStart(2,'0');
    const s = String(now.getSeconds()).padStart(2,'0');
    clockEl.textContent = h + ':' + m;
    secEl.textContent = ':' + s;
    dateEl.textContent = gunler[now.getDay()] + ', ' + now.getDate() + ' ' + aylar[now.getMonth()] + ' ' + now.getFullYear();
  }
  tick();
  setInterval(tick, 1000);
}

function initCalendar() {
  const cal = document.getElementById('mini-calendar');
  if (!cal) return;

  const now = new Date();
  const year = now.getFullYear();
  const month = now.getMonth();
  const today = now.getDate();
  const firstDay = new Date(year, month, 1).getDay();
  const daysInMonth = new Date(year, month + 1, 0).getDate();

  const labels = ['Pz','Sa','Ca','Pe','Cu','Ct','Pa'];
  labels.forEach(l => {
    const el = document.createElement('div');
    el.className = 'text-center text-[0.6rem] font-medium dark:text-neutral-600 text-neutral-400 py-1';
    el.textContent = l;
    cal.appendChild(el);
  });

  // pazartesi=0 olacak sekilde ayarla
  const offset = (firstDay === 0) ? 6 : firstDay - 1;
  for (let i = 0; i < offset; i++) {
    const el = document.createElement('div');
    cal.appendChild(el);
  }

  for (let d = 1; d <= daysInMonth; d++) {
    const el = document.createElement('div');
    el.className = 'text-center text-[0.65rem] py-1 rounded-md transition-colors ';
    if (d === today) {
      el.className += 'dark:bg-neutral-800 bg-neutral-200 dark:text-white text-neutral-900 font-semibold';
    } else {
      el.className += 'dark:text-neutral-500 text-neutral-400';
    }
    el.textContent = d;
    cal.appendChild(el);
  }
}

// === INTERSECTION OBSERVER ===
document.addEventListener('DOMContentLoaded', () => {
  initClock();
  initCalendar();

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.style.opacity = '1';
        entry.target.style.transform = 'translateY(0)';
      }
    });
  }, { threshold: 0.1 });

  document.querySelectorAll('.blog-card').forEach(card => {
    card.style.opacity = '0';
    card.style.transform = 'translateY(20px)';
    card.style.transition = 'all 0.6s cubic-bezier(0.16, 1, 0.3, 1)';
    observer.observe(card);
  });
});
