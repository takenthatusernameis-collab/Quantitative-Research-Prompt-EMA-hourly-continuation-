# EMA Hourly Continuation — SLP/USDT P8_50

**Symbol:** SLP/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1259 |
| net_profit_factor | 0.5814 |
| net_win_rate | 0.4488 |
| gross_profit_factor | 0.9297 |
| gross_win_rate | 0.4583 |
| sharpe_ratio | -7.5098 |
| sortino_ratio | -3.7275 |
| max_drawdown | 0.9903 |
| cagr | -0.8399 |
| net_avg_win | 24.3313 |
| net_avg_loss | -34.0731 |
| avg_hold_time_bars | 7.7943 |
| exposure | 0.4460 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
