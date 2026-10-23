# EMA Hourly Continuation — IOTX/USDT P21_100

**Symbol:** IOTX/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 714 |
| net_profit_factor | 0.5825 |
| net_win_rate | 0.4608 |
| gross_profit_factor | 0.9098 |
| gross_win_rate | 0.4748 |
| sharpe_ratio | -4.8411 |
| sortino_ratio | -1.8120 |
| max_drawdown | 0.8940 |
| cagr | -0.5844 |
| net_avg_win | 37.7386 |
| net_avg_loss | -55.3603 |
| avg_hold_time_bars | 12.1190 |
| exposure | 0.3933 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
