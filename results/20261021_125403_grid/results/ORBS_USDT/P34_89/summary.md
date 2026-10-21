# EMA Hourly Continuation — ORBS/USDT P34_89

**Symbol:** ORBS/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 486 |
| net_profit_factor | 0.6677 |
| net_win_rate | 0.4691 |
| gross_profit_factor | 0.9521 |
| gross_win_rate | 0.4691 |
| sharpe_ratio | -3.3217 |
| sortino_ratio | -1.0465 |
| max_drawdown | 0.7233 |
| cagr | -0.3812 |
| net_avg_win | 61.7221 |
| net_avg_loss | -81.6934 |
| avg_hold_time_bars | 11.0514 |
| exposure | 0.2441 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
