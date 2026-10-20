# EMA Hourly Continuation — ORBS/USDT P8_55

**Symbol:** ORBS/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1033 |
| net_profit_factor | 0.5106 |
| net_win_rate | 0.4211 |
| gross_profit_factor | 0.8871 |
| gross_win_rate | 0.4395 |
| sharpe_ratio | -8.1968 |
| sortino_ratio | -3.6930 |
| max_drawdown | 0.9900 |
| cagr | -0.8389 |
| net_avg_win | 23.7431 |
| net_avg_loss | -33.8231 |
| avg_hold_time_bars | 11.2333 |
| exposure | 0.5275 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
