# EMA Hourly Continuation — OGN/USDT P89_100

**Symbol:** OGN/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 182 |
| net_profit_factor | 0.4152 |
| net_win_rate | 0.4176 |
| gross_profit_factor | 0.6845 |
| gross_win_rate | 0.4176 |
| sharpe_ratio | -3.3906 |
| sortino_ratio | -0.6546 |
| max_drawdown | 0.5393 |
| cagr | -0.2619 |
| net_avg_win | 49.9957 |
| net_avg_loss | -86.3272 |
| avg_hold_time_bars | 5.1264 |
| exposure | 0.0422 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
