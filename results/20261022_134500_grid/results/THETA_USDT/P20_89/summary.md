# EMA Hourly Continuation — THETA/USDT P20_89

**Symbol:** THETA/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 704 |
| net_profit_factor | 0.6201 |
| net_win_rate | 0.4773 |
| gross_profit_factor | 0.9502 |
| gross_win_rate | 0.4858 |
| sharpe_ratio | -4.1805 |
| sortino_ratio | -1.5542 |
| max_drawdown | 0.8641 |
| cagr | -0.5286 |
| net_avg_win | 41.2306 |
| net_avg_loss | -60.7084 |
| avg_hold_time_bars | 11.3736 |
| exposure | 0.3640 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
