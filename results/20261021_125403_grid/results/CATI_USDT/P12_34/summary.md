# EMA Hourly Continuation — CATI/USDT P12_34

**Symbol:** CATI/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 440 |
| net_profit_factor | 0.5796 |
| net_win_rate | 0.4386 |
| gross_profit_factor | 0.7421 |
| gross_win_rate | 0.4386 |
| sharpe_ratio | -3.7000 |
| sortino_ratio | -1.2075 |
| max_drawdown | 0.6909 |
| cagr | -0.4292 |
| net_avg_win | 49.2021 |
| net_avg_loss | -66.3364 |
| avg_hold_time_bars | 8.1568 |
| exposure | 0.1967 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
