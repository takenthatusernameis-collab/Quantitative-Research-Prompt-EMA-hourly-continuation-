# EMA Hourly Continuation — GRAM/USDT P20_21

**Symbol:** GRAM/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1227 |
| net_profit_factor | 0.0741 |
| net_win_rate | 0.2478 |
| gross_profit_factor | 0.3559 |
| gross_win_rate | 0.3366 |
| sharpe_ratio | -20.6640 |
| sortino_ratio | -11.8001 |
| max_drawdown | 1.0000 |
| cagr | -0.9988 |
| net_avg_win | 2.6308 |
| net_avg_loss | -11.7007 |
| avg_hold_time_bars | 1.4963 |
| exposure | 0.0835 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
