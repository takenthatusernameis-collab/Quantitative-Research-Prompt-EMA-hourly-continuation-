# EMA Hourly Continuation — CTSI/USDT P8_50

**Symbol:** CTSI/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1084 |
| net_profit_factor | 0.6433 |
| net_win_rate | 0.4779 |
| gross_profit_factor | 1.0317 |
| gross_win_rate | 0.4871 |
| sharpe_ratio | -5.4205 |
| sortino_ratio | -2.5113 |
| max_drawdown | 0.9533 |
| cagr | -0.6990 |
| net_avg_win | 33.1032 |
| net_avg_loss | -47.0974 |
| avg_hold_time_bars | 9.0895 |
| exposure | 0.4479 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
