# EMA Hourly Continuation — BIGTIME/USDT P8_144

**Symbol:** BIGTIME/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 287 |
| net_profit_factor | 0.9848 |
| net_win_rate | 0.5366 |
| gross_profit_factor | 1.1542 |
| gross_win_rate | 0.5366 |
| sharpe_ratio | -0.0288 |
| sortino_ratio | -0.0070 |
| max_drawdown | 0.1168 |
| cagr | -0.0087 |
| net_avg_win | 91.3525 |
| net_avg_loss | -107.4113 |
| avg_hold_time_bars | 61.5679 |
| exposure | 0.7996 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
