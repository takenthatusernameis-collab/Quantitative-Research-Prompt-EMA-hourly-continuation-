# EMA Hourly Continuation — SUN/USDT P8_12

**Symbol:** SUN/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1607 |
| net_profit_factor | 0.0663 |
| net_win_rate | 0.2707 |
| gross_profit_factor | 0.4745 |
| gross_win_rate | 0.4101 |
| sharpe_ratio | -21.9106 |
| sortino_ratio | -13.6426 |
| max_drawdown | 1.0000 |
| cagr | -0.9995 |
| net_avg_win | 1.6313 |
| net_avg_loss | -9.1379 |
| avg_hold_time_bars | 2.8090 |
| exposure | 0.2043 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
