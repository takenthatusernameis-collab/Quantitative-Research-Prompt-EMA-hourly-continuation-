# EMA Hourly Continuation — DBR/USDT P34_50

**Symbol:** DBR/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 543 |
| net_profit_factor | 0.3657 |
| net_win_rate | 0.3978 |
| gross_profit_factor | 0.9006 |
| gross_win_rate | 0.4512 |
| sharpe_ratio | -8.8610 |
| sortino_ratio | -3.3251 |
| max_drawdown | 0.9661 |
| cagr | -0.8123 |
| net_avg_win | 25.7634 |
| net_avg_loss | -46.5351 |
| avg_hold_time_bars | 4.9374 |
| exposure | 0.1525 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
