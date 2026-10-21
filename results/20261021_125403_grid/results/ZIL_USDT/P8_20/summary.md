# EMA Hourly Continuation — ZIL/USDT P8_20

**Symbol:** ZIL/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 573 |
| net_profit_factor | 0.7055 |
| net_win_rate | 0.5061 |
| gross_profit_factor | 1.0324 |
| gross_win_rate | 0.5061 |
| sharpe_ratio | -2.6974 |
| sortino_ratio | -0.9299 |
| max_drawdown | 0.6748 |
| cagr | -0.3452 |
| net_avg_win | 54.0804 |
| net_avg_loss | -78.5540 |
| avg_hold_time_bars | 5.4188 |
| exposure | 0.1411 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
