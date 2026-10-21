# EMA Hourly Continuation — CELR/USDT P12_144

**Symbol:** CELR/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 418 |
| net_profit_factor | 0.7334 |
| net_win_rate | 0.4665 |
| gross_profit_factor | 0.8823 |
| gross_win_rate | 0.4665 |
| sharpe_ratio | -2.0814 |
| sortino_ratio | -0.6033 |
| max_drawdown | 0.5396 |
| cagr | -0.2432 |
| net_avg_win | 71.2189 |
| net_avg_loss | -84.9167 |
| avg_hold_time_bars | 34.7105 |
| exposure | 0.6565 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
