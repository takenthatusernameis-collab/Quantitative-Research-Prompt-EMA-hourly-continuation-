# EMA Hourly Continuation — ALEX/USDT P55_200

**Symbol:** ALEX/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 337 |
| net_profit_factor | 0.5309 |
| net_win_rate | 0.3976 |
| gross_profit_factor | 0.7149 |
| gross_win_rate | 0.3976 |
| sharpe_ratio | -4.1101 |
| sortino_ratio | -1.0499 |
| max_drawdown | 0.7340 |
| cagr | -0.3989 |
| net_avg_win | 60.9372 |
| net_avg_loss | -75.7658 |
| avg_hold_time_bars | 25.7270 |
| exposure | 0.3941 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
