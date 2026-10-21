# EMA Hourly Continuation — T/USDT P8_55

**Symbol:** T/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 678 |
| net_profit_factor | 0.7679 |
| net_win_rate | 0.5029 |
| gross_profit_factor | 1.0459 |
| gross_win_rate | 0.5029 |
| sharpe_ratio | -2.4959 |
| sortino_ratio | -0.9292 |
| max_drawdown | 0.6914 |
| cagr | -0.3469 |
| net_avg_win | 63.8949 |
| net_avg_loss | -84.1942 |
| avg_hold_time_bars | 15.2212 |
| exposure | 0.4670 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
