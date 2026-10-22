# EMA Hourly Continuation — ORBS/USDT P8_34

**Symbol:** ORBS/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 804 |
| net_profit_factor | 0.5515 |
| net_win_rate | 0.4179 |
| gross_profit_factor | 0.8045 |
| gross_win_rate | 0.4179 |
| sharpe_ratio | -6.4324 |
| sortino_ratio | -2.5972 |
| max_drawdown | 0.9514 |
| cagr | -0.7001 |
| net_avg_win | 34.8198 |
| net_avg_loss | -45.3282 |
| avg_hold_time_bars | 9.7438 |
| exposure | 0.3561 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
