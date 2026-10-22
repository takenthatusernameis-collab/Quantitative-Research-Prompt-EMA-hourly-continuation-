# EMA Hourly Continuation — QNT/USDT P89_200

**Symbol:** QNT/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 423 |
| net_profit_factor | 0.7179 |
| net_win_rate | 0.5248 |
| gross_profit_factor | 1.1115 |
| gross_win_rate | 0.5296 |
| sharpe_ratio | -2.0986 |
| sortino_ratio | -0.6138 |
| max_drawdown | 0.5312 |
| cagr | -0.2497 |
| net_avg_win | 58.9055 |
| net_avg_loss | -90.6283 |
| avg_hold_time_bars | 11.0615 |
| exposure | 0.2127 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
