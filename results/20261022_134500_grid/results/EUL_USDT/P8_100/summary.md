# EMA Hourly Continuation — EUL/USDT P8_100

**Symbol:** EUL/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 662 |
| net_profit_factor | 0.5781 |
| net_win_rate | 0.4622 |
| gross_profit_factor | 0.8079 |
| gross_win_rate | 0.4668 |
| sharpe_ratio | -3.7870 |
| sortino_ratio | -1.3641 |
| max_drawdown | 0.8106 |
| cagr | -0.4810 |
| net_avg_win | 36.1503 |
| net_avg_loss | -53.7518 |
| avg_hold_time_bars | 21.3399 |
| exposure | 0.6421 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
