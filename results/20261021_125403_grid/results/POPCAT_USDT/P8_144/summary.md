# EMA Hourly Continuation — POPCAT/USDT P8_144

**Symbol:** POPCAT/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 324 |
| net_profit_factor | 0.8676 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 0.9882 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -0.8466 |
| sortino_ratio | -0.2345 |
| max_drawdown | 0.2780 |
| cagr | -0.1057 |
| net_avg_win | 86.7598 |
| net_avg_loss | -100.0040 |
| avg_hold_time_bars | 42.8858 |
| exposure | 0.7340 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
