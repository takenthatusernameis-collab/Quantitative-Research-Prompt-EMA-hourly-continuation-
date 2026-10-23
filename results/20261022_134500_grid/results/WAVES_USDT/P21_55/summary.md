# EMA Hourly Continuation — WAVES/USDT P21_55

**Symbol:** WAVES/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1107 |
| net_profit_factor | 0.4100 |
| net_win_rate | 0.3984 |
| gross_profit_factor | 0.8573 |
| gross_win_rate | 0.4273 |
| sharpe_ratio | -10.6022 |
| sortino_ratio | -4.9904 |
| max_drawdown | 0.9983 |
| cagr | -0.9201 |
| net_avg_win | 15.7271 |
| net_avg_loss | -25.4025 |
| avg_hold_time_bars | 4.9124 |
| exposure | 0.2472 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
