# EMA Hourly Continuation — RLC/USDT P55_100

**Symbol:** RLC/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 648 |
| net_profit_factor | 0.4924 |
| net_win_rate | 0.4568 |
| gross_profit_factor | 0.8900 |
| gross_win_rate | 0.4784 |
| sharpe_ratio | -5.2464 |
| sortino_ratio | -1.8957 |
| max_drawdown | 0.9023 |
| cagr | -0.5952 |
| net_avg_win | 29.3862 |
| net_avg_loss | -50.1879 |
| avg_hold_time_bars | 5.5648 |
| exposure | 0.1639 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
