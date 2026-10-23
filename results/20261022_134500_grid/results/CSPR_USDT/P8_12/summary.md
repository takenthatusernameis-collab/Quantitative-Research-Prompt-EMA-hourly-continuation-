# EMA Hourly Continuation — CSPR/USDT P8_12

**Symbol:** CSPR/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1991 |
| net_profit_factor | 0.1466 |
| net_win_rate | 0.3074 |
| gross_profit_factor | 0.5910 |
| gross_win_rate | 0.3446 |
| sharpe_ratio | -21.0308 |
| sortino_ratio | -13.6224 |
| max_drawdown | 1.0000 |
| cagr | -0.9994 |
| net_avg_win | 2.8059 |
| net_avg_loss | -8.4969 |
| avg_hold_time_bars | 1.7820 |
| exposure | 0.1613 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
