# EMA Hourly Continuation — PHA/USDT P8_34

**Symbol:** PHA/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1373 |
| net_profit_factor | 0.5441 |
| net_win_rate | 0.4683 |
| gross_profit_factor | 0.9236 |
| gross_win_rate | 0.4778 |
| sharpe_ratio | -6.6686 |
| sortino_ratio | -3.4651 |
| max_drawdown | 0.9857 |
| cagr | -0.8131 |
| net_avg_win | 18.2830 |
| net_avg_loss | -29.5997 |
| avg_hold_time_bars | 5.5412 |
| exposure | 0.3458 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
