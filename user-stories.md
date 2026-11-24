# User Stories — Reorder & Live ETA Confidence

Derived directly from the [PRD](product-requirements-document.md) functional
requirements. Written for the Q2 build described in the
[Roadmap](product-roadmap.md).

---

### US-01 — One-tap reorder from home screen
**As** Busy Ben, **I want** to see my most recent orders on the home screen
**so that** I can reorder my usual lunch without searching for it again.

**Acceptance Criteria**
- Home screen shows up to 3 most recent *distinct* orders (not 3 most recent
  transactions, to avoid showing the same order 3 times if ordered repeatedly)
- Each card shows restaurant name, item summary, and last-ordered date
- Tapping a card goes directly to a pre-filled checkout, not the restaurant menu
- *(FR-01)*

---

### US-02 — Full cart reconstruction on reorder
**As** Family Fiona, **I want** my reorder to include all the modifiers I chose
last time **so that** I don't have to reconfigure each family member's order.

**Acceptance Criteria**
- All items, quantities, and modifiers from the original order are restored
  exactly
- If pricing has changed since the last order, the new price is shown clearly
  before checkout, not silently applied
- *(FR-02)*

---

### US-03 — Graceful handling of unavailable items
**As** Family Fiona, **I want** to be told if an item from my usual order isn't
available anymore **before** I reach checkout **so that** I'm not surprised by a
missing item after paying.

**Acceptance Criteria**
- If any item in a reordered cart is unavailable, a substitution prompt appears
  before checkout, offering the closest available alternative or removal
- The user cannot proceed to payment with an unresolved unavailable item
- *(FR-03)*

---

### US-04 — Live ETA at checkout
**As** Student Sara, **I want** the ETA I see at checkout to reflect real courier
and kitchen conditions **so that** I can trust it enough to actually plan around
it.

**Acceptance Criteria**
- ETA is computed from live courier GPS and current kitchen queue depth, not a
  static restaurant-level average
- ETA refreshes at least every 60 seconds while the order is active
- *(FR-04)*

---

### US-05 — Proactive delay notification
**As** Busy Ben, **I want** to be told if my order is running late **before** I
have to check the app myself **so that** I can adjust my plans without
guesswork.

**Acceptance Criteria**
- If live ETA drifts more than 10 minutes past the confirmed estimate, a push
  notification fires automatically
- Notification states the new estimated time, not just "your order is delayed"
- *(FR-05)*

---

### US-06 — Order tracking with stage and ETA together
**As** Student Sara, **I want** to see both the order stage and the live ETA on
one screen **so that** I understand not just *when* but *why* it's taking that
long.

**Acceptance Criteria**
- Tracking screen shows current stage (Confirmed → Preparing → Picked up →
  Arriving) alongside the live ETA
- If GPS signal is lost, the screen shows a "tracking temporarily unavailable"
  state rather than a frozen stale ETA
- *(FR-06)*
