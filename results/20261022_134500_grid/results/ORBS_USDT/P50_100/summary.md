# EMA Hourly Continuation — ORBS/USDT P50_100

**Symbol:** ORBS/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 684 |
| net_profit_factor | 0.4788 |
| net_win_rate | 0.4094 |
| gross_profit_factor | 0.9302 |
| gross_win_rate | 0.4284 |
| sharpe_ratio | -7.7357 |
| sortino_ratio | -2.8691 |
| max_drawdown | 0.9730 |
| cagr | -0.7602 |
| net_avg_win | 31.9027 |
| net_avg_loss | -46.1774 |
| avg_hold_time_bars | 6.5950 |
| exposure | 0.2050 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
