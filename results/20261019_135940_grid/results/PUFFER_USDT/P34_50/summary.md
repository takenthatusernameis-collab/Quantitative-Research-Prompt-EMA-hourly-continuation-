# EMA Hourly Continuation — PUFFER/USDT P34_50

**Symbol:** PUFFER/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 662 |
| net_profit_factor | 0.5478 |
| net_win_rate | 0.4864 |
| gross_profit_factor | 1.0075 |
| gross_win_rate | 0.5015 |
| sharpe_ratio | -5.5717 |
| sortino_ratio | -2.2594 |
| max_drawdown | 0.8919 |
| cagr | -0.6669 |
| net_avg_win | 33.5238 |
| net_avg_loss | -57.9573 |
| avg_hold_time_bars | 3.3369 |
| exposure | 0.1250 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
