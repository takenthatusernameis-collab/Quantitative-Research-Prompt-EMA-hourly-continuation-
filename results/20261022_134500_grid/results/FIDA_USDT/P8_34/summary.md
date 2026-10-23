# EMA Hourly Continuation — FIDA/USDT P8_34

**Symbol:** FIDA/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1305 |
| net_profit_factor | 0.4932 |
| net_win_rate | 0.4460 |
| gross_profit_factor | 0.8260 |
| gross_win_rate | 0.4590 |
| sharpe_ratio | -7.6644 |
| sortino_ratio | -3.8864 |
| max_drawdown | 0.9912 |
| cagr | -0.8469 |
| net_avg_win | 16.5738 |
| net_avg_loss | -27.0513 |
| avg_hold_time_bars | 6.1088 |
| exposure | 0.3607 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
