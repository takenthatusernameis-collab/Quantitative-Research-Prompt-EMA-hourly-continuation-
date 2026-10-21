# EMA Hourly Continuation — CTC/USDT P21_100

**Symbol:** CTC/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 504 |
| net_profit_factor | 0.8193 |
| net_win_rate | 0.5218 |
| gross_profit_factor | 1.0723 |
| gross_win_rate | 0.5218 |
| sharpe_ratio | -1.3189 |
| sortino_ratio | -0.4258 |
| max_drawdown | 0.4642 |
| cagr | -0.1800 |
| net_avg_win | 67.6431 |
| net_avg_loss | -90.1041 |
| avg_hold_time_bars | 16.5813 |
| exposure | 0.3799 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
