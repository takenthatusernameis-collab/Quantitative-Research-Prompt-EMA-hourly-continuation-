# EMA Hourly Continuation — BONK/USDT P20_26

**Symbol:** BONK/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 156 |
| net_profit_factor | 0.8652 |
| net_win_rate | 0.5321 |
| gross_profit_factor | 1.1299 |
| gross_win_rate | 0.5321 |
| sharpe_ratio | -0.5531 |
| sortino_ratio | -0.0997 |
| max_drawdown | 0.1820 |
| cagr | -0.0461 |
| net_avg_win | 86.3590 |
| net_avg_loss | -113.4891 |
| avg_hold_time_bars | 5.5833 |
| exposure | 0.0396 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
