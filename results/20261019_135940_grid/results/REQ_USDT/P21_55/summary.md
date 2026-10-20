# EMA Hourly Continuation — REQ/USDT P21_55

**Symbol:** REQ/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1050 |
| net_profit_factor | 0.4198 |
| net_win_rate | 0.4010 |
| gross_profit_factor | 0.8789 |
| gross_win_rate | 0.4343 |
| sharpe_ratio | -10.5423 |
| sortino_ratio | -4.8729 |
| max_drawdown | 0.9979 |
| cagr | -0.9140 |
| net_avg_win | 17.1509 |
| net_avg_loss | -27.3441 |
| avg_hold_time_bars | 5.8286 |
| exposure | 0.2782 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
