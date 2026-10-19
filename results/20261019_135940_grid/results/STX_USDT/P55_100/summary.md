# EMA Hourly Continuation — STX/USDT P55_100

**Symbol:** STX/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 605 |
| net_profit_factor | 0.5358 |
| net_win_rate | 0.4529 |
| gross_profit_factor | 0.8676 |
| gross_win_rate | 0.4628 |
| sharpe_ratio | -5.0361 |
| sortino_ratio | -1.7450 |
| max_drawdown | 0.8791 |
| cagr | -0.5656 |
| net_avg_win | 36.9842 |
| net_avg_loss | -57.1397 |
| avg_hold_time_bars | 4.8926 |
| exposure | 0.1339 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
