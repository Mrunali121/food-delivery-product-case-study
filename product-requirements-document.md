# Product Requirements Document — Reorder & Live ETA Confidence

**Product:** QuickBite (food delivery app, Germany)
**Owner:** Product Manager
**Status:** Approved for build, Q2
**Related:** [Roadmap](product-roadmap.md) · [User Research](user-research.md) · [Prioritization](feature-prioritization.xlsx) · [User Stories](user-stories.md)

## 1. Problem
68% of first-time QuickBite customers never place a second order within 30 days,
and "Where is my order?" tickets make up 22% of all support volume. Both trace
back to the same root cause identified in [user research](user-research.md):
customers don't trust the app to get their next order right, so they don't come
back to find out.

## 2. Goals
| Goal | Metric | Target |
|---|---|---|
| Increase repeat ordering | 30-day repeat order rate | 32% → 45% |
| Reduce delivery-status support load | "Where is my order?" tickets as % of total | 22% → 12% |
| Reduce ETA-related complaints | ETA accuracy (actual vs. shown at checkout) | ±15 min → ±5 min |

## 3. Non-Goals (explicitly out of scope for this release)
- Checkout field reduction / guest checkout simplification (deferred to Q3 — see
  [Roadmap](product-roadmap.md) and [Prioritization](feature-prioritization.xlsx))
- Loyalty/rewards program
- In-app courier chat

## 4. Scope

### 4.1 One-Tap Reorder
- A "Reorder" entry point on the home screen surfacing the user's 3 most recent
  distinct orders.
- One tap reconstructs the full cart (items, modifiers, restaurant) and takes the
  user directly to checkout — not the restaurant menu.
- If any item is no longer available, the user sees a clear substitution prompt
  before reaching checkout, not a silent removal.

### 4.2 Live ETA Confidence
- Replace the static "20–30 min" range shown at checkout with a live,
  continuously-updating estimate driven by courier GPS and kitchen prep-time data.
- Push a proactive notification if the ETA shifts by more than 10 minutes from
  what was shown at order confirmation — before the customer has to ask.
- Order tracking screen shows current stage (Confirmed → Preparing → Picked up →
  Arriving) alongside the live ETA, not just a progress bar.

## 5. Functional Requirements
| ID | Requirement | Priority |
|---|---|---|
| FR-01 | Home screen surfaces the 3 most recent distinct orders as one-tap reorder cards | Must |
| FR-02 | Reorder reconstructs the full cart including modifiers and takes the user to checkout | Must |
| FR-03 | Unavailable items trigger a substitution prompt before checkout, never a silent drop | Must |
| FR-04 | Checkout ETA is computed live from courier GPS + current kitchen queue, refreshed every 60 seconds | Must |
| FR-05 | A push notification fires if live ETA drifts more than 10 minutes from the confirmed estimate | Must |
| FR-06 | Order tracking screen shows stage + live ETA together | Must |
| FR-07 | Reorder cards update to reflect the 3 most recent orders after each new order | Should |

## 6. Edge Cases
- Reordering when the restaurant is currently closed → show reorder card as
  disabled with next-open time, not hidden.
- Reordering when the restaurant has left the platform → card removed from the
  reorder list gracefully, no broken deep link.
- GPS signal loss mid-delivery → ETA falls back to kitchen-queue-based estimate
  with a "tracking temporarily unavailable" note, never a frozen stale number.

## 7. Success Metrics & Measurement
See [`analytics/analysis.sql`](analytics/analysis.sql) for the actual queries used
to track these post-launch:
- 30-day repeat order rate, before/after cohort comparison
- ETA accuracy distribution (shown vs. actual delivery time)
- "Where is my order?" ticket volume as a % of total support tickets

## 8. Rollout Plan
Phased: 10% of Berlin traffic (Week 1) → 50% of Berlin (Week 2) → 100% Berlin +
expand nationally (Week 4), gated on the ETA accuracy metric holding at or below
±7 minutes at each stage.
