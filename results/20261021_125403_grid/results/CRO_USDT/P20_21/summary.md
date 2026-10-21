# EMA Hourly Continuation — CRO/USDT P20_21

**Symbol:** CRO/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 151 |
| net_profit_factor | 0.4608 |
| net_win_rate | 0.4371 |
| gross_profit_factor | 0.7601 |
| gross_win_rate | 0.4371 |
| sharpe_ratio | -2.8242 |
| sortino_ratio | -0.4986 |
| max_drawdown | 0.4577 |
| cagr | -0.2066 |
| net_avg_win | 57.0568 |
| net_avg_loss | -96.1490 |
| avg_hold_time_bars | 4.6424 |
| exposure | 0.0319 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
