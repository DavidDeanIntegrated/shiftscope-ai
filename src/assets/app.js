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
  // Stub forms: never send anything
  [].slice.call(document.querySelectorAll('form[data-stub]')).forEach(function (f) {
    f.addEventListener('submit', function (e) {
      e.preventDefault();
      var m = f.querySelector('.form-msg');
      if (m) m.textContent = "Thanks! This form is a demo and isn't connected yet, so nothing was sent or stored.";
    });
  });
})();
