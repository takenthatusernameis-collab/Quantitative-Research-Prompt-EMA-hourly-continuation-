# EMA Hourly Continuation — IOTA/USDT P20_26

**Symbol:** IOTA/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1203 |
| net_profit_factor | 0.1661 |
| net_win_rate | 0.3674 |
| gross_profit_factor | 0.6590 |
| gross_win_rate | 0.4206 |
| sharpe_ratio | -14.0453 |
| sortino_ratio | -7.0770 |
| max_drawdown | 0.9999 |
| cagr | -0.9757 |
| net_avg_win | 4.5050 |
| net_avg_loss | -15.7560 |
| avg_hold_time_bars | 2.0599 |
| exposure | 0.1126 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
