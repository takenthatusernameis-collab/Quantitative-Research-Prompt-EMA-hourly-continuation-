# EMA Hourly Continuation — AAVE/USDT P8_50

**Symbol:** AAVE/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1091 |
| net_profit_factor | 0.5787 |
| net_win_rate | 0.4620 |
| gross_profit_factor | 0.9230 |
| gross_win_rate | 0.4665 |
| sharpe_ratio | -6.4976 |
| sortino_ratio | -3.0140 |
| max_drawdown | 0.9758 |
| cagr | -0.7682 |
| net_avg_win | 26.5648 |
| net_avg_loss | -39.4111 |
| avg_hold_time_bars | 9.6123 |
| exposure | 0.4767 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
