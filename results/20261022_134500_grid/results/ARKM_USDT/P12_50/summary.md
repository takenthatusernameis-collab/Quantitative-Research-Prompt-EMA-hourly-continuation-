# EMA Hourly Continuation — ARKM/USDT P12_50

**Symbol:** ARKM/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1086 |
| net_profit_factor | 0.6156 |
| net_win_rate | 0.4521 |
| gross_profit_factor | 0.9261 |
| gross_win_rate | 0.4613 |
| sharpe_ratio | -6.2000 |
| sortino_ratio | -2.8818 |
| max_drawdown | 0.9691 |
| cagr | -0.7459 |
| net_avg_win | 31.5686 |
| net_avg_loss | -42.3188 |
| avg_hold_time_bars | 7.2514 |
| exposure | 0.3580 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
