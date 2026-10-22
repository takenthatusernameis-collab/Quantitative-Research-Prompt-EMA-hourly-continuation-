# EMA Hourly Continuation — DASH/USDT P26_100

**Symbol:** DASH/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 688 |
| net_profit_factor | 0.5115 |
| net_win_rate | 0.4448 |
| gross_profit_factor | 0.8861 |
| gross_win_rate | 0.4535 |
| sharpe_ratio | -5.5913 |
| sortino_ratio | -2.0601 |
| max_drawdown | 0.9210 |
| cagr | -0.6323 |
| net_avg_win | 31.4505 |
| net_avg_loss | -49.2493 |
| avg_hold_time_bars | 10.8416 |
| exposure | 0.3390 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
