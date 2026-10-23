# EMA Hourly Continuation — CTSI/USDT P20_26

**Symbol:** CTSI/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1189 |
| net_profit_factor | 0.2361 |
| net_win_rate | 0.3776 |
| gross_profit_factor | 0.7523 |
| gross_win_rate | 0.4306 |
| sharpe_ratio | -13.0451 |
| sortino_ratio | -6.4775 |
| max_drawdown | 0.9998 |
| cagr | -0.9643 |
| net_avg_win | 6.8823 |
| net_avg_loss | -17.6863 |
| avg_hold_time_bars | 2.7897 |
| exposure | 0.1508 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
