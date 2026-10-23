# EMA Hourly Continuation — CGPT/USDT P8_50

**Symbol:** CGPT/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1062 |
| net_profit_factor | 0.5882 |
| net_win_rate | 0.4708 |
| gross_profit_factor | 0.9290 |
| gross_win_rate | 0.4821 |
| sharpe_ratio | -5.5701 |
| sortino_ratio | -2.5513 |
| max_drawdown | 0.9569 |
| cagr | -0.7095 |
| net_avg_win | 27.2872 |
| net_avg_loss | -41.2721 |
| avg_hold_time_bars | 9.4068 |
| exposure | 0.4541 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
