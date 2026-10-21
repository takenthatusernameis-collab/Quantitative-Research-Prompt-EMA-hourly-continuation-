# EMA Hourly Continuation — PENDLE/USDT P8_100

**Symbol:** PENDLE/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 447 |
| net_profit_factor | 0.8680 |
| net_win_rate | 0.5056 |
| gross_profit_factor | 1.0121 |
| gross_win_rate | 0.5056 |
| sharpe_ratio | -0.8852 |
| sortino_ratio | -0.2683 |
| max_drawdown | 0.3403 |
| cagr | -0.1194 |
| net_avg_win | 79.5864 |
| net_avg_loss | -93.7596 |
| avg_hold_time_bars | 32.6868 |
| exposure | 0.6641 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
