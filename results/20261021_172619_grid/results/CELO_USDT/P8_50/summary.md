# EMA Hourly Continuation — CELO/USDT P8_50

**Symbol:** CELO/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 738 |
| net_profit_factor | 0.7869 |
| net_win_rate | 0.4932 |
| gross_profit_factor | 1.0062 |
| gross_win_rate | 0.4932 |
| sharpe_ratio | -2.4104 |
| sortino_ratio | -0.9340 |
| max_drawdown | 0.6731 |
| cagr | -0.3499 |
| net_avg_win | 67.2055 |
| net_avg_loss | -83.1250 |
| avg_hold_time_bars | 13.5664 |
| exposure | 0.4531 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
