# EMA Hourly Continuation — RENDER/USDT P26_34

**Symbol:** RENDER/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 930 |
| net_profit_factor | 0.2576 |
| net_win_rate | 0.3677 |
| gross_profit_factor | 0.6135 |
| gross_win_rate | 0.4011 |
| sharpe_ratio | -12.7756 |
| sortino_ratio | -6.0489 |
| max_drawdown | 0.9990 |
| cagr | -0.9584 |
| net_avg_win | 10.1333 |
| net_avg_loss | -22.8832 |
| avg_hold_time_bars | 2.0441 |
| exposure | 0.1003 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
