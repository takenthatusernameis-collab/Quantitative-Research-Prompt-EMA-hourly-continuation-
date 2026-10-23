# EMA Hourly Continuation — DUSK/USDT P21_100

**Symbol:** DUSK/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 649 |
| net_profit_factor | 0.6454 |
| net_win_rate | 0.4622 |
| gross_profit_factor | 0.8968 |
| gross_win_rate | 0.4684 |
| sharpe_ratio | -3.5663 |
| sortino_ratio | -1.2826 |
| max_drawdown | 0.7982 |
| cagr | -0.4523 |
| net_avg_win | 47.2834 |
| net_avg_loss | -62.9793 |
| avg_hold_time_bars | 13.3837 |
| exposure | 0.3948 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
