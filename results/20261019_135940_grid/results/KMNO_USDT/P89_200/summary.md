# EMA Hourly Continuation — KMNO/USDT P89_200

**Symbol:** KMNO/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 360 |
| net_profit_factor | 0.6436 |
| net_win_rate | 0.4889 |
| gross_profit_factor | 0.9469 |
| gross_win_rate | 0.4917 |
| sharpe_ratio | -2.5809 |
| sortino_ratio | -0.6937 |
| max_drawdown | 0.5780 |
| cagr | -0.2831 |
| net_avg_win | 57.5365 |
| net_avg_loss | -85.5168 |
| avg_hold_time_bars | 12.9306 |
| exposure | 0.2149 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
