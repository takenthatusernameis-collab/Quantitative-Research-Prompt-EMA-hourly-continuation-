# EMA Hourly Continuation — TRADE/USDT P21_100

**Symbol:** TRADE/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 533 |
| net_profit_factor | 0.5708 |
| net_win_rate | 0.4522 |
| gross_profit_factor | 0.8323 |
| gross_win_rate | 0.4522 |
| sharpe_ratio | -4.1049 |
| sortino_ratio | -1.3117 |
| max_drawdown | 0.8133 |
| cagr | -0.4814 |
| net_avg_win | 44.5760 |
| net_avg_loss | -64.4548 |
| avg_hold_time_bars | 16.6585 |
| exposure | 0.4036 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
