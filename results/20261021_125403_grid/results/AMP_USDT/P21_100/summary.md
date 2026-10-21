# EMA Hourly Continuation — AMP/USDT P21_100

**Symbol:** AMP/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 547 |
| net_profit_factor | 0.5307 |
| net_win_rate | 0.4095 |
| gross_profit_factor | 0.6892 |
| gross_win_rate | 0.4095 |
| sharpe_ratio | -4.6245 |
| sortino_ratio | -1.5292 |
| max_drawdown | 0.8406 |
| cagr | -0.5073 |
| net_avg_win | 41.9463 |
| net_avg_loss | -54.8149 |
| avg_hold_time_bars | 15.5119 |
| exposure | 0.3857 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
