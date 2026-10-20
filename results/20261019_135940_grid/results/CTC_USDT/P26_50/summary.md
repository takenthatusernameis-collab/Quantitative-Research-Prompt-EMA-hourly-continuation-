# EMA Hourly Continuation — CTC/USDT P26_50

**Symbol:** CTC/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 947 |
| net_profit_factor | 0.4201 |
| net_win_rate | 0.4340 |
| gross_profit_factor | 0.8858 |
| gross_win_rate | 0.4636 |
| sharpe_ratio | -8.5322 |
| sortino_ratio | -3.7240 |
| max_drawdown | 0.9910 |
| cagr | -0.8435 |
| net_avg_win | 17.4609 |
| net_avg_loss | -31.8685 |
| avg_hold_time_bars | 4.1003 |
| exposure | 0.1765 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
