# EMA Hourly Continuation — AURORA/USDT P55_200

**Symbol:** AURORA/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 365 |
| net_profit_factor | 0.5838 |
| net_win_rate | 0.4521 |
| gross_profit_factor | 0.8463 |
| gross_win_rate | 0.4575 |
| sharpe_ratio | -3.2510 |
| sortino_ratio | -0.8734 |
| max_drawdown | 0.6560 |
| cagr | -0.3409 |
| net_avg_win | 55.1676 |
| net_avg_loss | -77.9644 |
| avg_hold_time_bars | 20.0329 |
| exposure | 0.3324 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
