# EMA Hourly Continuation — ANYONE/USDT P8_21

**Symbol:** ANYONE/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1435 |
| net_profit_factor | 0.4983 |
| net_win_rate | 0.4348 |
| gross_profit_factor | 0.7970 |
| gross_win_rate | 0.4425 |
| sharpe_ratio | -8.8685 |
| sortino_ratio | -4.9810 |
| max_drawdown | 0.9958 |
| cagr | -0.9103 |
| net_avg_win | 15.8479 |
| net_avg_loss | -24.4710 |
| avg_hold_time_bars | 3.5498 |
| exposure | 0.2574 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
