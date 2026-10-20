# EMA Hourly Continuation — MOVR/USDT P34_50

**Symbol:** MOVR/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 928 |
| net_profit_factor | 0.3597 |
| net_win_rate | 0.4224 |
| gross_profit_factor | 0.8277 |
| gross_win_rate | 0.4537 |
| sharpe_ratio | -9.0801 |
| sortino_ratio | -3.9313 |
| max_drawdown | 0.9932 |
| cagr | -0.8615 |
| net_avg_win | 14.2329 |
| net_avg_loss | -28.9355 |
| avg_hold_time_bars | 2.7619 |
| exposure | 0.1165 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
