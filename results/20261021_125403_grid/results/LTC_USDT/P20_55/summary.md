# EMA Hourly Continuation — LTC/USDT P20_55

**Symbol:** LTC/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 469 |
| net_profit_factor | 0.6833 |
| net_win_rate | 0.5075 |
| gross_profit_factor | 1.0093 |
| gross_win_rate | 0.5075 |
| sharpe_ratio | -2.4609 |
| sortino_ratio | -0.7674 |
| max_drawdown | 0.6104 |
| cagr | -0.2947 |
| net_avg_win | 52.9337 |
| net_avg_loss | -79.8151 |
| avg_hold_time_bars | 7.7591 |
| exposure | 0.1654 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
