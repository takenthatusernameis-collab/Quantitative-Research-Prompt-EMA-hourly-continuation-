# EMA Hourly Continuation — KAS/USDT P34_200

**Symbol:** KAS/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 309 |
| net_profit_factor | 0.7483 |
| net_win_rate | 0.4790 |
| gross_profit_factor | 0.9037 |
| gross_win_rate | 0.4790 |
| sharpe_ratio | -1.5423 |
| sortino_ratio | -0.3858 |
| max_drawdown | 0.3834 |
| cagr | -0.1630 |
| net_avg_win | 72.3717 |
| net_avg_loss | -88.9100 |
| avg_hold_time_bars | 28.8447 |
| exposure | 0.4051 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
