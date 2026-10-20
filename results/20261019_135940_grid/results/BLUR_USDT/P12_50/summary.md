# EMA Hourly Continuation — BLUR/USDT P12_50

**Symbol:** BLUR/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1013 |
| net_profit_factor | 0.6170 |
| net_win_rate | 0.4748 |
| gross_profit_factor | 0.9807 |
| gross_win_rate | 0.4886 |
| sharpe_ratio | -5.3386 |
| sortino_ratio | -2.3864 |
| max_drawdown | 0.9470 |
| cagr | -0.6819 |
| net_avg_win | 31.6341 |
| net_avg_loss | -46.3532 |
| avg_hold_time_bars | 7.7473 |
| exposure | 0.3551 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
