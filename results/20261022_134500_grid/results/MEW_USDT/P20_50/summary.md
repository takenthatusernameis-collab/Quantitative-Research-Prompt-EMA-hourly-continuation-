# EMA Hourly Continuation — MEW/USDT P20_50

**Symbol:** MEW/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 965 |
| net_profit_factor | 0.4946 |
| net_win_rate | 0.4580 |
| gross_profit_factor | 0.7895 |
| gross_win_rate | 0.4694 |
| sharpe_ratio | -6.3283 |
| sortino_ratio | -2.7553 |
| max_drawdown | 0.9665 |
| cagr | -0.7392 |
| net_avg_win | 21.3812 |
| net_avg_loss | -36.5360 |
| avg_hold_time_bars | 4.7648 |
| exposure | 0.2090 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
