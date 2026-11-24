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
    // Try the JSON file first; if the folder was not uploaded (or the page is opened from disk),
    // fall back to the same data embedded below so the section never stays empty.
    let data;
    try {
      const res = await fetch('data/measurement-metrics.json');
      if (!res.ok) throw new Error('metrics fetch failed');
      data = await res.json();
    } catch (e) {
      data = EMBEDDED_METRICS;
    }

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

// Copy of data/measurement-metrics.json (kept in sync by hand).
const EMBEDDED_METRICS = {
  "metrics": [
    {
      "id": "repeat_rate",
      "label": "30-Day Repeat Order Rate",
      "unit": "%",
      "before": 32,
      "after": 47,
      "target": 45,
      "goal": "increase"
    },
    {
      "id": "eta_accuracy",
      "label": "Avg. Absolute ETA Error",
      "unit": "min",
      "before": 14.2,
      "after": 4.6,
      "target": 5,
      "goal": "decrease"
    },
    {
      "id": "support_tickets",
      "label": "\"Where is my order?\" Tickets (% of total)",
      "unit": "%",
      "before": 22,
      "after": 11.2,
      "target": 12,
      "goal": "decrease"
    }
  ],
  "source": "analytics/analysis.sql (queries 4-7), see product-requirements-document.md Section 7"
};
