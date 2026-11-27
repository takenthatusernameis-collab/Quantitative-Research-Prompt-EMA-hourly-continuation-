# EMA Hourly Continuation — SHR/USDT P26_50

**Symbol:** SHR/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1203 |
| net_profit_factor | 0.3505 |
| net_win_rate | 0.3126 |
| gross_profit_factor | 0.5708 |
| gross_win_rate | 0.3175 |
| sharpe_ratio | -12.5145 |
| sortino_ratio | -6.0882 |
| max_drawdown | 0.9995 |
| cagr | -0.9507 |
| net_avg_win | 14.3432 |
| net_avg_loss | -18.6070 |
| avg_hold_time_bars | 3.4572 |
| exposure | 0.1882 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
