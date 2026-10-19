# EMA Hourly Continuation — BONK/USDT P34_100

**Symbol:** BONK/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 625 |
| net_profit_factor | 0.6702 |
| net_win_rate | 0.4880 |
| gross_profit_factor | 1.0042 |
| gross_win_rate | 0.5008 |
| sharpe_ratio | -3.2927 |
| sortino_ratio | -1.1480 |
| max_drawdown | 0.7714 |
| cagr | -0.4283 |
| net_avg_win | 50.2737 |
| net_avg_loss | -71.4930 |
| avg_hold_time_bars | 9.2864 |
| exposure | 0.2638 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
