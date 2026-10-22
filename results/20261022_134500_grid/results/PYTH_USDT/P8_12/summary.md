# EMA Hourly Continuation — PYTH/USDT P8_12

**Symbol:** PYTH/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1752 |
| net_profit_factor | 0.2714 |
| net_win_rate | 0.4150 |
| gross_profit_factor | 0.7708 |
| gross_win_rate | 0.4458 |
| sharpe_ratio | -15.0579 |
| sortino_ratio | -8.9832 |
| max_drawdown | 1.0000 |
| cagr | -0.9915 |
| net_avg_win | 5.1247 |
| net_avg_loss | -13.3908 |
| avg_hold_time_bars | 1.7928 |
| exposure | 0.1428 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
