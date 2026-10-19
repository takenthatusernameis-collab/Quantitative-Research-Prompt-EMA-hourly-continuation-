# EMA Hourly Continuation — ALGO/USDT P55_144

**Symbol:** ALGO/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 468 |
| net_profit_factor | 0.5816 |
| net_win_rate | 0.4765 |
| gross_profit_factor | 0.9294 |
| gross_win_rate | 0.4829 |
| sharpe_ratio | -3.5364 |
| sortino_ratio | -1.0721 |
| max_drawdown | 0.7343 |
| cagr | -0.4044 |
| net_avg_win | 45.3732 |
| net_avg_loss | -71.0039 |
| avg_hold_time_bars | 11.8590 |
| exposure | 0.2523 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
