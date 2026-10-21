# EMA Hourly Continuation — ZETA/USDT P21_55

**Symbol:** ZETA/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 546 |
| net_profit_factor | 0.7162 |
| net_win_rate | 0.4835 |
| gross_profit_factor | 0.9437 |
| gross_win_rate | 0.4835 |
| sharpe_ratio | -2.6276 |
| sortino_ratio | -0.8761 |
| max_drawdown | 0.6456 |
| cagr | -0.3302 |
| net_avg_win | 60.8033 |
| net_avg_loss | -79.4803 |
| avg_hold_time_bars | 8.6667 |
| exposure | 0.2141 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
