# EMA Hourly Continuation — CELR/USDT P34_89

**Symbol:** CELR/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 691 |
| net_profit_factor | 0.5671 |
| net_win_rate | 0.4588 |
| gross_profit_factor | 0.8881 |
| gross_win_rate | 0.4718 |
| sharpe_ratio | -4.6881 |
| sortino_ratio | -1.7243 |
| max_drawdown | 0.8802 |
| cagr | -0.5658 |
| net_avg_win | 36.2914 |
| net_avg_loss | -54.2380 |
| avg_hold_time_bars | 8.2779 |
| exposure | 0.2588 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
