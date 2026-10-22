# EMA Hourly Continuation — BONK/USDT P34_50

**Symbol:** BONK/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 886 |
| net_profit_factor | 0.4392 |
| net_win_rate | 0.4436 |
| gross_profit_factor | 0.8706 |
| gross_win_rate | 0.4605 |
| sharpe_ratio | -8.0502 |
| sortino_ratio | -3.3739 |
| max_drawdown | 0.9869 |
| cagr | -0.8202 |
| net_avg_win | 19.6585 |
| net_avg_loss | -35.6823 |
| avg_hold_time_bars | 2.4413 |
| exposure | 0.0983 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
