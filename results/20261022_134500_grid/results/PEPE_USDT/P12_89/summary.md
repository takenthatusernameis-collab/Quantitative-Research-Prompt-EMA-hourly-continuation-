# EMA Hourly Continuation — PEPE/USDT P12_89

**Symbol:** PEPE/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 671 |
| net_profit_factor | 0.6078 |
| net_win_rate | 0.4545 |
| gross_profit_factor | 0.8875 |
| gross_win_rate | 0.4605 |
| sharpe_ratio | -4.6651 |
| sortino_ratio | -1.6879 |
| max_drawdown | 0.8834 |
| cagr | -0.5634 |
| net_avg_win | 44.4635 |
| net_avg_loss | -60.9652 |
| avg_hold_time_bars | 17.8987 |
| exposure | 0.5459 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
