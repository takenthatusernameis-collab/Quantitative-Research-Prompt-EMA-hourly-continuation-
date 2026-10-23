# EMA Hourly Continuation — AVA/USDT P89_100

**Symbol:** AVA/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 606 |
| net_profit_factor | 0.2322 |
| net_win_rate | 0.4010 |
| gross_profit_factor | 0.7253 |
| gross_win_rate | 0.4439 |
| sharpe_ratio | -9.0270 |
| sortino_ratio | -3.2216 |
| max_drawdown | 0.9857 |
| cagr | -0.8130 |
| net_avg_win | 12.2599 |
| net_avg_loss | -35.3463 |
| avg_hold_time_bars | 2.2096 |
| exposure | 0.0609 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
