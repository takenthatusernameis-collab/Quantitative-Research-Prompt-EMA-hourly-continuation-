# EMA Hourly Continuation — CELR/USDT P20_200

**Symbol:** CELR/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 309 |
| net_profit_factor | 0.6550 |
| net_win_rate | 0.4401 |
| gross_profit_factor | 0.7823 |
| gross_win_rate | 0.4401 |
| sharpe_ratio | -2.2944 |
| sortino_ratio | -0.5690 |
| max_drawdown | 0.4910 |
| cagr | -0.2309 |
| net_avg_win | 67.6217 |
| net_avg_loss | -81.1587 |
| avg_hold_time_bars | 48.2071 |
| exposure | 0.6741 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
