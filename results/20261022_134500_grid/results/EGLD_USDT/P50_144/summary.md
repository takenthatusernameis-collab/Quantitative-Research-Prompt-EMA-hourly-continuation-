# EMA Hourly Continuation — EGLD/USDT P50_144

**Symbol:** EGLD/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 468 |
| net_profit_factor | 0.5631 |
| net_win_rate | 0.4765 |
| gross_profit_factor | 0.9159 |
| gross_win_rate | 0.4872 |
| sharpe_ratio | -3.5577 |
| sortino_ratio | -1.0869 |
| max_drawdown | 0.7313 |
| cagr | -0.4044 |
| net_avg_win | 42.0582 |
| net_avg_loss | -67.9867 |
| avg_hold_time_bars | 13.9957 |
| exposure | 0.2977 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
