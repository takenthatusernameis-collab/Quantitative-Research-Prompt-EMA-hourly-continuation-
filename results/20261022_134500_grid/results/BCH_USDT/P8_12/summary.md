# EMA Hourly Continuation — BCH/USDT P8_12

**Symbol:** BCH/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1819 |
| net_profit_factor | 0.1550 |
| net_win_rate | 0.3024 |
| gross_profit_factor | 0.7107 |
| gross_win_rate | 0.3909 |
| sharpe_ratio | -21.9503 |
| sortino_ratio | -14.1664 |
| max_drawdown | 1.0000 |
| cagr | -0.9996 |
| net_avg_win | 3.3359 |
| net_avg_loss | -9.3261 |
| avg_hold_time_bars | 1.8664 |
| exposure | 0.1543 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
