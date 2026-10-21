# EMA Hourly Continuation — CYBER/USDT P34_100

**Symbol:** CYBER/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 474 |
| net_profit_factor | 0.7815 |
| net_win_rate | 0.5084 |
| gross_profit_factor | 1.0207 |
| gross_win_rate | 0.5084 |
| sharpe_ratio | -1.6515 |
| sortino_ratio | -0.5160 |
| max_drawdown | 0.4984 |
| cagr | -0.2115 |
| net_avg_win | 66.6920 |
| net_avg_loss | -88.2728 |
| avg_hold_time_bars | 12.2954 |
| exposure | 0.2649 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
