# EMA Hourly Continuation — CELR/USDT P26_100

**Symbol:** CELR/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 633 |
| net_profit_factor | 0.5790 |
| net_win_rate | 0.4629 |
| gross_profit_factor | 0.8604 |
| gross_win_rate | 0.4692 |
| sharpe_ratio | -4.0911 |
| sortino_ratio | -1.4471 |
| max_drawdown | 0.8272 |
| cagr | -0.4983 |
| net_avg_win | 38.6961 |
| net_avg_loss | -57.5972 |
| avg_hold_time_bars | 13.5482 |
| exposure | 0.3881 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
