# EMA Hourly Continuation — SAFE/USDT P89_100

**Symbol:** SAFE/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 119 |
| net_profit_factor | 0.5564 |
| net_win_rate | 0.4454 |
| gross_profit_factor | 0.7781 |
| gross_win_rate | 0.4454 |
| sharpe_ratio | -1.8720 |
| sortino_ratio | -0.2924 |
| max_drawdown | 0.2970 |
| cagr | -0.1256 |
| net_avg_win | 67.2889 |
| net_avg_loss | -97.1135 |
| avg_hold_time_bars | 9.9580 |
| exposure | 0.0543 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
