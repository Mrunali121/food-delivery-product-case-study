# User Research — QuickBite Reorder & Delivery Trust

## Objective
Understand why 68% of first-time customers never place a second order within 30
days, and why "Where is my order?" tickets make up 22% of support volume.

## Methodology
| Method | Sample | Purpose |
|---|---|---|
| 1:1 interviews | 15 customers (mix of one-time and repeat) | Depth on decision points and friction |
| Support ticket tagging | 600 tickets, 4-week sample | Quantify recurring complaint themes |
| In-app survey | 412 respondents | Validate interview themes at scale |
| Funnel analytics review | 90 days of checkout & order data | Locate where drop-off actually happens |

## Key Findings

### 1. The ETA shown at checkout doesn't match reality
Support ticket tagging showed **22% of all tickets** referenced order status or
delivery time. In interviews, customers consistently described the checkout ETA
as a promise, not an estimate — when the actual delivery ran 15+ minutes past it,
trust dropped sharply, even when the food still arrived warm and correct.

> "It said 25 minutes. I planned my lunch break around that. It showed up in 45.
> I don't think I even was that hungry anymore — I was just annoyed." — Interview P7

### 2. Reordering a favorite meal is more effort than it should be
11 of 15 interview participants described reordering the same meal from the same
restaurant as "searching from scratch again" — re-navigating the restaurant menu
and re-selecting the same modifiers each time. Survey data backed this up: 61% of
respondents said they'd order more often "if it were faster to get my usual."

### 3. Checkout has more required fields than repeat users expect
Funnel data showed a **34% drop-off at the payment step**, concentrated among
users who had never completed a purchase before. This is flagged as a real
finding but explicitly scoped to a later release — see
[Prioritization](feature-prioritization.xlsx) for why it wasn't picked for this
cycle despite the size of the drop-off.

### 4. Static tracking doesn't build confidence the way live tracking would
Survey respondents were asked to rate trust in delivery time estimates on a 1–5
scale: current static range averaged 2.6; when shown a mockup of live,
continuously-updating tracking, expected trust rating rose to 4.1.

## Synthesis
The one-and-done problem and the support ticket volume problem share a root
cause: customers don't trust QuickBite to get the *next* order right, so there's
no pull to come back and find out. This synthesis directly shaped the two
features selected for this cycle — see [Prioritization](feature-prioritization.xlsx)
and the resulting [PRD](product-requirements-document.md).

See [Personas](personas.md) for how these findings map onto the three user
segments interviewed.
