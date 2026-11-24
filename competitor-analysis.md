# Competitor Analysis — Food Delivery, DACH Market

Reviewed 3 comparable food delivery platforms operating in the German market
(anonymized as Competitor A/B/C below) against the two problem areas surfaced in
[user research](user-research.md): reorder friction and delivery-time trust.

## Feature Comparison

| Capability | QuickBite (current) | Competitor A | Competitor B | Competitor C |
|---|---|---|---|---|
| One-tap reorder of past orders | ❌ Not available | ✅ Available | ❌ Not available | ✅ Available (limited to 1 order) |
| Live, continuously-updating ETA | ❌ Static range only | ✅ Live tracking | ✅ Live tracking | ❌ Static range only |
| Proactive delay notifications | ❌ Not available | ✅ Available | ❌ Not available | ❌ Not available |
| Guest checkout (no account) | ❌ Account required | ✅ Available | ✅ Available | ❌ Account required |
| Loyalty / rewards program | ❌ Not available | ✅ Available | ✅ Available | ❌ Not available |
| Delivery fee shown before restaurant selection | ✅ Available | ❌ Shown at checkout only | ✅ Available | ✅ Available |

## Key Takeaways

1. **QuickBite is behind on both problem areas identified in research.** Two of
   the three competitors already offer live ETA tracking, and two offer one-tap
   reorder — these aren't speculative bets, they're closing a competitive gap
   that's also validated by our own user research.
2. **Guest checkout and loyalty are also gaps, but lower urgency right now.**
   Competitor A and B both have them, but our research (Finding #3) shows
   checkout drop-off is real yet not the dominant driver of the one-and-done
   problem the way reorder friction and ETA trust are — this is reflected in the
   [prioritization scoring](feature-prioritization.xlsx).
3. **No competitor combines live ETA with proactive delay notifications.**
   Competitor A has live tracking but doesn't proactively notify on delay — this
   is a specific opportunity to differentiate, not just match, and is captured
   as FR-05 in the [PRD](product-requirements-document.md).

## Scope note
This analysis intentionally excludes pricing/commission-structure comparison,
which is a separate workstream owned by the Business Development team and out of
scope for this product case study.
