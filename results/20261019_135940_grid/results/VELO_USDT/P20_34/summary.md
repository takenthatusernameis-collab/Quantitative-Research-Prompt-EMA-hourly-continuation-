# EMA Hourly Continuation — VELO/USDT P20_34

**Symbol:** VELO/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1211 |
| net_profit_factor | 0.4739 |
| net_win_rate | 0.4178 |
| gross_profit_factor | 0.7935 |
| gross_win_rate | 0.4335 |
| sharpe_ratio | -9.6511 |
| sortino_ratio | -4.7524 |
| max_drawdown | 0.9973 |
| cagr | -0.9043 |
| net_avg_win | 17.7553 |
| net_avg_loss | -26.8887 |
| avg_hold_time_bars | 2.6491 |
| exposure | 0.1458 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
