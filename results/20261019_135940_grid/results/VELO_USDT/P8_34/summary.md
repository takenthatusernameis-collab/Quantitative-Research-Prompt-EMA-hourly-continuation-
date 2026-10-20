# EMA Hourly Continuation — VELO/USDT P8_34

**Symbol:** VELO/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1461 |
| net_profit_factor | 0.5366 |
| net_win_rate | 0.4531 |
| gross_profit_factor | 0.8046 |
| gross_win_rate | 0.4600 |
| sharpe_ratio | -7.6838 |
| sortino_ratio | -4.1204 |
| max_drawdown | 0.9938 |
| cagr | -0.8651 |
| net_avg_win | 17.3765 |
| net_avg_loss | -26.8309 |
| avg_hold_time_bars | 4.7618 |
| exposure | 0.3162 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
