# EMA Hourly Continuation — AERO/USDT P8_100

**Symbol:** AERO/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 466 |
| net_profit_factor | 0.9992 |
| net_win_rate | 0.5386 |
| gross_profit_factor | 1.1519 |
| gross_win_rate | 0.5386 |
| sharpe_ratio | 0.0623 |
| sortino_ratio | 0.0194 |
| max_drawdown | 0.2261 |
| cagr | -0.0008 |
| net_avg_win | 103.7883 |
| net_avg_loss | -121.2587 |
| avg_hold_time_bars | 31.1330 |
| exposure | 0.6595 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
