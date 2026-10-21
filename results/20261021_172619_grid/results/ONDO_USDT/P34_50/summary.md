# EMA Hourly Continuation — ONDO/USDT P34_50

**Symbol:** ONDO/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 203 |
| net_profit_factor | 0.8431 |
| net_win_rate | 0.5320 |
| gross_profit_factor | 1.1404 |
| gross_win_rate | 0.5320 |
| sharpe_ratio | -0.7659 |
| sortino_ratio | -0.1578 |
| max_drawdown | 0.2254 |
| cagr | -0.0702 |
| net_avg_win | 83.1562 |
| net_avg_loss | -112.1317 |
| avg_hold_time_bars | 6.2562 |
| exposure | 0.0577 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
