# EMA Hourly Continuation — TFUEL/USDT P8_144

**Symbol:** TFUEL/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 582 |
| net_profit_factor | 0.6788 |
| net_win_rate | 0.4485 |
| gross_profit_factor | 0.8424 |
| gross_win_rate | 0.4485 |
| sharpe_ratio | -3.2438 |
| sortino_ratio | -1.1063 |
| max_drawdown | 0.7306 |
| cagr | -0.3987 |
| net_avg_win | 58.5321 |
| net_avg_loss | -70.1112 |
| avg_hold_time_bars | 23.9553 |
| exposure | 0.6309 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
