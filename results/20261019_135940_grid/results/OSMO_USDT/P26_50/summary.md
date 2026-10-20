# EMA Hourly Continuation — OSMO/USDT P26_50

**Symbol:** OSMO/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 910 |
| net_profit_factor | 0.4200 |
| net_win_rate | 0.3978 |
| gross_profit_factor | 0.8454 |
| gross_win_rate | 0.4198 |
| sharpe_ratio | -9.2663 |
| sortino_ratio | -3.9833 |
| max_drawdown | 0.9928 |
| cagr | -0.8594 |
| net_avg_win | 19.8578 |
| net_avg_loss | -31.2337 |
| avg_hold_time_bars | 4.5341 |
| exposure | 0.1875 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
