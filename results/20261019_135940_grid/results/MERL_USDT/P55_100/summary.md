# EMA Hourly Continuation — MERL/USDT P55_100

**Symbol:** MERL/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 589 |
| net_profit_factor | 0.6084 |
| net_win_rate | 0.4771 |
| gross_profit_factor | 0.9060 |
| gross_win_rate | 0.4822 |
| sharpe_ratio | -3.5985 |
| sortino_ratio | -1.2405 |
| max_drawdown | 0.7825 |
| cagr | -0.4400 |
| net_avg_win | 42.3473 |
| net_avg_loss | -63.5012 |
| avg_hold_time_bars | 5.9660 |
| exposure | 0.1602 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
