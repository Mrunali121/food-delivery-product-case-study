// Scroll-reveal for sections
if (!window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
  const els = document.querySelectorAll('.reveal');
  const io = new IntersectionObserver((entries) => {
    entries.forEach(e => { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
  }, { threshold: 0.12 });
  els.forEach(el => io.observe(el));
} else {
  document.querySelectorAll('.reveal').forEach(el => el.classList.add('in'));
}

// Load measured metrics from data/measurement-metrics.json and render
// simple before/after bar comparisons — no charting library needed.
async function loadMetrics() {
  const container = document.getElementById('metrics-container');
  try {
    const res = await fetch('data/measurement-metrics.json');
    if (!res.ok) throw new Error('metrics fetch failed');
    const data = await res.json();

    container.innerHTML = '';
    data.metrics.forEach(m => {
      const maxVal = Math.max(m.before, m.after, m.target) * 1.15;
      const beforeH = Math.max(6, (m.before / maxVal) * 100);
      const afterH = Math.max(6, (m.after / maxVal) * 100);

      const card = document.createElement('div');
      card.className = 'metric-card';
      card.innerHTML = `
        <div class="metric-label">${m.label}</div>
        <div class="metric-bars">
          <div class="metric-bar-col">
            <div class="metric-val">${m.before}${m.unit}</div>
            <div class="metric-bar metric-bar-before" style="height:${beforeH}%"></div>
            <div class="metric-bar-tick">Before</div>
          </div>
          <div class="metric-bar-col">
            <div class="metric-val">${m.after}${m.unit}</div>
            <div class="metric-bar metric-bar-after" style="height:${afterH}%"></div>
            <div class="metric-bar-tick">After</div>
          </div>
        </div>
        <div class="metric-target">Target: ${m.goal === 'increase' ? '≥' : '≤'} ${m.target}${m.unit}</div>
      `;
      container.appendChild(card);
    });
  } catch (err) {
    container.innerHTML = '<p class="mono loading-text">Metrics data unavailable — see analytics/analysis.sql for the underlying queries.</p>';
  }
}

loadMetrics();
