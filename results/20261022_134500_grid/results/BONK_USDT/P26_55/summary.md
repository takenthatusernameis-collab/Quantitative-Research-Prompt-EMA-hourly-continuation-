# EMA Hourly Continuation — BONK/USDT P26_55

**Symbol:** BONK/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 913 |
| net_profit_factor | 0.5368 |
| net_win_rate | 0.4655 |
| gross_profit_factor | 0.9024 |
| gross_win_rate | 0.4830 |
| sharpe_ratio | -5.8819 |
| sortino_ratio | -2.4967 |
| max_drawdown | 0.9550 |
| cagr | -0.7045 |
| net_avg_win | 25.9938 |
| net_avg_loss | -42.1701 |
| avg_hold_time_bars | 4.1763 |
| exposure | 0.1733 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
