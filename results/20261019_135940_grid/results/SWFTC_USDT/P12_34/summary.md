# EMA Hourly Continuation — SWFTC/USDT P12_34

**Symbol:** SWFTC/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1215 |
| net_profit_factor | 0.3498 |
| net_win_rate | 0.3984 |
| gross_profit_factor | 0.6894 |
| gross_win_rate | 0.4123 |
| sharpe_ratio | -10.8084 |
| sortino_ratio | -5.2958 |
| max_drawdown | 0.9989 |
| cagr | -0.9329 |
| net_avg_win | 11.1045 |
| net_avg_loss | -21.0168 |
| avg_hold_time_bars | 4.5704 |
| exposure | 0.2524 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
