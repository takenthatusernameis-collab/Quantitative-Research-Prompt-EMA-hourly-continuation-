# EMA Hourly Continuation — HNT/USDT P50_89

**Symbol:** HNT/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 742 |
| net_profit_factor | 0.4511 |
| net_win_rate | 0.4394 |
| gross_profit_factor | 0.7648 |
| gross_win_rate | 0.4542 |
| sharpe_ratio | -6.0511 |
| sortino_ratio | -2.3379 |
| max_drawdown | 0.9420 |
| cagr | -0.6710 |
| net_avg_win | 23.6613 |
| net_avg_loss | -41.1069 |
| avg_hold_time_bars | 4.9771 |
| exposure | 0.1679 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
