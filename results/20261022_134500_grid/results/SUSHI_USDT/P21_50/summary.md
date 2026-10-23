# EMA Hourly Continuation — SUSHI/USDT P21_50

**Symbol:** SUSHI/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 990 |
| net_profit_factor | 0.5080 |
| net_win_rate | 0.4354 |
| gross_profit_factor | 0.8991 |
| gross_win_rate | 0.4556 |
| sharpe_ratio | -7.5119 |
| sortino_ratio | -3.3127 |
| max_drawdown | 0.9839 |
| cagr | -0.8036 |
| net_avg_win | 23.5572 |
| net_avg_loss | -35.7576 |
| avg_hold_time_bars | 4.7061 |
| exposure | 0.2108 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
