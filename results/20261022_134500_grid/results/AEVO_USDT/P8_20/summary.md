# EMA Hourly Continuation — AEVO/USDT P8_20

**Symbol:** AEVO/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1625 |
| net_profit_factor | 0.4625 |
| net_win_rate | 0.4400 |
| gross_profit_factor | 0.8481 |
| gross_win_rate | 0.4597 |
| sharpe_ratio | -10.2976 |
| sortino_ratio | -5.8200 |
| max_drawdown | 0.9994 |
| cagr | -0.9448 |
| net_avg_win | 12.0286 |
| net_avg_loss | -20.4327 |
| avg_hold_time_bars | 3.3372 |
| exposure | 0.2454 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
