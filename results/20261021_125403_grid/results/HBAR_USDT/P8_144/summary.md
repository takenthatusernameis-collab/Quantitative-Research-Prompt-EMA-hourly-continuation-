# EMA Hourly Continuation — HBAR/USDT P8_144

**Symbol:** HBAR/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 347 |
| net_profit_factor | 0.9117 |
| net_win_rate | 0.5274 |
| gross_profit_factor | 1.1082 |
| gross_win_rate | 0.5274 |
| sharpe_ratio | -0.5319 |
| sortino_ratio | -0.1428 |
| max_drawdown | 0.3518 |
| cagr | -0.0674 |
| net_avg_win | 90.6927 |
| net_avg_loss | -110.9973 |
| avg_hold_time_bars | 48.1066 |
| exposure | 0.7588 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
