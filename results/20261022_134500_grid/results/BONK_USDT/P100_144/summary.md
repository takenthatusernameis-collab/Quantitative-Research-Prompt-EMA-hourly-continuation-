# EMA Hourly Continuation — BONK/USDT P100_144

**Symbol:** BONK/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 497 |
| net_profit_factor | 0.4449 |
| net_win_rate | 0.4125 |
| gross_profit_factor | 0.7086 |
| gross_win_rate | 0.4165 |
| sharpe_ratio | -5.9040 |
| sortino_ratio | -1.8598 |
| max_drawdown | 0.9035 |
| cagr | -0.6006 |
| net_avg_win | 35.2011 |
| net_avg_loss | -55.5433 |
| avg_hold_time_bars | 4.4990 |
| exposure | 0.1016 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
