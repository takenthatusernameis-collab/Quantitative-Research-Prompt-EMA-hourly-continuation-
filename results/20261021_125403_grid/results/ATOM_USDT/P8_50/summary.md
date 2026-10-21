# EMA Hourly Continuation — ATOM/USDT P8_50

**Symbol:** ATOM/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 600 |
| net_profit_factor | 0.7697 |
| net_win_rate | 0.5033 |
| gross_profit_factor | 1.0067 |
| gross_win_rate | 0.5033 |
| sharpe_ratio | -1.9531 |
| sortino_ratio | -0.6865 |
| max_drawdown | 0.5560 |
| cagr | -0.2707 |
| net_avg_win | 60.5551 |
| net_avg_loss | -79.7348 |
| avg_hold_time_bars | 17.9083 |
| exposure | 0.4884 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
