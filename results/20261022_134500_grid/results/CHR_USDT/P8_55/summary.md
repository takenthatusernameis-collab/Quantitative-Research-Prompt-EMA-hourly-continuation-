# EMA Hourly Continuation — CHR/USDT P8_55

**Symbol:** CHR/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1078 |
| net_profit_factor | 0.5634 |
| net_win_rate | 0.4341 |
| gross_profit_factor | 0.8660 |
| gross_win_rate | 0.4481 |
| sharpe_ratio | -6.6126 |
| sortino_ratio | -3.0480 |
| max_drawdown | 0.9759 |
| cagr | -0.7674 |
| net_avg_win | 26.8790 |
| net_avg_loss | -36.6013 |
| avg_hold_time_bars | 9.5724 |
| exposure | 0.4669 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
