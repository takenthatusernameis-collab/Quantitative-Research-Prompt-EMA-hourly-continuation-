# EMA Hourly Continuation — PEPE/USDT P26_89

**Symbol:** PEPE/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 399 |
| net_profit_factor | 0.8248 |
| net_win_rate | 0.5013 |
| gross_profit_factor | 1.0098 |
| gross_win_rate | 0.5013 |
| sharpe_ratio | -1.2692 |
| sortino_ratio | -0.3632 |
| max_drawdown | 0.3995 |
| cagr | -0.1549 |
| net_avg_win | 81.1388 |
| net_avg_loss | -98.8686 |
| avg_hold_time_bars | 15.5363 |
| exposure | 0.2818 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
