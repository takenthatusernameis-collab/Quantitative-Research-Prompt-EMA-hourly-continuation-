# EMA Hourly Continuation — GALA/USDT P26_89

**Symbol:** GALA/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 449 |
| net_profit_factor | 0.7366 |
| net_win_rate | 0.4833 |
| gross_profit_factor | 0.9113 |
| gross_win_rate | 0.4833 |
| sharpe_ratio | -1.8488 |
| sortino_ratio | -0.5592 |
| max_drawdown | 0.5044 |
| cagr | -0.2268 |
| net_avg_win | 61.3146 |
| net_avg_loss | -77.8570 |
| avg_hold_time_bars | 14.4232 |
| exposure | 0.2944 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
