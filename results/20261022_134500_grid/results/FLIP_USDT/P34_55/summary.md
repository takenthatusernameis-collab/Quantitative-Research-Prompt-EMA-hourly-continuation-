# EMA Hourly Continuation — FLIP/USDT P34_55

**Symbol:** FLIP/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 566 |
| net_profit_factor | 0.3273 |
| net_win_rate | 0.3463 |
| gross_profit_factor | 0.7385 |
| gross_win_rate | 0.3958 |
| sharpe_ratio | -9.4265 |
| sortino_ratio | -3.2223 |
| max_drawdown | 0.9868 |
| cagr | -0.8187 |
| net_avg_win | 24.4822 |
| net_avg_loss | -39.6250 |
| avg_hold_time_bars | 6.2774 |
| exposure | 0.1615 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
