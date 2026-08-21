# Product Roadmap — QuickBite

Quarterly roadmap, directly sequenced from the [RICE prioritization
scoring](feature-prioritization.xlsx). Each quarter's focus is a direct
consequence of what scored highest against the problems found in
[user research](user-research.md).

## Q1 — Discovery & Validation
- User research (interviews, survey, ticket tagging, funnel analysis)
- Competitor analysis
- RICE prioritization workshop with Engineering, Design, and Support leads
- PRD written and approved for the two top-scoring initiatives

**Output:** [User Research](user-research.md), [Personas](personas.md),
[Competitor Analysis](competitor-analysis.md), [Prioritization](feature-prioritization.xlsx)

## Q2 — Build: Reorder & Live ETA Confidence
- One-Tap Reorder (FR-01 to FR-03, FR-07)
- Live ETA Confidence (FR-04 to FR-06)
- Phased rollout: 10% → 50% → 100% Berlin, then national expansion

**Output:** [PRD](product-requirements-document.md), [User Stories](user-stories.md),
[Mockups](mockups/screens), shipped feature

**Success gate to proceed to Q3:** 30-day repeat order rate improves measurably
and ETA accuracy holds at ±7 minutes or better — tracked via
[`analytics/analysis.sql`](analytics/analysis.sql).

## Q3 — Checkout Simplification (deferred from this cycle)
- Guest checkout / reduced required fields at payment step
- Addresses the 34% payment-step drop-off found in research (Finding #3), which
  scored lower than reorder/ETA in Q1's RICE prioritization but remains a real,
  sized opportunity

## Q4 — Loyalty & Retention Layer
- Loyalty/rewards program (competitive gap identified in
  [Competitor Analysis](competitor-analysis.md))
- Builds on the trust foundation established by Live ETA Confidence — sequencing
  a rewards program before fixing delivery trust would have asked customers to
  stay loyal to an experience they didn't yet trust

## Explicitly not on this roadmap
- In-app courier chat — scored lowest in RICE prioritization, revisit if support
  ticket data shows a new driver after Q2/Q3 ship
- Group ordering / bill splitting — interesting but not connected to either
  problem this roadmap is solving; would need its own research cycle
