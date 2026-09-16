# ASML valuation — every assumption, and why

A discounted cash flow forecasts the future. The future is not in the annual report,
so every forward-looking number below is a judgement. This file states each one, what
it is anchored to, the argument for it, and the argument against it.

All figures in € millions unless stated. Historical figures are from ASML's Annual
Report 2025 (US GAAP), with page numbers given. Market data is as at 15 September 2026.

---

## 1. Revenue

### 2026 total net sales: €44,000m

**Anchor.** Management guided to €43–45bn in the Q2 2026 results release (15 July 2026).
This is the midpoint.

**Why take guidance rather than forecast it.** Two and a half quarters of the year are
already known: H1 2026 actuals were €18,093m, and Q3 was guided at €11.0–12.0bn. Only
Q4 is genuinely a forecast, and management has better information about it than I do.

**The problem hiding in it.** Work the arithmetic backwards. €44,000m less H1 of
€18,093m less a Q3 midpoint of €11,500m leaves an implied Q4 of about **€14,400m**.
Q4 2025 was €9,718m. Guidance therefore requires a fourth quarter roughly **48% above
the same quarter last year**. That is the single most demanding assumption in ASML's
own outlook, and it is not mine — it is theirs. I have adopted it, and the sensitivity
analysis is where I test what happens if it does not land.

### Revenue growth 2027–2030: 15%, 10%, 7%, 5%

**The shape of the judgement.** This is not one assumption but a view about where in a
cycle the company sits. The history is unambiguous that a cycle exists:

| Year | Total net sales | Growth |
|---|---|---|
| 2023 | €27,558.5m | — |
| 2024 | €28,262.9m | +2.6% |
| 2025 | €32,667.3m | +15.6% |
| 2026E | €44,000m | +34.7% (guided) |

A business that grew 2.6% two years ago and is guiding to 35% today cannot be forecast
by extending the most recent year.

**The case for faster growth.** Management is adding 30% to low-NA EUV capacity for
2027 — from around 65 units in 2026 to roughly 85 — and investigating a further 30%
for 2028; DUV immersion capacity rises on a similar path. Firms do not fund capacity
they expect to idle. Demand from AI datacentre buildout looks structural rather than
cyclical. And ASML is running well ahead of its own long-term plan: the €44bn guided
for 2026 is close to the 2030 revenue the company modelled at its 2022 investor day,
reached four years early.

**The case for slower growth.** 2024 demonstrates that this business can go flat. The
customer base is effectively three companies, so one pausing its capital programme
removes a large share of revenue at once. If the guided Q4 reflects customers pulling
orders forward, 2027 begins from an inflated base. Export controls remain a live
constraint on addressable demand. And after a year of roughly 35% growth, some
reversion is the base rate rather than a pessimistic view.

**Why this path.** 15% in 2027 accepts that expanded capacity gets used but not that
it is filled instantly; growth then decays toward the terminal rate rather than
stopping abruptly, which is how capital-equipment cycles usually resolve. It is
deliberately between the two cases above rather than an endorsement of either.

**What it is worth testing.** A path containing an outright down year — 12%, then −5%,
then recovery — is arguably more honest about this industry, and moves fair value from
€521 to €433. The conclusion does not change, which is itself informative.

---

## 2. Costs

### Gross margin: 55.0%

**Anchor.** Guided at 54–56% for 2026; 52.8% actual in 2025, up from 51.3% in both
2024 and 2023. Q2 2026 came in at 54.0%.

**Argument.** Margin is rising, and the mechanism is visible in the units. ASML sold
327 lithography systems in 2025 against 418 in 2024, yet system revenue rose 12.4% —
fewer machines at much higher prices, as EUV displaces DUV in the mix. That mix shift
continues in 2026: H1 units rose 11% while revenue rose 17%. Holding 55% assumes the
trend persists but does not extend it further, which guidance does not support.

### R&D and SG&A: grown at 8% a year from 2025 actuals

**Why not a percentage of sales.** R&D is committed multi-year spending on machine
development. It does not fall when revenue falls, and it does not automatically scale
when revenue rises. Modelling it as a fixed percentage of sales would wrongly imply
both.

**Why this matters.** Treating these as absolute costs creates operating leverage:
EBIT margin then rises and falls faster than revenue, which is exactly what the history
shows. EBIT margin fell to 31.9% in 2024 when revenue grew 2.6%, then rose to 34.6% in
2025 when revenue grew 15.6%. A model that assumed constant cost ratios would have
missed this entirely.

**The consistency trap.** Because of this, the margin assumption is not independent of
the growth assumption. Forecasting slow revenue growth alongside expanding margins is
internally inconsistent, and it is the first thing a reader should check.

### Effective tax rate: 17.5%

17.7% in 2025, 18.6% in 2024, 15.8% in 2023; recent quarters near 17.5%. Stable enough
that a three-year anchor is defensible without further argument.

---

## 3. Cash

### Capex: 6.0% of sales

**Anchor.** 7.8% in 2023, 7.3% in 2024, **4.8% in 2025** — a sharp fall.

**Argument.** The fall reflects the completion of a capacity build, not a permanent
reduction in capital intensity. Management has now stated it is adding 30% to EUV and
DUV immersion capacity for 2027. Capacity expansion requires capital, so assuming the
2025 trough persists would be assuming the expansion is free. 6.0% sits between the
recent trough and the prior peak.

**Honest caveat.** This is the assumption I am least confident in, and it matters:
capex is subtracted directly from free cash flow, so an error here flows straight to
the answer.

### D&A: 3.0% of sales

