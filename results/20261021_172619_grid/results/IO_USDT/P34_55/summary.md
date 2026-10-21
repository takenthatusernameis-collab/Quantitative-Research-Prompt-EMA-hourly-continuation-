# EMA Hourly Continuation — IO/USDT P34_55

**Symbol:** IO/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 244 |
| net_profit_factor | 0.8257 |
| net_win_rate | 0.5123 |
| gross_profit_factor | 1.0436 |
| gross_win_rate | 0.5123 |
| sharpe_ratio | -0.9360 |
| sortino_ratio | -0.2170 |
| max_drawdown | 0.2387 |
| cagr | -0.0955 |
| net_avg_win | 79.8594 |
| net_avg_loss | -101.5973 |
| avg_hold_time_bars | 6.1721 |
| exposure | 0.0729 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
