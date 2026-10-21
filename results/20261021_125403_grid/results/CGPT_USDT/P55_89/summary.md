# EMA Hourly Continuation — CGPT/USDT P55_89

**Symbol:** CGPT/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 315 |
| net_profit_factor | 0.6765 |
| net_win_rate | 0.4667 |
| gross_profit_factor | 0.8840 |
| gross_win_rate | 0.4667 |
| sharpe_ratio | -2.2646 |
| sortino_ratio | -0.5732 |
| max_drawdown | 0.4931 |
| cagr | -0.2318 |
| net_avg_win | 68.9066 |
| net_avg_loss | -89.1250 |
| avg_hold_time_bars | 6.6159 |
| exposure | 0.0947 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
