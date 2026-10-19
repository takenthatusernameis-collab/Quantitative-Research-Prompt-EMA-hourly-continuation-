# EMA Hourly Continuation — AERO/USDT P55_100

**Symbol:** AERO/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 529 |
| net_profit_factor | 0.5109 |
| net_win_rate | 0.4575 |
| gross_profit_factor | 0.8503 |
| gross_win_rate | 0.4612 |
| sharpe_ratio | -4.6241 |
| sortino_ratio | -1.4831 |
| max_drawdown | 0.8440 |
| cagr | -0.5212 |
| net_avg_win | 36.3753 |
| net_avg_loss | -60.0347 |
| avg_hold_time_bars | 5.6560 |
| exposure | 0.1360 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
