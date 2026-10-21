# EMA Hourly Continuation — POLYX/USDT P34_89

**Symbol:** POLYX/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 494 |
| net_profit_factor | 0.7391 |
| net_win_rate | 0.4919 |
| gross_profit_factor | 0.9854 |
| gross_win_rate | 0.4919 |
| sharpe_ratio | -2.3039 |
| sortino_ratio | -0.7323 |
| max_drawdown | 0.6068 |
| cagr | -0.2850 |
| net_avg_win | 66.3742 |
| net_avg_loss | -86.9439 |
| avg_hold_time_bars | 10.7591 |
| exposure | 0.2416 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
