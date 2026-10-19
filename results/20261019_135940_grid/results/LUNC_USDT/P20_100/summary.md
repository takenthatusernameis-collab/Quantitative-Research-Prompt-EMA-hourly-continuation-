# EMA Hourly Continuation — LUNC/USDT P20_100

**Symbol:** LUNC/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 757 |
| net_profit_factor | 0.4136 |
| net_win_rate | 0.4386 |
| gross_profit_factor | 0.7300 |
| gross_win_rate | 0.4478 |
| sharpe_ratio | -6.3601 |
| sortino_ratio | -2.4492 |
| max_drawdown | 0.9538 |
| cagr | -0.6995 |
| net_avg_win | 20.2094 |
| net_avg_loss | -38.1679 |
| avg_hold_time_bars | 11.1942 |
| exposure | 0.3852 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
