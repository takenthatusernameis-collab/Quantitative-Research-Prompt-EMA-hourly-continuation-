# EMA Hourly Continuation — CKB/USDT P8_55

**Symbol:** CKB/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1085 |
| net_profit_factor | 0.6187 |
| net_win_rate | 0.4498 |
| gross_profit_factor | 0.9403 |
| gross_win_rate | 0.4645 |
| sharpe_ratio | -6.4698 |
| sortino_ratio | -2.9923 |
| max_drawdown | 0.9737 |
| cagr | -0.7634 |
| net_avg_win | 32.3553 |
| net_avg_loss | -42.7495 |
| avg_hold_time_bars | 9.7502 |
| exposure | 0.4809 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
