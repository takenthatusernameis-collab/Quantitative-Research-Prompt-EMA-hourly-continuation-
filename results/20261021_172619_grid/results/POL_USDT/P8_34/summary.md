# EMA Hourly Continuation — POL/USDT P8_34

**Symbol:** POL/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 683 |
| net_profit_factor | 0.6869 |
| net_win_rate | 0.4832 |
| gross_profit_factor | 0.9341 |
| gross_win_rate | 0.4832 |
| sharpe_ratio | -3.1084 |
| sortino_ratio | -1.1626 |
| max_drawdown | 0.7540 |
| cagr | -0.4124 |
| net_avg_win | 48.9778 |
| net_avg_loss | -66.6615 |
| avg_hold_time_bars | 8.8419 |
| exposure | 0.2745 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
