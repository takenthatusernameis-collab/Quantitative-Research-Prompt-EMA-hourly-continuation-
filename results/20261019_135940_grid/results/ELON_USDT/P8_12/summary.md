# EMA Hourly Continuation — ELON/USDT P8_12

**Symbol:** ELON/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1595 |
| net_profit_factor | 0.1710 |
| net_win_rate | 0.3737 |
| gross_profit_factor | 0.5533 |
| gross_win_rate | 0.4025 |
| sharpe_ratio | -16.1327 |
| sortino_ratio | -9.3566 |
| max_drawdown | 1.0000 |
| cagr | -0.9921 |
| net_avg_win | 3.4609 |
| net_avg_loss | -12.0747 |
| avg_hold_time_bars | 1.9912 |
| exposure | 0.1444 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
