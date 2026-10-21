# EMA Hourly Continuation — MANA/USDT P20_55

**Symbol:** MANA/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 517 |
| net_profit_factor | 0.7438 |
| net_win_rate | 0.4971 |
| gross_profit_factor | 1.0127 |
| gross_win_rate | 0.4971 |
| sharpe_ratio | -2.3096 |
| sortino_ratio | -0.7534 |
| max_drawdown | 0.6113 |
| cagr | -0.2916 |
| net_avg_win | 65.4399 |
| net_avg_loss | -86.9657 |
| avg_hold_time_bars | 8.9516 |
| exposure | 0.2104 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
