# EMA Hourly Continuation — PROM/USDT P8_34

**Symbol:** PROM/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1314 |
| net_profit_factor | 0.5347 |
| net_win_rate | 0.4330 |
| gross_profit_factor | 0.9867 |
| gross_win_rate | 0.4635 |
| sharpe_ratio | -9.0316 |
| sortino_ratio | -4.5693 |
| max_drawdown | 0.9969 |
| cagr | -0.8990 |
| net_avg_win | 20.1319 |
| net_avg_loss | -28.7563 |
| avg_hold_time_bars | 6.5830 |
| exposure | 0.3932 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
