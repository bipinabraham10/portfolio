(function () {
  "use strict";

  var root = document.documentElement;

  // ---------------------------------------------------------------
  // Dark mode toggle (desktop rail button + mobile topbar button)
  // ---------------------------------------------------------------
  function setTheme(theme) {
    root.setAttribute("data-theme", theme);
    localStorage.setItem("theme", theme);
    var pressed = theme === "dark";
    document.querySelectorAll("#theme-toggle, #theme-toggle-mobile").forEach(function (btn) {
      btn.setAttribute("aria-pressed", String(pressed));
    });
  }

  function toggleTheme() {
    var current = root.getAttribute("data-theme") === "dark" ? "dark" : "light";
    setTheme(current === "dark" ? "light" : "dark");
  }

  document.querySelectorAll("#theme-toggle, #theme-toggle-mobile").forEach(function (btn) {
    btn.addEventListener("click", toggleTheme);
  });

  // keep in sync with OS-level changes if the user never made an explicit choice
  if (!localStorage.getItem("theme") && window.matchMedia) {
    window.matchMedia("(prefers-color-scheme: dark)").addEventListener("change", function (e) {
      setTheme(e.matches ? "dark" : "light");
    });
  }

  // ---------------------------------------------------------------
  // Scrollspy: highlight the rail link for the section in view
  // ---------------------------------------------------------------
  var links = Array.prototype.slice.call(document.querySelectorAll(".rail-link"));
  var sections = links
    .map(function (link) {
      return document.getElementById(link.dataset.section);
    })
    .filter(Boolean);

  function setActive(id) {
    links.forEach(function (link) {
      link.classList.toggle("is-active", link.dataset.section === id);
    });
  }

  if ("IntersectionObserver" in window && sections.length) {
    var observer = new IntersectionObserver(
      function (entries) {
        var visible = entries
          .filter(function (e) { return e.isIntersecting; })
          .sort(function (a, b) { return b.intersectionRatio - a.intersectionRatio; });
        if (visible.length) {
          setActive(visible[0].target.id);
        }
      },
      { rootMargin: "-35% 0px -50% 0px", threshold: [0, 0.25, 0.5, 0.75, 1] }
    );
    sections.forEach(function (section) { observer.observe(section); });
  }

  // ---------------------------------------------------------------
  // Scroll progress fill — rail track (desktop) + topbar bar (mobile)
  // ---------------------------------------------------------------
  var railProgress = document.getElementById("rail-progress");
  var mobileProgress = document.getElementById("mobile-progress");

  function updateProgress() {
    var scrollTop = window.scrollY || document.documentElement.scrollTop;
    var docHeight = document.documentElement.scrollHeight - window.innerHeight;
    var pct = docHeight > 0 ? Math.min(100, (scrollTop / docHeight) * 100) : 0;
    if (railProgress) railProgress.style.height = pct + "%";
    if (mobileProgress) mobileProgress.style.width = pct + "%";
  }

  var ticking = false;
  window.addEventListener("scroll", function () {
    if (!ticking) {
      window.requestAnimationFrame(function () {
        updateProgress();
        ticking = false;
      });
      ticking = true;
    }
  });
  updateProgress();

  // ---------------------------------------------------------------
  // Footer year
  // ---------------------------------------------------------------
  var yearEl = document.getElementById("year");
  if (yearEl) yearEl.textContent = new Date().getFullYear();
})();
