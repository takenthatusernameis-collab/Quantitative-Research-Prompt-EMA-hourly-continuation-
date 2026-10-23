# EMA Hourly Continuation — ALPINE/USDT P89_144

**Symbol:** ALPINE/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 528 |
| net_profit_factor | 0.4780 |
| net_win_rate | 0.4508 |
| gross_profit_factor | 0.8956 |
| gross_win_rate | 0.4773 |
| sharpe_ratio | -5.4759 |
| sortino_ratio | -1.7847 |
| max_drawdown | 0.8862 |
| cagr | -0.5775 |
| net_avg_win | 34.0493 |
| net_avg_loss | -58.4651 |
| avg_hold_time_bars | 6.9091 |
| exposure | 0.1658 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
