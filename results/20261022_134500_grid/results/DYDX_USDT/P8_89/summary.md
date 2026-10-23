# EMA Hourly Continuation — DYDX/USDT P8_89

**Symbol:** DYDX/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 602 |
| net_profit_factor | 0.6942 |
| net_win_rate | 0.4950 |
| gross_profit_factor | 0.9969 |
| gross_win_rate | 0.4967 |
| sharpe_ratio | -3.0323 |
| sortino_ratio | -1.0540 |
| max_drawdown | 0.7310 |
| cagr | -0.3910 |
| net_avg_win | 54.2621 |
| net_avg_loss | -76.6168 |
| avg_hold_time_bars | 24.9236 |
| exposure | 0.6820 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
