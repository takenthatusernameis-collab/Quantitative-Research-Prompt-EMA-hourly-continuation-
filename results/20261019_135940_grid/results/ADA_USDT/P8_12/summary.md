# EMA Hourly Continuation — ADA/USDT P8_12

**Symbol:** ADA/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1841 |
| net_profit_factor | 0.1493 |
| net_win_rate | 0.3341 |
| gross_profit_factor | 0.6555 |
| gross_win_rate | 0.3922 |
| sharpe_ratio | -20.2084 |
| sortino_ratio | -12.8144 |
| max_drawdown | 1.0000 |
| cagr | -0.9991 |
| net_avg_win | 2.8539 |
| net_avg_loss | -9.5882 |
| avg_hold_time_bars | 1.6350 |
| exposure | 0.1368 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
