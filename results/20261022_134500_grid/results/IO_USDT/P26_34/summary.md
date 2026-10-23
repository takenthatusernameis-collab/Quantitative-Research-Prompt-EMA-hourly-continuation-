# EMA Hourly Continuation — IO/USDT P26_34

**Symbol:** IO/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 990 |
| net_profit_factor | 0.3705 |
| net_win_rate | 0.4131 |
| gross_profit_factor | 0.7381 |
| gross_win_rate | 0.4313 |
| sharpe_ratio | -10.4412 |
| sortino_ratio | -4.8344 |
| max_drawdown | 0.9971 |
| cagr | -0.9151 |
| net_avg_win | 14.3454 |
| net_avg_loss | -27.2589 |
| avg_hold_time_bars | 2.0303 |
| exposure | 0.0973 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
