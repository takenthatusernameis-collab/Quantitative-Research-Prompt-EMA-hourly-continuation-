# EMA Hourly Continuation — ALGO/USDT P50_144

**Symbol:** ALGO/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 479 |
| net_profit_factor | 0.5995 |
| net_win_rate | 0.4823 |
| gross_profit_factor | 0.9444 |
| gross_win_rate | 0.4906 |
| sharpe_ratio | -3.3373 |
| sortino_ratio | -1.0260 |
| max_drawdown | 0.7245 |
| cagr | -0.3892 |
| net_avg_win | 46.0204 |
| net_avg_loss | -71.4989 |
| avg_hold_time_bars | 11.8142 |
| exposure | 0.2572 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
