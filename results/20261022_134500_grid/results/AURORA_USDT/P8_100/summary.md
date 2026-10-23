# EMA Hourly Continuation — AURORA/USDT P8_100

**Symbol:** AURORA/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 609 |
| net_profit_factor | 0.6593 |
| net_win_rate | 0.4663 |
| gross_profit_factor | 0.9541 |
| gross_win_rate | 0.4762 |
| sharpe_ratio | -3.7927 |
| sortino_ratio | -1.3022 |
| max_drawdown | 0.8086 |
| cagr | -0.4706 |
| net_avg_win | 54.3345 |
| net_avg_loss | -72.0209 |
| avg_hold_time_bars | 23.1905 |
| exposure | 0.6420 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
