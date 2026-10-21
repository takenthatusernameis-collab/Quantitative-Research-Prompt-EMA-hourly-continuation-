# EMA Hourly Continuation — PEPE/USDT P8_144

**Symbol:** PEPE/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 321 |
| net_profit_factor | 0.9461 |
| net_win_rate | 0.5296 |
| gross_profit_factor | 1.1161 |
| gross_win_rate | 0.5296 |
| sharpe_ratio | -0.2701 |
| sortino_ratio | -0.0698 |
| max_drawdown | 0.1697 |
| cagr | -0.0363 |
| net_avg_win | 91.5617 |
| net_avg_loss | -108.9563 |
| avg_hold_time_bars | 51.3396 |
| exposure | 0.7491 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
