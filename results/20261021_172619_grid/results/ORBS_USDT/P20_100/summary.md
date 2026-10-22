# EMA Hourly Continuation — ORBS/USDT P20_100

**Symbol:** ORBS/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 527 |
| net_profit_factor | 0.7161 |
| net_win_rate | 0.4782 |
| gross_profit_factor | 0.9638 |
| gross_win_rate | 0.4782 |
| sharpe_ratio | -2.8840 |
| sortino_ratio | -0.9431 |
| max_drawdown | 0.7038 |
| cagr | -0.3528 |
| net_avg_win | 66.5418 |
| net_avg_loss | -85.1476 |
| avg_hold_time_bars | 18.4004 |
| exposure | 0.4408 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
