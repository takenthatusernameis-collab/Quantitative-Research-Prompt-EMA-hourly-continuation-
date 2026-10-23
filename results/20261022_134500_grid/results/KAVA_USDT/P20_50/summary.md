# EMA Hourly Continuation — KAVA/USDT P20_50

**Symbol:** KAVA/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1053 |
| net_profit_factor | 0.5059 |
| net_win_rate | 0.4207 |
| gross_profit_factor | 0.9806 |
| gross_win_rate | 0.4530 |
| sharpe_ratio | -9.5266 |
| sortino_ratio | -4.3594 |
| max_drawdown | 0.9963 |
| cagr | -0.8914 |
| net_avg_win | 23.0203 |
| net_avg_loss | -33.0493 |
| avg_hold_time_bars | 5.4150 |
| exposure | 0.2592 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
