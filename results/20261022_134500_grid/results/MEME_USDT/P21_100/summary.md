# EMA Hourly Continuation — MEME/USDT P21_100

**Symbol:** MEME/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 650 |
| net_profit_factor | 0.6415 |
| net_win_rate | 0.4723 |
| gross_profit_factor | 0.9450 |
| gross_win_rate | 0.4769 |
| sharpe_ratio | -3.8543 |
| sortino_ratio | -1.3811 |
| max_drawdown | 0.8264 |
| cagr | -0.4855 |
| net_avg_win | 47.3035 |
| net_avg_loss | -66.0003 |
| avg_hold_time_bars | 14.9154 |
| exposure | 0.4407 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
