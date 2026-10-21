# EMA Hourly Continuation — CHR/USDT P8_12

**Symbol:** CHR/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 384 |
| net_profit_factor | 0.7018 |
| net_win_rate | 0.4844 |
| gross_profit_factor | 0.9973 |
| gross_win_rate | 0.4844 |
| sharpe_ratio | -2.5378 |
| sortino_ratio | -0.7113 |
| max_drawdown | 0.6203 |
| cagr | -0.2791 |
| net_avg_win | 71.1028 |
| net_avg_loss | -95.1750 |
| avg_hold_time_bars | 5.2943 |
| exposure | 0.0920 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
