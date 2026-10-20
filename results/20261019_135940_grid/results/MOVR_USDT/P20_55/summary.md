# EMA Hourly Continuation — MOVR/USDT P20_55

**Symbol:** MOVR/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 977 |
| net_profit_factor | 0.4832 |
| net_win_rate | 0.4422 |
| gross_profit_factor | 0.8626 |
| gross_win_rate | 0.4575 |
| sharpe_ratio | -6.9956 |
| sortino_ratio | -3.0698 |
| max_drawdown | 0.9775 |
| cagr | -0.7777 |
| net_avg_win | 21.1470 |
| net_avg_loss | -34.6905 |
| avg_hold_time_bars | 5.4954 |
| exposure | 0.2440 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
