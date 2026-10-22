# EMA Hourly Continuation — JUP/USDT P8_20

**Symbol:** JUP/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1679 |
| net_profit_factor | 0.4953 |
| net_win_rate | 0.4574 |
| gross_profit_factor | 0.9900 |
| gross_win_rate | 0.4741 |
| sharpe_ratio | -10.2309 |
| sortino_ratio | -5.8813 |
| max_drawdown | 0.9994 |
| cagr | -0.9483 |
| net_avg_win | 12.7694 |
| net_avg_loss | -21.7355 |
| avg_hold_time_bars | 2.7022 |
| exposure | 0.2062 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
