"""
Estimate ASML's equity beta from market data, rather than taking it off a website.

Beta is the slope of the regression of the stock's returns on the market's returns:

    r_asset  =  alpha  +  beta * r_market  +  error

It answers: when the market moves 1%, how much does this stock move on average?
Beta > 1 means more volatile than the market, which means shareholders demand a
higher return, which raises the WACC, which lowers the valuation. It is one of
three inputs to the cost of equity, so it is worth getting honestly.

Run:  pip install yfinance pandas numpy
      python estimate_beta.py
"""

import numpy as np
import pandas as pd
import yfinance as yf

TICKER = "ASML.AS"        # Amsterdam listing, priced in EUR.
YEARS = 5
INTERVAL = "1wk"          # weekly: ~260 points over 5y. Daily is noisy, monthly too sparse.

# Several indices on purpose. Which one you regress against changes the answer,
# and saying so is better analysis than quoting a single number.
INDICES = {
    "^AEX":      "AEX (Amsterdam) - WARNING: ASML is a huge weight in this index",
    "^STOXX50E": "EURO STOXX 50 - ASML is still a large weight",
    "^STOXX":    "STOXX Europe 600 - broadest EUR index, least contaminated",
    "^GSPC":     "S&P 500 - USD, so there is a currency mismatch. Cross-check only.",
}


def ols(y, x):
    """Least squares slope and intercept, with the standard error of the slope.

    Returns beta, alpha, se(beta), t-statistic, R-squared, n.
    Written out rather than imported so every step is visible and checkable.
    """
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    n = len(x)
    xbar, ybar = x.mean(), y.mean()
    sxx = ((x - xbar) ** 2).sum()
    sxy = ((x - xbar) * (y - ybar)).sum()

    beta = sxy / sxx
    alpha = ybar - beta * xbar

    resid = y - (alpha + beta * x)
    dof = n - 2
    s2 = (resid ** 2).sum() / dof            # residual variance
    se_beta = np.sqrt(s2 / sxx)
    t_stat = beta / se_beta if se_beta > 0 else float("inf")

    ss_tot = ((y - ybar) ** 2).sum()
    r2 = 1.0 - (resid ** 2).sum() / ss_tot

    return beta, alpha, se_beta, t_stat, r2, n


def self_test():
    """The regression must return exactly what we know the answer to be.

    Build a series with a beta of 1.60 by construction and check we recover it.
    If this fails, nothing below is worth reading.
    """
    rng = np.random.default_rng(0)
    mkt = rng.normal(0, 0.02, 5000)
    noise = rng.normal(0, 0.01, 5000)
    asset = 1.60 * mkt + noise

    beta, _, se, _, _, _ = ols(asset, mkt)
    assert abs(beta - 1.60) < 3 * se, f"self-test failed: got {beta:.3f}"

    # Regressing a series on itself must give exactly 1.
    beta_self, _, _, _, r2_self, _ = ols(mkt, mkt)
    assert abs(beta_self - 1.0) < 1e-10, "beta of the market on itself must be 1"
    assert abs(r2_self - 1.0) < 1e-10, "R-squared of a series on itself must be 1"

    print(f"self-test passed  (recovered beta {beta:.3f} from a true 1.600)\n")


def weekly_returns(tickers):
    """Download adjusted closes and convert to simple weekly returns."""
    raw = yf.download(
        tickers, period=f"{YEARS}y", interval=INTERVAL,
        auto_adjust=True, progress=False,
    )["Close"]
    if isinstance(raw, pd.Series):
        raw = raw.to_frame()
    return raw.pct_change().dropna(how="any")


def main():
    self_test()

    rets = weekly_returns([TICKER] + list(INDICES))
    if TICKER not in rets.columns:
        raise SystemExit(f"no data for {TICKER} - check the ticker and your connection")

    print(f"{TICKER}, {YEARS}y of {INTERVAL} returns, {len(rets)} observations\n")
    print(f"{'index':<12}{'beta':>8}{'se':>8}{'t':>8}{'R2':>8}{'adj beta':>10}   note")
    print("-" * 96)

    for idx, note in INDICES.items():
        if idx not in rets.columns:
            print(f"{idx:<12}{'no data':>8}")
            continue

        pair = rets[[TICKER, idx]].dropna()
        beta, alpha, se, t, r2, n = ols(pair[TICKER], pair[idx])

        # Blume adjustment. Betas drift toward 1 over time, so practitioners
        # (and Bloomberg's "adjusted beta") shrink the raw estimate:
        adj = (2.0 / 3.0) * beta + (1.0 / 3.0)

        print(f"{idx:<12}{beta:>8.3f}{se:>8.3f}{t:>8.1f}{r2:>8.2f}{adj:>10.3f}   {note}")

    print("\nWhich to use:")
    print("  - Prefer STOXX Europe 600: broad, in euros, and ASML is a small part of it.")
    print("  - Treat the AEX figure with suspicion. ASML is a large share of that index,")
    print("    so you are partly regressing the stock on itself, which drags beta toward 1.")
    print("  - Quote the adjusted beta if you use one, and say that you did.")
    print("  - Report the RANGE across indices in your note. The spread is a real")
    print("    uncertainty in your WACC, and it belongs in the sensitivity sweep.")


if __name__ == "__main__":
    main()