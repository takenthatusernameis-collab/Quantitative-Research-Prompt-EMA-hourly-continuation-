# EMA Hourly Continuation — IO/USDT P20_50

**Symbol:** IO/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 938 |
| net_profit_factor | 0.5884 |
| net_win_rate | 0.4627 |
| gross_profit_factor | 0.8947 |
| gross_win_rate | 0.4701 |
| sharpe_ratio | -5.7551 |
| sortino_ratio | -2.5685 |
| max_drawdown | 0.9458 |
| cagr | -0.7078 |
| net_avg_win | 31.1256 |
| net_avg_loss | -45.5535 |
| avg_hold_time_bars | 4.7132 |
| exposure | 0.2140 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
