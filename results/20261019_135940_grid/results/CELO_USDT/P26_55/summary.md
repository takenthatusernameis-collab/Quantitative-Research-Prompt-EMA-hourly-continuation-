# EMA Hourly Continuation — CELO/USDT P26_55

**Symbol:** CELO/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 889 |
| net_profit_factor | 0.5078 |
| net_win_rate | 0.4623 |
| gross_profit_factor | 0.8879 |
| gross_win_rate | 0.4747 |
| sharpe_ratio | -6.2197 |
| sortino_ratio | -2.6092 |
| max_drawdown | 0.9594 |
| cagr | -0.7170 |
| net_avg_win | 24.0575 |
| net_avg_loss | -40.7393 |
| avg_hold_time_bars | 4.9528 |
| exposure | 0.1992 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
