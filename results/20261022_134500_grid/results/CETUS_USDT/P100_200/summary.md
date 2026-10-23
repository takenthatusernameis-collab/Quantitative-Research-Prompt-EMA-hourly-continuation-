# EMA Hourly Continuation — CETUS/USDT P100_200

**Symbol:** CETUS/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 371 |
| net_profit_factor | 0.6319 |
| net_win_rate | 0.4528 |
| gross_profit_factor | 0.9186 |
| gross_win_rate | 0.4609 |
| sharpe_ratio | -3.2826 |
| sortino_ratio | -0.8885 |
| max_drawdown | 0.6653 |
| cagr | -0.3473 |
| net_avg_win | 67.3602 |
| net_avg_loss | -88.2152 |
| avg_hold_time_bars | 9.4124 |
| exposure | 0.1580 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
