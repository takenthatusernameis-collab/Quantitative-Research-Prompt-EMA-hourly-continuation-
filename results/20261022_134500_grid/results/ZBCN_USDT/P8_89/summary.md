# EMA Hourly Continuation — ZBCN/USDT P8_89

**Symbol:** ZBCN/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 959 |
| net_profit_factor | 0.6731 |
| net_win_rate | 0.4891 |
| gross_profit_factor | 0.9555 |
| gross_win_rate | 0.4922 |
| sharpe_ratio | -3.8994 |
| sortino_ratio | -1.7121 |
| max_drawdown | 0.8759 |
| cagr | -0.5611 |
| net_avg_win | 38.1500 |
| net_avg_loss | -54.2478 |
| avg_hold_time_bars | 13.0626 |
| exposure | 0.5796 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
