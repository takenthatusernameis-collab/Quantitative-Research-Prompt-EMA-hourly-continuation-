# EMA Hourly Continuation — FIL/USDT P20_26

**Symbol:** FIL/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 148 |
| net_profit_factor | 0.6018 |
| net_win_rate | 0.4595 |
| gross_profit_factor | 0.8608 |
| gross_win_rate | 0.4595 |
| sharpe_ratio | -1.9599 |
| sortino_ratio | -0.3410 |
| max_drawdown | 0.3571 |
| cagr | -0.1439 |
| net_avg_win | 71.8158 |
| net_avg_loss | -101.4284 |
| avg_hold_time_bars | 4.6216 |
| exposure | 0.0311 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
