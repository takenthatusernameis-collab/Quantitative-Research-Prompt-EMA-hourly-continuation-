# EMA Hourly Continuation — DIA/USDT P12_55

**Symbol:** DIA/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1005 |
| net_profit_factor | 0.5176 |
| net_win_rate | 0.4537 |
| gross_profit_factor | 0.8469 |
| gross_win_rate | 0.4667 |
| sharpe_ratio | -6.3490 |
| sortino_ratio | -2.8202 |
| max_drawdown | 0.9678 |
| cagr | -0.7430 |
| net_avg_win | 22.7677 |
| net_avg_loss | -36.5341 |
| avg_hold_time_bars | 8.1284 |
| exposure | 0.3697 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
