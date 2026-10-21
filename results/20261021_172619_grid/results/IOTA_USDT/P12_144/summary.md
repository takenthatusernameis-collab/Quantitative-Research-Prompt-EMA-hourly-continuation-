# EMA Hourly Continuation — IOTA/USDT P12_144

**Symbol:** IOTA/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 387 |
| net_profit_factor | 0.9986 |
| net_win_rate | 0.5478 |
| gross_profit_factor | 1.2041 |
| gross_win_rate | 0.5478 |
| sharpe_ratio | 0.0532 |
| sortino_ratio | 0.0152 |
| max_drawdown | 0.2279 |
| cagr | -0.0011 |
| net_avg_win | 91.2730 |
| net_avg_loss | -110.7270 |
| avg_hold_time_bars | 38.3669 |
| exposure | 0.6749 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
