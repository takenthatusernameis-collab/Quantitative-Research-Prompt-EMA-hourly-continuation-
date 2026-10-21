# EMA Hourly Continuation — PEPE/USDT P8_21

**Symbol:** PEPE/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 464 |
| net_profit_factor | 0.8290 |
| net_win_rate | 0.5216 |
| gross_profit_factor | 1.0740 |
| gross_win_rate | 0.5216 |
| sharpe_ratio | -1.2050 |
| sortino_ratio | -0.3741 |
| max_drawdown | 0.3924 |
| cagr | -0.1594 |
| net_avg_win | 70.7901 |
| net_avg_loss | -93.0862 |
| avg_hold_time_bars | 5.2306 |
| exposure | 0.1103 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
