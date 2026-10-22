# EMA Hourly Continuation — ATOM/USDT P12_55

**Symbol:** ATOM/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 959 |
| net_profit_factor | 0.5005 |
| net_win_rate | 0.4599 |
| gross_profit_factor | 0.8887 |
| gross_win_rate | 0.4734 |
| sharpe_ratio | -6.2980 |
| sortino_ratio | -2.7500 |
| max_drawdown | 0.9654 |
| cagr | -0.7353 |
| net_avg_win | 21.9105 |
| net_avg_loss | -37.2728 |
| avg_hold_time_bars | 8.4442 |
| exposure | 0.3681 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
