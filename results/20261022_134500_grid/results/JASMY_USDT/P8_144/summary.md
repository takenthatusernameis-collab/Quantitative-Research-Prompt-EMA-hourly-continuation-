# EMA Hourly Continuation — JASMY/USDT P8_144

**Symbol:** JASMY/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 454 |
| net_profit_factor | 0.8367 |
| net_win_rate | 0.5330 |
| gross_profit_factor | 1.1210 |
| gross_win_rate | 0.5330 |
| sharpe_ratio | -1.1252 |
| sortino_ratio | -0.3421 |
| max_drawdown | 0.4244 |
| cagr | -0.1510 |
| net_avg_win | 71.3613 |
| net_avg_loss | -97.3600 |
| avg_hold_time_bars | 36.7687 |
| exposure | 0.7588 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
