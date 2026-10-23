# EMA Hourly Continuation — CGPT/USDT P26_50

**Symbol:** CGPT/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 877 |
| net_profit_factor | 0.4737 |
| net_win_rate | 0.4413 |
| gross_profit_factor | 0.8810 |
| gross_win_rate | 0.4550 |
| sharpe_ratio | -7.2612 |
| sortino_ratio | -3.0311 |
| max_drawdown | 0.9778 |
| cagr | -0.7780 |
| net_avg_win | 22.7283 |
| net_avg_loss | -37.8931 |
| avg_hold_time_bars | 3.8210 |
| exposure | 0.1523 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
