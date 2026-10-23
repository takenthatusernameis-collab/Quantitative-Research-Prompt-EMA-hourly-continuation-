# EMA Hourly Continuation — CGPT/USDT P12_50

**Symbol:** CGPT/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1003 |
| net_profit_factor | 0.5482 |
| net_win_rate | 0.4576 |
| gross_profit_factor | 0.9270 |
| gross_win_rate | 0.4726 |
| sharpe_ratio | -6.1182 |
| sortino_ratio | -2.7100 |
| max_drawdown | 0.9662 |
| cagr | -0.7357 |
| net_avg_win | 25.4946 |
| net_avg_loss | -39.2430 |
| avg_hold_time_bars | 7.6221 |
| exposure | 0.3475 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
