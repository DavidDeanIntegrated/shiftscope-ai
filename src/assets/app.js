(function () {
  var t = document.querySelector('.nav-toggle'), n = document.getElementById('nav');
  if (t && n) t.addEventListener('click', function () { var o = n.classList.toggle('open'); t.setAttribute('aria-expanded', o); });
  // Directory search + filter
  var q = document.getElementById('q'), grid = document.getElementById('grid');
  if (q && grid) {
    var cards = [].slice.call(grid.querySelectorAll('.card')), chips = [].slice.call(document.querySelectorAll('.chip'));
    var count = document.getElementById('count'), empty = document.getElementById('empty'), cat = 'all';
    var params = new URLSearchParams(location.search);
    if (params.get('q')) q.value = params.get('q');
    if (params.get('cat')) cat = params.get('cat');
    function apply() {
      var terms = q.value.toLowerCase().trim().split(/\s+/).filter(Boolean), shown = 0;
      cards.forEach(function (c) {
        var ok = (cat === 'all' || c.dataset.cat === cat) && terms.every(function (w) { return c.dataset.text.indexOf(w) > -1; });
        c.hidden = !ok; if (ok) shown++;
      });
      chips.forEach(function (ch) { var a = ch.dataset.filter === cat; ch.classList.toggle('active', a); ch.setAttribute('aria-pressed', a); });
      count.textContent = shown + (shown === 1 ? ' tool' : ' tools');
      empty.hidden = shown !== 0;
    }
    q.addEventListener('input', apply);
    chips.forEach(function (ch) { ch.addEventListener('click', function () { cat = ch.dataset.filter; apply(); }); });
    apply();
  }
  // Kit newsletter forms: progressive enhancement with fetch; falls back to a normal POST.
  [].slice.call(document.querySelectorAll('form[data-kit]')).forEach(function (f) {
    f.addEventListener('submit', function (e) {
      if (!window.fetch || !window.FormData) return; // native POST
      e.preventDefault();
      var m = f.querySelector('.form-msg'), b = f.querySelector('button[type=submit]');
      if (b) b.disabled = true;
      if (m) { m.classList.remove('err'); m.textContent = 'Subscribing…'; }
      fetch(f.action, { method: 'POST', body: new FormData(f), headers: { Accept: 'application/json' } })
        .then(function (r) { return r.json().catch(function () { return {}; }).then(function (j) { return { ok: r.ok, j: j }; }); })
        .then(function (res) {
          if (res.j.status === 'quarantined' && res.j.url) { window.location.href = res.j.url; return; } // Kit spam check (captcha)
          if (res.ok && (!res.j.status || res.j.status === 'success')) {
            if (m) m.textContent = 'Thanks! Check your inbox to confirm.';
            f.reset();
          } else {
            if (m) { m.classList.add('err'); m.textContent = (res.j.errors && res.j.errors.join ? res.j.errors.join(' ') : '') || 'Something went wrong. Please try again or use the Kit link below.'; }
          }
        })
        .catch(function () { f.submit(); }) // network/CORS issue: fall back to a normal POST
        .then(function () { if (b) b.disabled = false; });
    });
  });
  // Stub forms (submit a tool): never send anything
  [].slice.call(document.querySelectorAll('form[data-stub]')).forEach(function (f) {
    f.addEventListener('submit', function (e) {
      e.preventDefault();
      var m = f.querySelector('.form-msg');
      if (m) m.textContent = "Thanks! This form is a demo and isn't connected yet, so nothing was sent or stored.";
    });
  });
})();
