# EMA Hourly Continuation — ORDI/USDT P89_100

**Symbol:** ORDI/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 649 |
| net_profit_factor | 0.3339 |
| net_win_rate | 0.4083 |
| gross_profit_factor | 0.7958 |
| gross_win_rate | 0.4361 |
| sharpe_ratio | -8.4833 |
| sortino_ratio | -3.0947 |
| max_drawdown | 0.9816 |
| cagr | -0.7950 |
| net_avg_win | 18.5641 |
| net_avg_loss | -38.3662 |
| avg_hold_time_bars | 1.9245 |
| exposure | 0.0568 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
