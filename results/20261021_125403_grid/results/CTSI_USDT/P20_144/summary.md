# EMA Hourly Continuation — CTSI/USDT P20_144

**Symbol:** CTSI/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 452 |
| net_profit_factor | 0.7396 |
| net_win_rate | 0.4646 |
| gross_profit_factor | 0.9128 |
| gross_win_rate | 0.4646 |
| sharpe_ratio | -2.3985 |
| sortino_ratio | -0.7239 |
| max_drawdown | 0.6158 |
| cagr | -0.2844 |
| net_avg_win | 76.8754 |
| net_avg_loss | -90.2012 |
| avg_hold_time_bars | 24.7942 |
| exposure | 0.5094 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