Three-year average (2.7%, 3.3%, 3.1%). Stable; no argument required.

### Working capital: 10% of the revenue increase

**Argument.** Growth consumes cash through inventory and receivables. ASML's inventory
is unusually large because machines take a long time to build.

**Why this is probably too conservative.** Contract liabilities — customer deposits
paid before delivery — stood at €16.0bn at the end of 2025, up from €12.6bn. Customers
are partly financing ASML's working capital. A more careful treatment would net this
off and might show working capital as a source of cash rather than a use. This is
flagged as a simplification rather than defended as correct.

---

## 4. Discount rate

### WACC: 10.76%

**Cost of equity, via CAPM:** risk-free rate + beta × equity risk premium
= 3.58% + 1.45 × 5.0% = **10.83%**

- **Risk-free rate 3.58%** — German 10-year Bund, 15 September 2026. A euro-denominated
  forecast requires a euro risk-free rate.
- **Equity risk premium 5.0%** — within the conventional 4.5–5.5% range for developed
  markets. Should be replaced with Damodaran's current implied premium and cited.
- **Beta 1.45** — estimated rather than sourced: an ordinary least squares regression of
  five years of weekly ASML returns on the STOXX Europe 600, Blume-adjusted
  (⅔ × raw + ⅓). Raw beta was 1.675, standard error 0.139.

**Why STOXX Europe 600 and not the AEX.** The AEX regression gives 1.994, materially
higher. ASML is a very large constituent of the AEX, so that regression is partly of
the stock against itself. Writing the index return as a weighted sum shows why:
ASML's own variance enters the covariance with weight *w* but the index variance with
weight *w²*, so at realistic weights the measured beta is pushed **upward** for a stock
more volatile than the rest of its index. The STOXX Europe 600 is broad, euro-denominated
and only marginally exposed to this problem.

**Beta range.** Adjusted estimates span 1.26 (S&P 500) to 1.66 (AEX), which moves the
cost of equity from roughly 9.8% to 11.8%. This is a live uncertainty and belongs in
the sensitivity analysis, not in a footnote.

**An admission about CAPM.** The regression R² against STOXX Europe 600 is 0.36. Only
about a third of ASML's weekly movement is explained by the market at all; the rest is
the semiconductor capital cycle. CAPM is being used because it is the convention, not
because it describes this stock well.

**Debt.** Total debt of €4,390.9m against a market capitalisation of roughly €529.6bn
is under 1% of capital, so WACC is materially the cost of equity. A pre-tax cost of
debt of 3.0% is assumed; interest paid in 2025 was €114.5m.

---

## 5. Terminal value

### Terminal growth: 2.0%

**Argument.** A terminal growth rate is a claim about growth in perpetuity. Anything
above long-run nominal GDP implies the company eventually becomes the entire economy.
2.0% is below developed-market nominal GDP of roughly 4% and reflects a business whose
addressable market is three customers.

**Why this single cell dominates.** The discounted terminal value is **69% of enterprise
value**. The valuation is therefore mostly a statement about a growth rate nobody can
observe, and only a minority a statement about the five years actually forecast.

---

## 6. The result, and what it means

| | |
|---|---|
| Enterprise value | €191.7bn |
| Add: net cash | €8.9bn |
| Equity value | €200.7bn |
| Value per share | **€521** |
| Market price (15 Sep 2026) | €1,379 |

**The sensitivity grid does not rescue it.** Across discount rates from 8.5% to 12.5%
and terminal growth from 1% to 3% — twenty-five combinations spanning every value a
reasonable analyst would defend — the highest fair value produced is €801. No pair
reaches the market price.

**So the model was run backwards.** Holding the forecast fixed and solving for the
terminal growth rate that would justify €1,379 gives **8.09% in perpetuity**, against
long-run nominal GDP near 4%. Alternatively, reaching today's price on a 2% terminal
rate requires roughly 40% revenue growth every year to 2030 — ASML at about €169bn of
revenue, five times today's, selling to three customers.

**The conclusion, stated carefully.** The correct reading is not "ASML is 62%
overvalued". It is that today's price cannot be reconstructed from a discounted cash
flow using any conventional set of assumptions, and therefore embeds expectations that
should be examined directly. Either the market is pricing a growth path far beyond
what the history and guidance support, or it is not valuing ASML on discounted cash
flows at all.

**And the point about the physics.** Understanding EUV lithography — tin-droplet plasma
sources, picometre-tolerance reflective optics, the reason no competitor exists —
explains completely why ASML earns extraordinary margins and why nobody can take them.
It says almost nothing about what the company is worth, because the valuation turns on
a terminal growth rate and three customers' capital budgets. The moat is physical. The
valuation is not.

---

## What would change my mind

- **Capacity sold out through 2028.** If the 30% expansion for 2027 and a further 30%
  for 2028 are contracted rather than speculative, the growth path here is too low.
- **High-NA pricing above expectation.** Machine prices are the mix story; materially
  higher average selling prices would lift both revenue and margin.
- **Working capital treated properly.** Netting off €16bn of customer prepayments could
  raise free cash flow meaningfully.
- **A lower cost of equity.** If beta nearer 1.26 is the better estimate, WACC falls
  about one point and terminal value rises materially.

## Known weaknesses

- Guidance for Q4 2026 is adopted, not tested. A miss there lowers every subsequent year.
- Working capital is modelled crudely, and probably conservatively.
- Comparable company multiples were not refreshed at the time of writing.
- A five-year explicit forecast is short for a company with this long a product cycle;
  ten years would push less value into the terminal calculation.
