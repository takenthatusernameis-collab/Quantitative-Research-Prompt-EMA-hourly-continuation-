# EMA Hourly Continuation — LQTY/USDT P26_89

**Symbol:** LQTY/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 479 |
| net_profit_factor | 0.7088 |
| net_win_rate | 0.4739 |
| gross_profit_factor | 0.9011 |
| gross_win_rate | 0.4739 |
| sharpe_ratio | -2.4318 |
| sortino_ratio | -0.7564 |
| max_drawdown | 0.6032 |
| cagr | -0.2942 |
| net_avg_win | 62.6981 |
| net_avg_loss | -79.6862 |
| avg_hold_time_bars | 14.7474 |
| exposure | 0.3197 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
