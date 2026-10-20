# EMA Hourly Continuation — PHA/USDT P8_20

**Symbol:** PHA/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1656 |
| net_profit_factor | 0.4589 |
| net_win_rate | 0.4589 |
| gross_profit_factor | 0.9365 |
| gross_win_rate | 0.4704 |
| sharpe_ratio | -9.4200 |
| sortino_ratio | -5.3721 |
| max_drawdown | 0.9988 |
| cagr | -0.9307 |
| net_avg_win | 11.1443 |
| net_avg_loss | -20.5997 |
| avg_hold_time_bars | 3.0713 |
| exposure | 0.2312 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
