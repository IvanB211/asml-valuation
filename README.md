# What is the most advanced machine ever built actually worth?

ASML makes the only machines that can print the world's most advanced chips. The moat
is not a patent or a brand — it is physics, and nobody else has solved it. So I valued
the company, expecting the technology to be the thing that decided the answer.

It wasn't.

**Headline:** a five-year discounted cash flow and a comparables cross-check give a fair
value of **€521 per share** against a market price of **€1,379**. Across twenty-five
combinations of discount rate and terminal growth — every value a reasonable analyst
would defend — the highest figure produced is €801. None reaches the market price.

Solving the model backwards, today's price implies **8.09% growth in perpetuity**
against long-run nominal GDP near 4%. Reaching it on a conventional 2% terminal rate
instead requires roughly 40% revenue growth every year to 2030: ASML at about €169bn of
revenue, five times today's, selling to three customers.

The moat is physical. The valuation is not.

---

## The question

A discounted cash flow says a company is worth the cash it will hand its owners,
discounted for the fact that later cash is worth less. Everything else is machinery for
estimating those two things.

ASML is an unusually clean subject for it. The business has two parts — selling
lithography machines, and servicing the ones already installed — and both are disclosed
in detail. That means the forecast can be built from the ground up rather than
extrapolated, and it leaves time for the part that actually matters: working out which
assumption the answer rests on.

## What is assumed, and what is measured

The assumptions are the weak point of any valuation, so they are stated in full in
[`ASSUMPTIONS.md`](ASSUMPTIONS.md) — each one with its anchor, the argument for it, and
the argument against it. The short version:

| assumed | value | anchor |
|---|---|---|
| 2026 revenue | €44.0bn | management guidance of €43–45bn |
| revenue growth 2027–30 | 15 / 10 / 7 / 5% | judgement; capacity +30% planned for 2027 |
| gross margin | 55.0% | guided 54–56%; 52.8% actual in 2025 |
| capex | 6.0% of sales | between the 2025 trough of 4.8% and the 2023 peak of 7.8% |
| WACC | 10.76% | CAPM, with beta estimated rather than sourced |
| terminal growth | 2.0% | below long-run nominal GDP |

Everything historical comes from ASML's Annual Report 2025 (US GAAP) and the Q2 2026
quarterly statements, with page references in the workbook's `Sources` tab.

## Beta was estimated, not looked up

Cost of equity needs a beta, and the usual approach is to take one off a data provider.
[`estimate_beta.py`](estimate_beta.py) regresses five years of weekly ASML returns on
four different indices instead, with the least squares written out by hand and a
self-test that recovers a known beta of 1.60 before any real data is touched.

| index | beta | s.e. | R² | adjusted |
|---|---|---|---|---|
| AEX | 1.994 | 0.100 | 0.60 | 1.662 |
| EURO STOXX 50 | 1.562 | 0.106 | 0.45 | 1.375 |
| **STOXX Europe 600** | **1.675** | 0.139 | 0.36 | **1.450** |
| S&P 500 | 1.396 | 0.118 | 0.35 | 1.264 |

The AEX figure is contaminated and it is worth seeing why. ASML is a large constituent
of that index, so the regression is partly of the stock against itself. Writing the
index return as `w·r_ASML + (1−w)·r_rest`, ASML's own variance enters the covariance
with weight `w` but the index variance with weight `w²` — so at realistic weights the
measured beta is pushed **upward** for a stock more volatile than the rest of its index,
not toward 1 as the intuition suggests.

Using STOXX Europe 600 adjusted: **1.45**, with a credible range of 1.26–1.66 that moves
the cost of equity by two percentage points. That range is a live uncertainty, not a
footnote.

One admission: an R² of 0.36 means barely a third of ASML's weekly movement is explained
by the market. CAPM is used here because it is the convention, not because it describes
this stock well.

## Where the value actually sits

Discounted terminal value is **69% of enterprise value**. Two thirds of the answer is a
single number resting on a growth rate nobody can observe, and only one third is the
five years actually forecast. This is true of most discounted cash flows and is usually
left unsaid.

That is why the sensitivity grid and the reverse solve matter more than the point
estimate. A fair value of €521 is one draw from a distribution of assumptions; the
statement that *no defensible pair of assumptions reaches the market price* is the
finding.

## Running it

Open `ASML_DCF.xlsx`. Every input is a yellow cell on the `Assumptions` tab; change one
and the model recalculates. Nothing on the `DCF` tab is hardcoded.

```bash
pip install yfinance pandas numpy
python estimate_beta.py
```

| file | |
|---|---|
| `ASML_DCF.xlsx` | assumptions, DCF, sensitivity grid, comparables, sources |
| `ASSUMPTIONS.md` | every assumption with the argument for and against |
| `estimate_beta.py` | beta regression with self-test |

## Limitations

- **Q4 2026 guidance is adopted, not tested.** Management's full-year range implies a
  fourth quarter roughly 48% above last year's. That is their assumption; this model
  takes it, and a miss lowers every subsequent year.
- **Working capital is modelled crudely.** Contract liabilities — customer deposits paid
  before delivery — were €16.0bn at the end of 2025. Netting those off properly would
  likely raise free cash flow, so this treatment is conservative.
- **Comparable multiples are stale.** The peer set in the workbook needs refreshing, and
  Tokyo Electron and ASM International are missing from it.
- **Five years is a short explicit forecast** for a company with this long a product
  cycle. Ten would push less value into the terminal calculation.
- **A valuation is not a prediction.** It is a statement about what a set of assumptions
  implies. The point of the reverse solve is to make the market's assumptions explicit
  rather than to claim mine are better.

## What I would do next

1. **Replace the sensitivity grid with a proper sweep** — ten thousand random draws
   across every assumption, then a variance decomposition saying what fraction of the
   spread each input is responsible for.
2. **Model working capital properly**, netting contract liabilities against inventory
   and receivables.
3. **Extend the forecast to ten years**, so less of the answer sits in the terminal value.
4. **Build the revenue forecast from units and prices** rather than growth rates, using
   the disclosed capacity plan as the constraint.
