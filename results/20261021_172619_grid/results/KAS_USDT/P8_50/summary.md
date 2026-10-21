# EMA Hourly Continuation — KAS/USDT P8_50

**Symbol:** KAS/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 690 |
| net_profit_factor | 0.8826 |
| net_win_rate | 0.5319 |
| gross_profit_factor | 1.1188 |
| gross_win_rate | 0.5319 |
| sharpe_ratio | -0.9305 |
| sortino_ratio | -0.3529 |
| max_drawdown | 0.3907 |
| cagr | -0.1549 |
| net_avg_win | 70.6142 |
| net_avg_loss | -90.9078 |
| avg_hold_time_bars | 13.1290 |
| exposure | 0.4118 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
