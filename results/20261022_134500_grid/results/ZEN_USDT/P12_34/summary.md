# EMA Hourly Continuation — ZEN/USDT P12_34

**Symbol:** ZEN/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1348 |
| net_profit_factor | 0.4513 |
| net_win_rate | 0.4444 |
| gross_profit_factor | 0.8588 |
| gross_win_rate | 0.4585 |
| sharpe_ratio | -8.8792 |
| sortino_ratio | -4.5873 |
| max_drawdown | 0.9965 |
| cagr | -0.8950 |
| net_avg_win | 13.6818 |
| net_avg_loss | -24.2465 |
| avg_hold_time_bars | 3.9926 |
| exposure | 0.2446 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
