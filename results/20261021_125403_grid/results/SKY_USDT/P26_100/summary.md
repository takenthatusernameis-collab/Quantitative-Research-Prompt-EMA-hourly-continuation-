# EMA Hourly Continuation — SKY/USDT P26_100

**Symbol:** SKY/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 369 |
| net_profit_factor | 0.7884 |
| net_win_rate | 0.5041 |
| gross_profit_factor | 1.0102 |
| gross_win_rate | 0.5041 |
| sharpe_ratio | -1.5896 |
| sortino_ratio | -0.4843 |
| max_drawdown | 0.4978 |
| cagr | -0.2002 |
| net_avg_win | 73.5112 |
| net_avg_loss | -94.7716 |
| avg_hold_time_bars | 19.1545 |
| exposure | 0.3941 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
